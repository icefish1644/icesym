#!/bin/bash

cd $HOME
rm -R icesym
# Get necesary files from github repo.
git clone https://github.com/manu080797/icesym.git

# Fix bug when compiling wxpython that cannot find gst1.0 headers.
#export GST_CFLAGS="$(pkg-config gstreamer-1.0 --cflags)"
#export GST_LIBS="$(pkg-config gstreamer-1.0 --libs)"

# Compile wxpthon from source and update cygwin's version.
#pip2.7 install --upgrade wxpython

# Compile ICESYM-1D and install generated Dll to site-packages.
cd $HOME/icesym/ICESYM-1D/src
CFLAGS="-fpermissive" make
make install

# Run ICESYM-GUI
#cd $HOME/icesym/ICESYM-GUI/
#DISPLAY=:0 python2.7 SimulatorGUI.py

pause
