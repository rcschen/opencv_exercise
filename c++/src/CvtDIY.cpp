#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <util.hpp>

using namespace cv;
using namespace std;

Mat myCvtColor(Mat orgImg, Mat targetImg)
{  for(int i = 0; i < orgImg.rows; i++)
     for(int j = 0; j<orgImg.cols; j++)
   {
     targetImg.at<Vec3b>(i,j)[0] = 0.299*orgImg.at<Vec3b>(i,j)[2] + 0.587*orgImg.at<Vec3b>(i,j)[1] + 0.144*orgImg.at<Vec3b>(i,j)[0];
     targetImg.at<Vec3b>(i,j)[1] = ((orgImg.at<Vec3b>(i,j)[2]*(-38) - orgImg.at<Vec3b>(i,j)[1]*74  + orgImg.at<Vec3b>(i,j)[0]*112) + 128)/256 + 128;
     targetImg.at<Vec3b>(i,j)[2] = ((orgImg.at<Vec3b>(i,j)[2]*112 - orgImg.at<Vec3b>(i,j)[1]*94 - orgImg.at<Vec3b>(i,j)[0]*18) + 128)/256 + 128; 
   }
   return targetImg;
}

int main(int argc, char **argv)
{
  char * imageName = argv[1];
  Mat orgImg;
  Mat funcYcbImg;
  orgImg = imread(imageName, 1);
  Mat diyYcbImg = Mat::zeros(orgImg.rows, orgImg.cols, CV_8UC3 );

  if( argc != 2 || ! orgImg.data )
  {
      printf( " No image data n " );
      return -1;
  }
  showimg(orgImg);
  //test what scalar is
  cout << Scalar(256) << endl;   
  for(int i = 0; i < orgImg.rows; i++)
     for(int j = 0; j<orgImg.cols; j++)
     {
        cout<< (int) orgImg.at<Vec3b>(i,j)[0] << " , " ;
        cout<< (int) orgImg.at<Vec3b>(i,j)[1] << " , ";
        cout<< (int) orgImg.at<Vec3b>(i,j)[2] << endl ;

     }
  cvtColor(orgImg,  funcYcbImg, CV_BGR2YCrCb);
  showimg(funcYcbImg);
  showimg(myCvtColor(orgImg,diyYcbImg ));
  showimg(myCvtColor(orgImg,diyYcbImg ));

  return 0;
}


