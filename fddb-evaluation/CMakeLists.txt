project(fddb-eval)
cmake_minimum_required(VERSION 2.8)

find_package(OpenCV REQUIRED)

file(GLOB SRC *.cpp)
add_executable(fddbEval ${SRC})

target_link_libraries(fddbEval ${OpenCV_LIBS})