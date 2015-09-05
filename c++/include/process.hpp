#include <opencv2/opencv.hpp>
#include <stdio.h>

using namespace cv;

void canny_edge(Mat *src, Mat *targ, double threshold1, double threshold2, int apertureSize=3, bool L2gradient=false );

void  preCornerDetect_ex( Mat *src, Mat *targ, int ksize, int borderType=BORDER_DEFAULT);
