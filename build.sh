#!/usr/bin/env bash
cd ./ICESym-1D/src/
CFLAGS="-L/usr/local/lib/gcc/7 -o3" make install
echo "Done"
bash