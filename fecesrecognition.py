import cv2
import numpy as np
import scipy
import scipy.spatial
from matplotlib.pyplot import imread
import _pickle as pickle
import random
import os
import matplotlib.pyplot as plt
import sys
import math

# Feature extractor
def extract_features(image_path, vector_size=32):
    image = imread(image_path, 1)
    try:
        alg = cv2.KAZE_create()
        # Finding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        if dsc is None: # Handling NULL object
            return None
        
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print( 'Error: ', e)
        return None

    return dsc


def batch_extractor(images_path, pickled_db_path):
    folder = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for fold in folder:
        files = [os.path.join(fold, p) for p in sorted(os.listdir(fold))] 
        for f in files:
            print( 'Extracting features from image %s' % f)
            name = f.split('/')[-1].lower()
            temp = extract_features(f)
            if temp is not None:
                result[name] = temp
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)

class Matcher(object):

    def __init__(self, pickled_db_path="features.pck"):
        with open(pickled_db_path, 'rb') as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.items():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def euclidean_distance(vector1, vector2):
        v = vector2.reshape(-1)
        vself = vector1.reshape(-1)
        
        res = 0
        v_norm = 0
        vself_norm = 0
        for i in range(32*64): # There are 32*64 keypoints
            v_norm += v[i] * v[i]
            vself_norm += vself[i] * vself[i]

        v_norm = math.sqrt(v_norm)
        vself_norm = math.sqrt(vself_norm)

        for i in range(32*64):
            a = v[i] / v_norm
            b = vself[i] / vself_norm
            res += (a - b) ** 2
        
        return math.sqrt(res)

    def euclidean_vector(self, vector):
        # getting euclidean distance between search image and images database
        v = vector.reshape(-1)

        euclidean_result = np.arange(self.matrix.shape[0], dtype=float)
        i = 0
        for vtemp in self.matrix:
            euclidean_result[i] = Matcher.euclidean_distance(vtemp, v)
            i+=1

        return euclidean_result.reshape(-1)

    def match_euclidean(self, image_path, topn):
        features = extract_features(image_path)
        img_distances = self.euclidean_vector(features)

        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances[nearest_ids].tolist()

    def cosine_distance(vector1, vector2):
        v = vector2.reshape(-1)
        vself = vector1.reshape(-1)
        
        res = 0
        v_norm = 0
        vself_norm = 0
        for i in range(32*64): # There are 32*64 keypoints
            res += v[i] * vself[i]
            v_norm += v[i] * v[i]
            vself_norm += vself[i] * vself[i]
        
        v_norm = math.sqrt(v_norm)
        vself_norm = math.sqrt(vself_norm)
        return res / (v_norm * vself_norm)

    def cosine_vector(self, vector):
        # getting cosine similarity between search image and images database
        v = vector.reshape(-1)

        cosine_result = np.arange(self.matrix.shape[0], dtype=float)
        i = 0
        for vtemp in self.matrix:
            cosine_result[i] = Matcher.cosine_distance(vtemp, v)
            i+=1

        return cosine_result.reshape(-1)

    def match_cosine(self, image_path, topn):
        features = extract_features(image_path)
        img_distances = self.cosine_vector(features)
        
        nearest_ids = np.argsort(-img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances[nearest_ids].tolist()

def show_img(path):
    img = imread(path, 1)
    plt.imshow(img)
    plt.show()
    
def run_DataSet_extractor():
    Data_images_path = os.path.abspath(__file__)
    relative_path = '\\Data\\DataUji'
    Data_images_path = os.path.dirname(Data_images_path) + relative_path
    Data_files = [os.path.join(Data_images_path, p) for p in sorted(os.listdir(Data_images_path))]
    batch_extractor(Data_images_path, "Data_features.pck")
    
def run_Reference_extractor():
    Ref_images_path = os.path.abspath(__file__)
    relative_path = '\\Data\\Referensi'
    Ref_images_path = os.path.dirname(Ref_images_path) + relative_path
    Ref_files = [os.path.join(Ref_images_path, p) for p in sorted(os.listdir(Ref_images_path))]
    # getting 3 random images 
    # sample = random.sample(files, 3)
    batch_extractor(Ref_images_path, "Ref_features.pck")

# Run these to get the file packages
# run_DataSet_extractor()
# run_Reference_extractor()

def find_match(TestFiles, metode, T):
    RefSet = Matcher("Ref_features.pck")
    print(TestFiles)
    print( 'Query image ==========================================')
    show_img(TestFiles)
    if (metode==2): 
        names, match = RefSet.match_cosine(TestFiles, T)
        print( 'Result images ========================================')
        for i in range(T):
            # we got cosine distance, cosine distance between vectors
            print('Cosine======================================')
            print( 'Match %s' % (match[i]))
            show_img(names[i])
            print(names[i])

    if (metode==1):
        names2, match2 = RefSet.match_euclidean(TestFiles, T)
        print( 'Result images ========================================')
        for i in range(T):
            # we got euclidean distance, euclidean distance between vectors
            print('Euclidean======================================')
            print( 'Distance %s' % (match2[i]))
            show_img(names2[i])
            print(names2[i])

# Contoh find_match
# find_match("D:/_ALinGEO/Tubes2Algeo/Data/DataUji/pins_alexandra daddarioTest/alexandra daddario25.jpg", 1, 2)
