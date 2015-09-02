#include <stdio.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>

#include <opencv2/opencv.hpp>

using namespace cv;


int main(){

    CvCapture *camera=cvCaptureFromFile("http://192.168.1.232:8080/?action=stream");
    if (camera==NULL)
        printf("camera is null\n");
    else
        printf("camera is not null");

    cvNamedWindow("img");
    while (cvWaitKey(10)!=atoi("q")){
        double t1=(double)cvGetTickCount();
        IplImage *img=cvQueryFrame(camera);
        double t2=(double)cvGetTickCount();
        printf("time: %gms  fps: %.2g\n",(t2-t1)/(cvGetTickFrequency()*1000.), 1000./((t2-t1)/(cvGetTickFrequency()*1000.)));
        std::cout << img << std::endl;
        cvShowImage("img",0);
        //namedWindow("img",1);

        //imshow("Cam", img);
  
        if (waitKey(2) == 27)
               break;
 
    }
    cvReleaseCapture(&camera);
}
