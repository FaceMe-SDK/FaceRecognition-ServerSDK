#include <opencv2/opencv.hpp>
#include "faceme_recog.h"

#define LICENSE_KEY "XXXXX-XXXXX-XXXXX-XXXXX"		// Please request license to support@faceme.tw
#define SIMILARITY_THRESHOLD (0.67f)

void printUsage(const std::string& message = "");
bool parseArgs(int argc, char *argv[], std::map<std::string, std::string >& values);

int main(int argc, char *argv[]) {
    std::string modelFolder, imagePath1, imagePath2;
   
    // Parsing args
	std::map<std::string, std::string > args;
	if (!parseArgs(argc, argv, args)) {
		printUsage();
		return -1;
	}
	if (args.find("--image1") == args.end()) {
		printUsage("--image1 required");
		return -1;
	}
	if (args.find("--image2") == args.end()) {
		printUsage("--image2 required");
		return -1;
	}
	if (args.find("--model") == args.end()) {
		printUsage("--model required");
		return -1;
	}
	imagePath1 = args["--image1"];
	imagePath2 = args["--image2"];
    modelFolder = args["--model"];

    const char* version = fmr_version();
    printf("version: %s\n", version);

    int ret = fmr_init(modelFolder.c_str(), LICENSE_KEY);
    if(ret != 0) {
        printf("init failed: %d\n", ret);
        return -1;
    }

    cv::Mat image1 = cv::imread(imagePath1);
    if(image1.empty())
    {
        printf("image1 is null!\n");
        return -1;
    }

    cv::Mat image2 = cv::imread(imagePath2);
    if(image2.empty())
    {
        printf("image2 is null!\n");
        return -1;
    }

    int faceRect1[4], faceRect2[4], featSize1 = 0, featSize2 = 0;
    float feature1[512], feature2[512];
    
    ret = fmr_extract_feature(image1.data, image1.cols, image1.rows, faceRect1, (unsigned char*)feature1, &featSize1);
    if(ret == -1) {
        printf("license error!\n");
		return -1;
    } else if(ret == -2) {
        printf("init error!\n");
		return -1;
    } else if(ret == 0) {
        printf("image1: no face detected!\n");
		return -1;
    } else if(ret == 1) {
        printf("image1: feature extracted!\n");
    }

    ret = fmr_extract_feature(image2.data, image2.cols, image2.rows, faceRect1, (unsigned char*)feature2, &featSize2);
    if(ret == -1) {
        printf("license error!\n");
		return -1;
    } else if(ret == -2) {
        printf("init error!\n");
		return -1;
    } else if(ret == 0) {
        printf("image2: no face detected!\n");
		return -1;
    } else if(ret == 1) {
        printf("image2: feature extracted!\n");
    }

    double similairity = fmr_compare_feature((unsigned char*)feature1, (unsigned char*)feature2);
	if(similairity > SIMILARITY_THRESHOLD) {
		printf("same person!, similarity = %f\n", similairity);
	} else {
		printf("different person!, similarity = %f\n", similairity);
	}

    return 0;
}

void printUsage(const std::string& message)
{
	if (!message.empty()) {
		printf("%s", message.c_str());
	}

	printf(
		"\n********************************************************************************\n"
		"example_recognition\n"
		"\t--image1 <path-to-image> \n"
		"\t--image2 <path-to-image> \n"
		"\t--model <path-to-model-folder> \n"
		"\n"
		"--image1: Path to an image(JPEG/PNG/BMP).\n\n"
		"--image2: Path to an image(JPEG/PNG/BMP).\n\n"
		"--model: Path to the folder containing models.\n\n"
        "./example_recognition --image1 ../../test_image/Carlos_Menem_0018.jpg --image2 ../../test_image/Carlos_Menem_0020.jpg --model ../../model\n"
		"********************************************************************************\n"
	);
}

bool parseArgs(int argc, char *argv[], std::map<std::string, std::string >& values)
{
	assert(argc > 0 && argv != nullptr);

	values.clear();

	// Make sure the number of arguments is even
	if ((argc - 1) & 1) {
		printf("Number of args must be even");
		return false;
	}

	// Parsing
	for (int index = 1; index < argc; index += 2) {
		std::string key = argv[index];
		if (key.size() < 2 || key[0] != '-' || key[1] != '-') {
			printf("Invalid key: %s", key.c_str());
			return false;
		}
		values[key] = argv[index + 1];
	}

	return true;
}