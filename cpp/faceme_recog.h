#pragma once

#ifdef __cplusplus
extern "C" {
#endif

/*
Get SDK version
*/
const char* fmr_version();

/*
Init SDK
    ret == 0 -> successful, ret < 0 -> model error, ret > 0 -> license error
*/
int fmr_init(const char* dictPath, char* licenseKey);

/*
Extract facial feature
Check main.cpp for usage
    ret < 0 -> init error
    ret >= 0 -> detected face count
*/
int fmr_extract_feature(unsigned char* bgrData, int img_width, int img_height, int* faceBox, unsigned char* feats, int* featSize);

/*
Compare feature
Check main.cpp for usage
    return value: similarity between two feature
*/
double fmr_compare_feature(unsigned char* feat1, unsigned char* feat2);

#ifdef __cplusplus
}
#endif