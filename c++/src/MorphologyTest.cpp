#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <util.hpp>
#include <process.hpp>
using namespace cv;
using namespace std;

int main(int argc, char **argv)
{
  char *fileName = argv[1];
  Mat imgOrg;
  readimg(fileName, 1, &imgOrg);
  Mat imgErode;
  Mat imgDilate;
  Mat imgOpening;
  Mat imgClosing;
  Mat imgMpGradient;
  Mat imgTopHat;
  Mat imgBlackHat;
  showimg(imgOrg,"org");

  doErode(&imgOrg, &imgErode);
  showimg(imgErode, "erode");

  doDilate(&imgOrg, &imgDilate);
  showimg(imgDilate, "dliage");

  doDilate(&imgErode, &imgOpening);
  showimg(imgOpening, "opening");

  doErode(&imgDilate, &imgClosing);
  showimg(imgClosing, "closing");

  imgMpGradient = imgDilate - imgErode;
  showimg(imgMpGradient,"Mpgradient");
 
  imgTopHat = imgOrg - imgOpening;
  showimg(imgTopHat,"top hat");
 
  imgBlackHat = imgClosing - imgOrg;
  showimg(imgBlackHat,"black hat");
 
}
