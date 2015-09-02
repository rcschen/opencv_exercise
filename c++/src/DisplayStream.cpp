#include <stdio.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;

int main(int argc, char** argv)
{ 
  VideoCapture cap;
  Mat src;
  std::cout << cap.open("http://192.168.1.232:8080/?action=stream?dummy=param.mjpg") << std::endl;
  std::cout << "test" << std::endl;
  while (1)
  {
 
                cap >> src;
                // your code here
                /// Show your results
                namedWindow("Cam", CV_WINDOW_AUTOSIZE);
                std::cout << "test:"<<CV_WINDOW_AUTOSIZE << std::endl;

                imshow("Cam", src);
                if (waitKey(2) == 27)
                        break;
                 // Press "Esc" to exit
  } 
  return 0;
}
