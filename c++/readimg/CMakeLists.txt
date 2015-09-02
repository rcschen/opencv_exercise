cmake_minimum_required(VERSION 2.8)
project( ReadImage )
find_package( OpenCV REQUIRED )
add_executable( ReadImage ReadImage.cpp )
target_link_libraries( ReadImage ${OpenCV_LIBS} )

