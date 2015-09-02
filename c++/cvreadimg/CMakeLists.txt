cmake_minimum_required(VERSION 2.8)
project( ReadImgCV )
find_package( OpenCV REQUIRED )
add_executable( ReadImgCV ReadImgCV.cpp )
target_link_libraries( ReadImgCV ${OpenCV_LIBS} )

