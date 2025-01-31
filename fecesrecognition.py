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
import tkinter as tkr
import ProgressBar as PB

def extract_features(image_path, vector_size=32):
    image = imread(image_path, 1)
    try:
        alg = cv2.KAZE_create()
        kps = alg.detect(image)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        kps, dsc = alg.compute(image, kps)
        if dsc is None:
            return None
        
        dsc = dsc.flatten()
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
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
        for i in range(32*64):
            v_norm += v[i] * v[i]
            vself_norm += vself[i] * vself[i]

        v_norm = math.sqrt(v_norm)
        vself_norm = math.sqrt(vself_norm)

        for i in range(32*64):
            a = v[i] / v_norm
            b = vself[i] / vself_norm
            res += (a - b) * (a - b)
        
        return math.sqrt(res)

    def euclidean_vector(self, vector):
        v = vector.reshape(-1)

        euclidean_result = np.arange(self.matrix.shape[0], dtype=float)
        i = 0
        PB.show_progress(len(self.matrix))
        for vtemp in (self.matrix):
            PB.update_bar()
            euclidean_result[i] = Matcher.euclidean_distance(vtemp, v)
            i+=1
        PB.close_bar()

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
        for i in range(32*64):
            res += v[i] * vself[i]
            v_norm += v[i] * v[i]
            vself_norm += vself[i] * vself[i]
        
        v_norm = math.sqrt(v_norm)
        vself_norm = math.sqrt(vself_norm)
        return res / (v_norm * vself_norm)

    def cosine_vector(self, vector):
        v = vector.reshape(-1)

        cosine_result = np.arange(self.matrix.shape[0], dtype=float)
        i = 0
        PB.show_progress(len(self.matrix))
        for vtemp in self.matrix:
            PB.update_bar()
            cosine_result[i] = Matcher.cosine_distance(vtemp, v)
            i+=1
        PB.close_bar()

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
    batch_extractor(Ref_images_path, "Ref_features.pck")

def find_match(TestFiles, metode, T):
    RefSet = Matcher("Ref_features.pck")
    tested_image = imread(TestFiles, 1)
    if (metode==2): 
        names, match = RefSet.match_cosine(TestFiles, T)

        all_image = [imread(path, 1) for path in names]
        return all_image, match, tested_image

    else:
        names, match = RefSet.match_euclidean(TestFiles, T)

        all_image = [imread(path, 1) for path in names]
        return all_image, match, tested_image
