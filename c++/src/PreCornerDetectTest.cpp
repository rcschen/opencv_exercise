#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <util.hpp>
#include <process.hpp>
using namespace cv;
using namespace std;

int main(int argc, char **argv)
{
   char *fileName = argv[1];
   Mat imgOrg;
   readimg(fileName, 1, &imgOrg);
   Mat imgConer; // = Mat::zeros(imgOrg.rows, imgOrg.cols, CV_32FC3 );

   showimg(imgOrg);
   int ksize =  7; //must odd and less than 31
   preCornerDetect_ex(&imgOrg, &imgConer, ksize);
   showimg(imgConer);
   return 0; 
}
