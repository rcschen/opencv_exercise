#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <util.hpp>

using namespace cv;
using namespace std;
int avg_cb = 75;
int avg_cr = 178;
int skinRange = 40;
void SkinColorDetection(Mat *image);

int main(int argc, char **argv)
{
  char *fileName = argv[1];
  Mat imgOrg;
  readimg(fileName, 1, &imgOrg);
  Mat imgYCbCr = Mat::zeros(imgOrg.rows, imgOrg.cols, CV_8UC3);
  cvtColorDiy(&imgOrg, &imgYCbCr); 
  showimg(imgOrg);
  showimg(imgYCbCr);
  SkinColorDetection(&imgYCbCr);
  showimg(imgYCbCr);

  return 0; 
}
void SkinColorDetection(Mat *image)
{  
   double cb, cr;
   for(int i = 0; i< image->rows; i++)
      for(int j = 0; j< image->cols; j++)
      {   cb = image->at<Vec3b>(i,j)[1];
          cr = image->at<Vec3b>(i,j)[2];
           if((cb > avg_cb-skinRange && cb < avg_cb+skinRange) &&
                  (cr > avg_cr-skinRange && cr < avg_cr+skinRange)) {
              image->at<Vec3b>(i,j)[0] =  255.0;
              image->at<Vec3b>(i,j)[1] =  255.0;
              image->at<Vec3b>(i,j)[2] =  255.0;

           }else {
              image->at<Vec3b>(i,j)[0] =  0.0;
              image->at<Vec3b>(i,j)[1] =  0.0;
              image->at<Vec3b>(i,j)[2] =  0.0;
           }


      }
}
