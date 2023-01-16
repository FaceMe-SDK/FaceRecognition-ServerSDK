import sys
sys.path.append('.')

import cv2
import numpy as np
import os
import base64

from faceme_recog import fmr_version
from faceme_recog import fmr_init
from faceme_recog import fmr_extract_feature
from faceme_recog import fmr_compare_feature

licenseKey = "XXXXX-XXXXX-XXXXX-XXXXX"      # Please request license to support@faceme.tw
modelFolder = os.path.abspath(os.path.dirname(__file__)) + '/../model'

if __name__ == '__main__':

    version = fmr_version()
    print("version: ", version.decode('utf-8'))

    ret = fmr_init(modelFolder.encode('utf-8'), licenseKey.encode('utf-8'))
    if ret != 0:
        print(f"init failed: {ret}")
        exit(-1)

    imagePath1 = os.path.abspath(os.path.dirname(__file__)) + '/../test_image/Carlos_Menem_0018.jpg'
    image1 = cv2.imread(imagePath1)
    if image1 is None:
        print("image1 is null!")
        exit(-1)
        
    imagePath2 = os.path.abspath(os.path.dirname(__file__)) + '/../test_image/Carlos_Menem_0020.jpg'
    image2 = cv2.imread(imagePath2)
    if image2 is None:
        print("image2 is null!")
        exit(-1)

    faceRect1 = np.zeros([4], dtype=np.int32)
    feature1 = np.zeros([2048], dtype=np.uint8)
    featureSize1 = np.zeros([1], dtype=np.int32)

    ret = fmr_extract_feature(image1, image1.shape[1], image1.shape[0], faceRect1, feature1, featureSize1)
    if ret == -1:
        print("license error!")
        exit(-1)
    elif ret == -2:
        print("init error!")
        exit(-1)
    elif ret == 0:
        print("image1: no face detected!")
        exit(-1)
    elif ret == 1:
        print("image1: feature extracted!")

    faceRect2 = np.zeros([4], dtype=np.int32)
    feature2 = np.zeros([2048], dtype=np.uint8)
    featureSize2 = np.zeros([1], dtype=np.int32)

    ret = fmr_extract_feature(image2, image2.shape[1], image2.shape[0], faceRect2, feature2, featureSize2)
    if ret == -1:
        print("license error!")
        exit(-1)
    elif ret == -2:
        print("init error!")
        exit(-1)
    elif ret == 0:
        print("image2: no face detected!")
        exit(-1)
    elif ret == 1:
        print("image2: feature extracted!")

    similarity = fmr_compare_feature(feature1, feature2)
    if similarity > 0.67:
        print(f"same person!, similarity = {similarity}")
    else:
        print(f"different person!, similarity = {similarity}")

    exit(0)