project(foobar C)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(BZip2 REQUIRED)

add_executable(${CMAKE_PROJECT_NAME} bzip2.c)
target_link_libraries(${CMAKE_PROJECT_NAME} ${BZIP2_LIBRARIES})

install(TARGETS ${CMAKE_PROJECT_NAME}
        RUNTIME DESTINATION bin)
