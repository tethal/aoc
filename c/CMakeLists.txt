cmake_minimum_required(VERSION 3.22)
project(aoc C CXX)

set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 17)

add_executable(aoc_2024_01
        2024/01.c
        util.c
)
