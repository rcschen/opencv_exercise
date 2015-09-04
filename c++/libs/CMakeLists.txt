add_library( util util.cpp )
target_link_libraries( util  ${OpenCV_LIBS}  )
add_library( process process.cpp )
target_link_libraries( process  ${OpenCV_LIBS}  )

