cmake_minimum_required(VERSION 3.17)
project(ExtremalP5)

set(EIGEN_DIR "C:/Users/shiva/Desktop/CS Projects/extlib/eigen-3.3.9")
include_directories(${EIGEN_DIR})

set(CMAKE_CXX_STANDARD 17)

add_executable(ExtremalP5 main.cpp)