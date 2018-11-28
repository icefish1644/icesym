#!/usr/bin/env bash
cd ./ICESym-1D/src/
rm simCythonCPP.cpp
sudo CFLAGS="-L/usr/local/Cellar/gcc/8.2.0/lib/gcc/8/gcc/x86_64-apple-darwin18.0.0/8.2.0/../../../ -lgfortran -pthread -g -O2 -Wall" CC="clang" CXX="clang" F90="gfortran" make -B install
echo "Done building"