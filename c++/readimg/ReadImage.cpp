#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <stdio.h>
#include <iostream>

#include <opencv2/opencv.hpp> 
using namespace cv;
 
int main( int argc, char* argv[] )
{
 std::cout << argc << std::endl;
 std::cout << argv[0] << std::endl;
 std::cout << argv[1] << std::endl;
// std::cout << argv[2] << std::endl;
 //char* type = argv[2];
 char* imageName = argv[1];
 //int type = (int) *argv[2]; 
 //std::cout << imageName << std::endl;
 //int x = (int)*type - 48;
 //std::cout << "-----"<< argc << std::endl;
 //std::cout << sizeof(imageName)<< std::endl;

 //std::cout << x << std::endl;

 Mat image;
 image = imread( imageName, 1 );
 
 if( argc != 2 || !image.data )
 {
   printf( " No image data n " );
   return -1;
 }
 std::cout << image.channels() << std::endl;
  std::cout << sizeof(image.col(0)) << std::endl; 

 namedWindow( imageName, CV_WINDOW_AUTOSIZE );
 imshow( imageName, image );
 waitKey(0);
 return 0;
}
