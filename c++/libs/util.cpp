#include "util.hpp"

using namespace cv;
int showimg(Mat image)
{  namedWindow( "test", CV_WINDOW_AUTOSIZE );
   imshow("test", image);
   waitKey(0);
   return 0; 
}
