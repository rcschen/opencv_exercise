//#include "stdafx.h"
#include "cvaux.h"
#include "highgui.h"
int main(int *argc, char **argv)
{
 IplImage *pImg;
 IplImage *pGrayImg;
 IplImage *pCornerImg_32F;
 IplImage *pCornerImg_8U;
 //CvCapture *capture = cvCaptureFromCAM(0);
 bool createMemory = false;
 char * filename = argv[1];
 pImg = cvLoadImage(argv[1]);
 cvShowImage("pImg1", pImg);
 cvWaitKey(0);

  if(!createMemory)
  {
   pGrayImg = cvCreateImage( cvGetSize(pImg),
    pImg->depth, 1);
   pCornerImg_32F = cvCreateImage( cvGetSize(pImg),
    IPL_DEPTH_32F, 1);
   pCornerImg_8U = cvCreateImage( cvGetSize(pImg),
    IPL_DEPTH_8U, 1);
   createMemory = !createMemory;
  }

 cvCvtColor( pImg, pGrayImg, CV_BGR2GRAY);
 cvPreCornerDetect(pGrayImg, pCornerImg_32F, 7);       
        
 cvDilate( pCornerImg_32F, pCornerImg_32F, 0, 1 );
 cvConvertScale( pCornerImg_32F, pCornerImg_8U, 255 );
        
 cvShowImage("Gray", pGrayImg);
 cvWaitKey(0);

 cvShowImage("CornerDetect", pCornerImg_8U);
 cvWaitKey(0);

 cvReleaseImage( &pImg );
 cvReleaseImage( &pGrayImg );
 cvReleaseImage( &pCornerImg_32F );
 cvReleaseImage( &pCornerImg_8U );
 //cvReleaseCapture( &capture );
 return 0;
}
