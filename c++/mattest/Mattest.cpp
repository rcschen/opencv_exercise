//#include <opencv2/core/core.hpp>
//#include <opencv2/highgui/highgui.hpp>

#include <opencv2/opencv.hpp>
using namespace cv;
void showImg(Mat img)
{
  imshow("img",img);
  waitKey(0);

}
int main(int argc, char** argv)
{
  Mat image32f(2, 3, CV_32F, Scalar(3));
  std::cout<< "CV_32F"<<image32f << std::endl;
  Mat image8uc3(2, 3, CV_8UC3, Scalar(3));
  std::cout<< "CV_8UC3:"<< image8uc3 << std::endl;
  Mat image32fc4(2, 3, CV_32FC4, Scalar(3));
  std::cout<< "CV_32fC4:"<< image32fc4 << std::endl;
  Mat image3332fc5 = Mat::ones(3, 3, CV_32FC2)*5;
  std::cout<< "CV_3332f5:"<< image3332fc5 << std::endl;
  Mat image3332fcp5 = Mat::ones(3, 3, CV_32FC2)+5;
  std::cout<< "CV_3332f5:"<< image3332fcp5 << std::endl;
  float B22data[] = { 5, -15, 20, -15};
  Mat B2216u = Mat(2, 2, CV_16U, B22data);
  Mat B2232f = Mat(2, 2, CV_32F, B22data);
  std::cout<< "b2216u:"<< B2216u << std::endl;
  std::cout<< "b2232f:"<< B2232f << std::endl;

  Mat vec01 = Mat::zeros(2, 2, CV_8U); 
  randu(vec01, Scalar(0), Scalar(256));
  std::cout<< "vec01:"<< vec01 << std::endl;
  showImg(vec01);
  Mat vec01c3 = Mat::zeros(2, 2, CV_8UC3); 
  randu(vec01c3, Scalar(0), Scalar(256));
  std::cout<< "vec01c3:"<< vec01c3 << std::endl;
  showImg(vec01c3);
  Mat vec01c4 = Mat::zeros(2, 2, CV_8UC4); 
  randu(vec01c4, Scalar(0), Scalar(256));
  std::cout<< "vec01c4:"<< vec01c4 << std::endl;
  showImg(vec01c4);
  Mat vec01c5 = Mat::zeros(2, 2, CV_8UC(5)); 
  randu(vec01c5, Scalar(0), Scalar(256));
  //std::cout<< "vec01c5:"<< vec01c5 << std::endl;
  //showImg(vec01c5);

  cv::Mat gauss = cv::Mat::zeros(100, 100, CV_8U); 
  cv::randn(gauss, cv::Scalar(128), cv::Scalar(10));
  //showImg(gauss);
  cv::Mat gaussc3 = cv::Mat::zeros(100, 100, CV_8UC3); 
  cv::randn(gaussc3, cv::Scalar(128), cv::Scalar(10));
  //showImg(gaussc3);

}
