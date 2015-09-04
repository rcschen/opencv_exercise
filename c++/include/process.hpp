#include <opencv2/opencv.hpp>
#include <stdio.h>

using namespace cv;

void canny_edge(Mat *src, Mat *targ, double threshold1, double threshold2, int apertureSize, bool L2gradient );

