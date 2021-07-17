An example cross-platform CMake-based project.

We use lib: SDL2 and OpenGL
===> Appear a spinning 3D logo to a desktop window. You can build it on Windows, MacOS or Linux.

![](https://www.facebook.com/photo/?fbid=346766520193292&set=a.111448607058419)

## Requirements

### Ubuntu

Install the SDL2 headers and libraries.

    sudo apt install libsdl2-dev
    
OpenGL headers and libraries are already present on the system. CMake will find them automatically(c'est jolie ce cmake nn).

A small intro to cmake for beginners: (it's useful !4/10: hé fais gaff les gens de la justice)
--------------------------------------------------------
a tool that helps to build c/c++ projects on about many platforms: cmake project contains CMakeLists.txt = configure & build such project (c'est encore ambigu) !!
OK, **, CMAKE generates build pipeline: in our case(linux): a Makefile

## Build Instructions
* create build dir
* generate makefile with cmake command, you choose build type of course
* execute make after that.