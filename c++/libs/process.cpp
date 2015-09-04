#include "process.hpp"

using namespace std;

void canny_edge(Mat *src, Mat *targ, double threshold1, double threshold2, int apertureSize, bool L2gradient)
{ Mat imageGray;
  cout<< "test << endl";
  cvtColor(*src, imageGray, CV_RGB2GRAY);
  Canny(imageGray, *targ, threshold1, threshold2, apertureSize, L2gradient);
}
