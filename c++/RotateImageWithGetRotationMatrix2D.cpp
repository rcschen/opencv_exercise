#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

int showimg(Mat image)
{  namedWindow( "test", CV_WINDOW_AUTOSIZE );
   imshow("test", image);
   waitKey(0);
   return 0; 
}

int main(int argc, char **argv)
{
   char* imageName = argv[1];
   float angle = 90.0F;
   Mat imgOrg;
   imgOrg = imread(imageName, 1);
   if( argc != 2 || ! imgOrg.data )
   {
      printf( " No image data n " );
      return -1;
   }
   showimg(imgOrg);
   cout << imgOrg.type() << endl;
   Mat imgRes = Mat::zeros( imgOrg.rows, imgOrg.cols, imgOrg.type());
   //cout << imgRes << endl;
   Point2f org_center(imgOrg.cols/2.0F, imgOrg.rows/2.0F);
   Mat rotateM = getRotationMatrix2D(org_center, angle, 1.0);
   warpAffine(imgOrg, imgRes, rotateM, imgOrg.size());
   showimg(imgRes);
}
