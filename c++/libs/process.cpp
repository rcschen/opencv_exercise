#include "process.hpp"
#include "util.hpp"

using namespace std;

void canny_edge(Mat *src, Mat *targ, double threshold1, double threshold2, int apertureSize, bool L2gradient)
{ Mat imageGray;
  cout<< "test << endl";
  cvtColor(*src, imageGray, CV_RGB2GRAY);
  Canny(imageGray, *targ, threshold1, threshold2, apertureSize, L2gradient);
}
int dilation_elem = 0;
int dilation_size = 0;
void preCornerDetect_ex(Mat *src, Mat *targ, int ksize, int borderType) 
{
  Mat imageGray;
  cvtColor(*src, imageGray, CV_RGB2GRAY);

  preCornerDetect(imageGray, *targ, ksize, borderType);
  int dilation_type;
  if( dilation_elem == 0 ){ dilation_type = MORPH_RECT; }
  else if( dilation_elem == 1 ){ dilation_type = MORPH_CROSS; }
  else if( dilation_elem == 2) { dilation_type = MORPH_ELLIPSE; }

  Mat element = getStructuringElement( dilation_type,
                                       Size( 2*dilation_size + 1, 2*dilation_size+1 ),
                                       Point( dilation_size, dilation_size ) );
  dilate(*targ, *targ, element );
   
}
