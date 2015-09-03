#include "util.hpp"

using namespace cv;
using namespace std;
int showimg(Mat image)
{  namedWindow( "test", CV_WINDOW_AUTOSIZE );
   imshow("test", image);
   waitKey(0);
   return 0; 
}

void readimg(char *fileName, int mode, Mat *img)
 {  
    Mat tmpimg = imread(fileName, mode);
    *img = tmpimg;
    if(! img->data )
    {
       printf(" No image data ");
    }
}
void cvtColorDiy(Mat *orgImg, Mat *targetImg)
{  for(int i = 0; i < orgImg->rows; i++)
     for(int j = 0; j<orgImg->cols; j++)
   {
     targetImg->at<Vec3b>(i,j)[0] = 0.299*orgImg->at<Vec3b>(i,j)[2] + 0.587*orgImg->at<Vec3b>(i,j)[1] + 0.144*orgImg->at<Vec3b>(i,j)[0];
     targetImg->at<Vec3b>(i,j)[1] = ((orgImg->at<Vec3b>(i,j)[2]*(-38) - orgImg->at<Vec3b>(i,j)[1]*74  + orgImg->at<Vec3b>(i,j)[0]*112) + 128)/256 + 128;
     targetImg->at<Vec3b>(i,j)[2] = ((orgImg->at<Vec3b>(i,j)[2]*112 - orgImg->at<Vec3b>(i,j)[1]*94 - orgImg->at<Vec3b>(i,j)[0]*18) + 128)/256 + 128; 
   }
}
