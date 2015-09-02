#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <util.hpp>

using namespace cv;
using namespace std;
int main(int argc, char **argv)
{
   char* imageName = argv[1];
   Mat imgOrg;
   Mat imgGray;
   imgOrg = imread(imageName, 1);
   if( argc != 2 || ! imgOrg.data )
   {
      printf( " No image data n " );
      return -1;
   }
   showimg(imgOrg);
  
   cvtColor( imgOrg, imgGray, CV_RGB2GRAY );
   showimg(imgGray);
}

