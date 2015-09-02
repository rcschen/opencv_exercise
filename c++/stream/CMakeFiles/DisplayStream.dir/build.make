# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/cschen/opencv_exercise/c++/stream

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/cschen/opencv_exercise/c++/stream

# Include any dependencies generated for this target.
include CMakeFiles/DisplayStream.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/DisplayStream.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/DisplayStream.dir/flags.make

CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o: CMakeFiles/DisplayStream.dir/flags.make
CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o: DisplayStream.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/cschen/opencv_exercise/c++/stream/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o -c /home/cschen/opencv_exercise/c++/stream/DisplayStream.cpp

CMakeFiles/DisplayStream.dir/DisplayStream.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/DisplayStream.dir/DisplayStream.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/cschen/opencv_exercise/c++/stream/DisplayStream.cpp > CMakeFiles/DisplayStream.dir/DisplayStream.cpp.i

CMakeFiles/DisplayStream.dir/DisplayStream.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/DisplayStream.dir/DisplayStream.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/cschen/opencv_exercise/c++/stream/DisplayStream.cpp -o CMakeFiles/DisplayStream.dir/DisplayStream.cpp.s

CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o.requires:
.PHONY : CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o.requires

CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o.provides: CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o.requires
	$(MAKE) -f CMakeFiles/DisplayStream.dir/build.make CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o.provides.build
.PHONY : CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o.provides

CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o.provides.build: CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o

# Object files for target DisplayStream
DisplayStream_OBJECTS = \
"CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o"

# External object files for target DisplayStream
DisplayStream_EXTERNAL_OBJECTS =

DisplayStream: CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o
DisplayStream: CMakeFiles/DisplayStream.dir/build.make
DisplayStream: /usr/local/lib/libopencv_videostab.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_video.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_ts.a
DisplayStream: /usr/local/lib/libopencv_superres.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_stitching.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_photo.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_ocl.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_objdetect.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_nonfree.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_ml.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_legacy.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_imgproc.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_highgui.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_gpu.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_flann.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_features2d.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_core.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_contrib.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_calib3d.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_nonfree.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_ocl.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_gpu.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_photo.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_objdetect.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_legacy.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_video.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_ml.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_calib3d.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_features2d.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_highgui.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_imgproc.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_flann.so.2.4.10
DisplayStream: /usr/local/lib/libopencv_core.so.2.4.10
DisplayStream: CMakeFiles/DisplayStream.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable DisplayStream"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/DisplayStream.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/DisplayStream.dir/build: DisplayStream
.PHONY : CMakeFiles/DisplayStream.dir/build

CMakeFiles/DisplayStream.dir/requires: CMakeFiles/DisplayStream.dir/DisplayStream.cpp.o.requires
.PHONY : CMakeFiles/DisplayStream.dir/requires

CMakeFiles/DisplayStream.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/DisplayStream.dir/cmake_clean.cmake
.PHONY : CMakeFiles/DisplayStream.dir/clean

CMakeFiles/DisplayStream.dir/depend:
	cd /home/cschen/opencv_exercise/c++/stream && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/cschen/opencv_exercise/c++/stream /home/cschen/opencv_exercise/c++/stream /home/cschen/opencv_exercise/c++/stream /home/cschen/opencv_exercise/c++/stream /home/cschen/opencv_exercise/c++/stream/CMakeFiles/DisplayStream.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/DisplayStream.dir/depend

