#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main(int argc, char** argv )
{
   Mat image;
   image = imread(argv[1],1);
   cout << image << endl;
   IplImage *impimg = cvLoadImage(argv[1],1);
   cout <<" =====" << endl;

   cout << *impimg << endl;

}
