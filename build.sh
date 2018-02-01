#!/usr/bin/env bash
cd ./ICESym-1D/src/
CFLAGS="-L/usr/local/lib/gcc/7﻿-pthread -DNDEBUG -g -fwrapv -O2 -Wall -fno-strict-aliasing -Wdate-time -D_FORTIFY_SOURCE=2 -g -fstack-protector-strong -Wformat -Werror=format-security -fPIC" CC="gcc-7" CXX="g++-7" make -B install
echo "Done building"