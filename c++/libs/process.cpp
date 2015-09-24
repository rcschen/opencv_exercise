#include "process.hpp"
#include "util.hpp"

using namespace std;

void canny_edge(Mat *src, Mat *targ, double threshold1, double threshold2, int apertureSize, bool L2gradient)
{ Mat imageGray;
  cout<< "test << endl";
  cvtColor(*src, imageGray, CV_RGB2GRAY);
  Canny(imageGray, *targ, threshold1, threshold2, apertureSize, L2gradient);
}
int dilation_elem = 2;
int dilation_size = 1;

Mat getElement(int type, int size)
{
  Mat element = getStructuringElement( type, Size( 2*size + 1, 2*size+1 ), Point( size, size ) );
  return element;
}
int getType(int t)
{ 
  if( t == 0 ) 
  {
    return MORPH_RECT; 
  }
  else if( t == 1 ) 
  {  
    return MORPH_CROSS; 
  }
  else if( t == 2 )  
  {
    return MORPH_ELLIPSE; 
  }
  
}
void preCornerDetect_ex(Mat *src, Mat *targ, int ksize, int borderType) 
{
  Mat imageGray;
  cvtColor(*src, imageGray, CV_RGB2GRAY);

  preCornerDetect(imageGray, *targ, ksize, borderType);
  int dilation_type = getType(dilation_elem) ;
   
  Mat element = getElement( dilation_type, dilation_size );
  cout<<"element:"<<element<<endl;
  dilate(*targ, *targ, element );
   
}

void doErode(Mat *src, Mat *trg)
{
   Mat element = getElement( getType(dilation_elem), dilation_size );
   erode(*src, *trg, element);
}

void doDilate(Mat *src, Mat *trg)
{
  Mat element = getElement( getType(dilation_elem), dilation_size );
  dilate(*src, *trg, element);
}
