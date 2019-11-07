import cv2
import numpy as np
import scipy
import scipy.spatial
from matplotlib.pyplot import imread
import _pickle as pickle
import random
from random import shuffle
import os
from shutil import copy
import matplotlib.pyplot as plt
import sys

path = './PINS'
    
if len(sys.argv) == 2:
    path = sys.argv[1]

files = os.listdir(path)
for name in files:
    images_path = os.path.abspath(__file__)
    relative_path = name
    images_path = os.path.dirname(images_path) + '/PINS/' + relative_path
    filesTemp = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    sz = len(filesTemp)
    cut = int(0.8 * sz)
    shuffled_Temp = filesTemp
    shuffle(shuffled_Temp)
    Reference = shuffled_Temp[:cut]
    Test = shuffled_Temp[cut:]

    dirNameRef = '\\Data\\Referensi\\' + relative_path + 'Reference'
    dirNameTest = '\\Data\\DataUji\\' + relative_path + 'Test' 
    base = os.path.abspath(__file__)
    base = os.path.dirname(base)

    try:
        os.mkdir(base + dirNameRef)
        print("Directory " , dirNameRef ,  " Created ") 

    except FileExistsError:
        print("Directory " , dirNameRef ,  " already exists")

    try:
        os.mkdir(base + dirNameTest)
        print("Directory " , dirNameTest ,  " Created ") 

    except FileExistsError:
        print("Directory " , dirNameTest ,  " already exists")

    for temp in Reference:
        dst = base + dirNameRef 
        copy(temp, dst)
    for temp in Test:
        dst = base + dirNameTest 
        copy(temp, dst)