cmake_minimum_required(VERSION 2.8)
project( Practice )
find_package( OpenCV REQUIRED )
set(LOCAL_INCLUDE include)
set(SRC_DIR src)
set(LIB_DIR libs)
message(${OpenCV_LIBS} )
include_directories(${LOCAL_INCLUDE})
add_subdirectory(${SRC_DIR})
add_subdirectory(${LIB_DIR})



