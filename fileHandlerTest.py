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

path = './PINS'
    
if len(sys.argv) == 2:
    path = sys.argv[1]

files = os.listdir(path)
for name in files:
    print(name)