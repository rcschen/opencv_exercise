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
   Mat imgEdge;
   readimg(fileName, 1, &imgOrg);
   showimg(imgOrg);
   imgEdge = Mat::zeros(imgOrg.rows, imgOrg.cols, CV_8UC3);

   canny_edge(&imgOrg, &imgEdge, 50.0, 100.0, 5, false );
   showimg(imgOrg);
   showimg(imgEdge);
   return 0; 
}
