<p align="center">
  <img width="640" src="https://user-images.githubusercontent.com/122285115/212581402-a095f46c-480b-45c9-98bc-23622d3a11e1.jpg">
  <h4 align="center">FaceMe® provides system integrators with fast, flexible and extremely precise facial recognition that can be deployed across a number of scenarios, including security, access control, public safety, fintech, smart retail and home protection.</h4>  
</p>

> **Note**
>
> SDK is fully on-premise, processing all happens on hosting server and no data leaves server.

## Project Structure
```graphql
./FaceLivenessDetection-ServerSDK
  ├─ bin/linux_x86_64                 - # Core library files
  │  ├─ openvino
  │  ├─ libfaceme_recog1.so
  │  └─ libimutils.so
  ├─ cpp                              - # C++ example
  │  ├─ CMakeLists.txt                - # CMake file for build example
  │  ├─ faceme_recog.h                - # C++ header file to include library
  │  └─ main.cpp                      - # C++ example code
  ├─ flask                            - # Python flask API serving example
  │  ├─ app.py                        - # Flask example code
  │  └─ requirements.txt              - # Python requirement list
  ├─ model                            - # NN dictionary files for library
  │  ├─ data1.bin
  │  ├─ data2.bin  
  │  └─ data3.bin
  ├─ python                           - # Python example
  │  ├─ faceme_recog.py               - # Python library Import Interface file
  │  ├─ main.py                       - # Python example code
  │  └─ requirements.txt              - # Python requirement list
  ├─ test_image                       - # Test Images
  └─ Dockerfile                       - # Docker script for python flask API serving example
```

## Setup Project
#### - Linux
- Download repo and extract it
- Install system dependencies
```
sudo apt-get update -y
sudo apt-get install -y libcurl4-openssl-dev libssl-dev libopencv-dev
```
- Copy libraries into system folder
```
cp -rf ./bin/linux_x86_64/openvino/* /usr/lib
cp ./bin/linux_x86_64/libimutils.so /usr/lib
```
#### - Windows
Contact us by Email support@faceme.tw
#### - Request license
Subscribe free trial at our [Subscription Page](https://sdk.faceme.tw/#contact-us)  
You will get email with trial license key ("XXXXX-XXXXX-XXXXX-XXXXX").
  
## C++ Example
- Replace license key in main.cpp https://github.com/FaceMe-SDK/FaceRecognition-ServerSDK/blob/6d5152e7ab146f2cee25bde96f09b8a76f48f33c/cpp/main.cpp#L1-L7
- Build project
```
cd cpp
mkdir build && cd build
cmake ..
make
```
- Run project
```
./example_recognition --image1 ../../test_image/Carlos_Menem_0018.jpg --image2 ../../test_image/Carlos_Menem_0020.jpg --model ../../model
```

## Python Example
- Replace license key in main.py https://github.com/FaceMe-SDK/FaceRecognition-ServerSDK/blob/6d5152e7ab146f2cee25bde96f09b8a76f48f33c/python/main.py#L11-L17
- Install dependencies
```
cd python
pip install -r requirements.txt
```
- Run project
```
python main.py
```
## Python Flask Example
- Replace license key in app.py https://github.com/FaceMe-SDK/FaceRecognition-ServerSDK/blob/6d5152e7ab146f2cee25bde96f09b8a76f48f33c/flask/app.py#L20-L26
- Install dependencies
```
cd flask
pip install -r requirements.txt
```
- Run project
```
python app.py
```
<p align="center">
  <img width="360" src="https://user-images.githubusercontent.com/122285115/212585049-63740d35-e44b-46d4-b02b-fbe4a50fa0e2.png">&emsp;&emsp;
  <img width="360" src="https://user-images.githubusercontent.com/122285115/212585096-8361b446-a0ee-4726-b2f4-906994c17144.png">
</p>


## Docker Flask Example
- Replace license key in app.py https://github.com/FaceMe-SDK/FaceRecognition-ServerSDK/blob/6d5152e7ab146f2cee25bde96f09b8a76f48f33c/flask/app.py#L20-L26
- Build docker image
```
docker build --pull --rm -f "Dockerfile" -t facemerecognition:latest "."
```
- Run image
```
docker run facemerecognition
```
## Request license
Subscribe free trial at our [Subscription Page](https://sdk.faceme.tw/#contact-us)  
You will get email with trial license key ("XXXXX-XXXXX-XXXXX-XXXXX").
