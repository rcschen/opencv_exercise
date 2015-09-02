//#include "stdafx.h"
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>

using namespace std;

void RGBtoYCbCr(IplImage *);
int main(int argc, char **argv)
{
    char * imageName = argv[1];

    IplImage* pImage = cvLoadImage(imageName);
    CvSize cvSize = cvGetSize(pImage); 
    cout << pImage->depth << endl;
     cout << pImage->nChannels << endl;
  
    IplImage* pImageYCbCr1 = cvCreateImage(cvGetSize(pImage),
        pImage->depth, pImage->nChannels);
    IplImage* pImageYCbCr2 = cvCreateImage(cvGetSize(pImage),
        pImage->depth, pImage->nChannels);

    if(pImage) //§PÂ¼v¹³¬O§_Ū¨ú
    {
        cvCopy(pImage, pImageYCbCr1, NULL);
        //½ƻs¤@¥÷³µ¹pImageYCbCr1

        cvCvtColor( pImage, pImageYCbCr2, CV_BGR2YCrCb );
        //OpenCV API´£¨ѪºRGBÂYCbCrªºÂ´«¨禡
        
        RGBtoYCbCr(pImageYCbCr1);
        //¦ۭqªºRGBÂYCbCrªºÂ´«¨禡

        cvShowImage("RGB", pImage);
        cvWaitKey(0);

        cvShowImage("YCbCr", pImageYCbCr1);
        cvWaitKey(0);

        cvShowImage("YCbCr2", pImageYCbCr2);       
    }
    cvWaitKey(0);
    return 0;
}
void RGBtoYCbCr(IplImage *image)
{
    CvScalar scalarImg;
    double cb, cr, y;
    for(int i=0; i<image->height; i++)
    for(int j=0; j<image->width; j++)
    {
        scalarImg = cvGet2D(image, i, j);
        //±q¼v¹³¤¤¨úÈ        y = 0.299*scalarImg.val[2] + 0.587*scalarImg.val[1] 
            + 0.144*scalarImg.val[0];
        cb = ((scalarImg.val[2]*(-38) - scalarImg.val[1]*74 
            + scalarImg.val[0]*112) + 128)/256 + 128;
        cr = ((scalarImg.val[2]*112 - scalarImg.val[1]*94 
            - scalarImg.val[0]*18) + 128)/256 + 128;
        //RGBÃ¦â¶¡ÂYCbCrÃ¦â¶¡¤½¦¡Â´«
        cvSet2D(image, i, j, cvScalar( y, cr, cb));
    }
}
