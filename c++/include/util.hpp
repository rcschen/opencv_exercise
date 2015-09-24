#include <opencv2/opencv.hpp>
#include <stdio.h>

int showimg(cv::Mat image, char *frameName = "test");
void readimg(char *fileName, int mode, cv::Mat *img);
void cvtColorDiy(cv::Mat *org, cv::Mat *targ);
