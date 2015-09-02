#include <opencv2/opencv.hpp> 
using namespace cv;

int main(int argc, char* argv[]){
   char* imgname = argv[1];
   IplImage * img=cvLoadImage(imgname);
   cvNamedWindow("a");
   cvShowImage("a", img);
   cvWaitKey(0);
   return 0;
}
