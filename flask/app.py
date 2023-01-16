import sys
sys.path.append('.')
sys.path.append('../python')

from flask import Flask, request, jsonify
from time import gmtime, strftime
import os
import base64
import json
import cv2
import numpy as np

from faceme_recog import fmr_version
from faceme_recog import fmr_init
from faceme_recog import fmr_extract_feature
from faceme_recog import fmr_compare_feature

app = Flask(__name__) 

app.config['SITE'] = "http://0.0.0.0:8888/"
app.config['DEBUG'] = False

licenseKey = "XXXXX-XXXXX-XXXXX-XXXXX"      # Please request license to support@faceme.tw
modelFolder = os.path.abspath(os.path.dirname(__file__)) + '/../model'

version = fmr_version()
print("version: ", version.decode('utf-8'))

ret = fmr_init(modelFolder.encode('utf-8'), licenseKey.encode('utf-8'))
if ret != 0:
    print(f"init failed: {ret}");
    exit(-1)

@app.route('/compare_face', methods=['POST'])
def compare_face():
    file1 = request.files['image1']
    image1 = cv2.imdecode(np.fromstring(file1.read(), np.uint8), cv2.IMREAD_COLOR)
    if image1 is None:
        result = "image1: is null!"
        status = "ok"
        response = jsonify({"status": status, "data": {"result": result}})
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    file2 = request.files['image2']
    image2 = cv2.imdecode(np.fromstring(file2.read(), np.uint8), cv2.IMREAD_COLOR)
    if image2 is None:
        result = "image2: is null!"
        status = "ok"
        response = jsonify({"status": status, "data": {"result": result}})
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    faceRect1 = np.zeros([4], dtype=np.int32)
    feature1 = np.zeros([2048], dtype=np.uint8)
    featureSize1 = np.zeros([1], dtype=np.int32)

    ret = fmr_extract_feature(image1, image1.shape[1], image1.shape[0], faceRect1, feature1, featureSize1)
    if ret <= 0:
        if ret == -1:
            result = "license error!"
        elif ret == -2:
            result = "init error!"
        elif ret == 0:
            result = "image1: no face detected!"

        status = "ok"
        response = jsonify({"status": status, "data": {"result": result}})
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    faceRect2 = np.zeros([4], dtype=np.int32)
    feature2 = np.zeros([2048], dtype=np.uint8)
    featureSize2 = np.zeros([1], dtype=np.int32)

    ret = fmr_extract_feature(image2, image2.shape[1], image2.shape[0], faceRect2, feature2, featureSize2)
    if ret <= 0:
        if ret == -1:
            result = "license error!"
        elif ret == -2:
            result = "init error!"
        elif ret == 0:
            result = "image2: no face detected!"

        status = "ok"
        response = jsonify({"status": status, "data": {"result": result}})
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    similarity = fmr_compare_feature(feature1, feature2)
    if similarity > 0.67:
        result = "same person!"
    else:
        result = "different person!"
  
    status = "ok"
    response = jsonify({"status": status, "data": {"result": result, "similarity": float(similarity)}})
    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


@app.route('/compare_face_base64', methods=['POST'])
def coompare_face_base64():
    content = request.get_json()
    imageBase641 = content['image1']
    image1 = cv2.imdecode(np.frombuffer(base64.b64decode(imageBase641), dtype=np.uint8), cv2.IMREAD_COLOR)

    if image1 is None:
        result = "image1: is null!"
        status = "ok"
        response = jsonify({"status": status, "data": {"result": result}})
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    imageBase642 = content['image2']
    image2 = cv2.imdecode(np.frombuffer(base64.b64decode(imageBase642), dtype=np.uint8), cv2.IMREAD_COLOR)

    if image2 is None:
        result = "image2: is null!"
        status = "ok"
        response = jsonify({"status": status, "data": {"result": result}})
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    faceRect1 = np.zeros([4], dtype=np.int32)
    feature1 = np.zeros([2048], dtype=np.uint8)
    featureSize1 = np.zeros([1], dtype=np.int32)

    ret = fmr_extract_feature(image1, image1.shape[1], image1.shape[0], faceRect1, feature1, featureSize1)
    if ret <= 0:
        if ret == -1:
            result = "license error!"
        elif ret == -2:
            result = "init error!"
        elif ret == 0:
            result = "image1: no face detected!"

        status = "ok"
        response = jsonify({"status": status, "data": {"result": result}})
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    faceRect2 = np.zeros([4], dtype=np.int32)
    feature2 = np.zeros([2048], dtype=np.uint8)
    featureSize2 = np.zeros([1], dtype=np.int32)

    ret = fmr_extract_feature(image2, image2.shape[1], image2.shape[0], faceRect2, feature2, featureSize2)
    if ret <= 0:
        if ret == -1:
            result = "license error!"
        elif ret == -2:
            result = "init error!"
        elif ret == 0:
            result = "image2: no face detected!"

        status = "ok"
        response = jsonify({"status": status, "data": {"result": result}})
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    similarity = fmr_compare_feature(feature1, feature2)
    if similarity > 0.67:
        result = "same person!"
    else:
        result = "different person!"
  
    status = "ok"
    response = jsonify({"status": status, "data": {"result": result, "similarity": float(similarity)}})
    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8888))
    app.run(host='0.0.0.0', port=port)