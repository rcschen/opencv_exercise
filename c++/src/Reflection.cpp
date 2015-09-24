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
   Mat imgReflect;
   readimg(fileName, 1, &imgOrg);
   showimg(imgOrg);
   imgReflect = Mat::zeros(imgOrg.rows, imgOrg.cols, CV_8UC3);

   //canny_edge(&imgOrg, &imgEdge, 50.0, 100.0, 5, false );
   for(int i = 0; i < imgOrg.rows; i++)
     for(int j = 0; j< imgOrg.cols; j++)
   {
        imgReflect.at<Vec3b>(i,j) = imgOrg.at<Vec3b>(i,(imgOrg.cols-1-j));
   }
   showimg( imgReflect);

}
