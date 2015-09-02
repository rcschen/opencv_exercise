cmake_minimum_required(VERSION 2.8)
project( Mattest )
find_package( OpenCV REQUIRED )
add_executable( Mattest Mattest.cpp )
target_link_libraries( Mattest ${OpenCV_LIBS} )

