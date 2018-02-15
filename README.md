# icesym
Fork of icesym \
Added two heat transfer models: non-homogeneous cylinder wall temperature and radial heat transfer in tube. \
Modified to run in macos Sierra and Windows 10 (Cygwin). \
Added convergence check. 

# Dependencies:
python 2.7 (with development headers) \
numpy \
cython \
gfortran \
g++ \
autotools \
wxwidgets for python 2.7 (only for GUI) (>= 4.0)

# Install on linux:
install dependencies \
clone git repo \
open terminal in repo's root directory \
run build.sh script

# Install on Ubuntu:
sudo apt-get update \
sudo apt-get install python2.7 python2.7-dev python-numpy gfortran build-essential cython git nano \
git clone https://github.com/manu080797/icesym \
cd icesym/ICESym-1D/src \
rm simCythonCPP.cpp \ 
sudo make install -B \
nano exec.py (modify accordingly to your model's path) \
python2.7 exec.py

# Install on Fedora:
sudo dnf update
sudo dnf install python2 python2-devel gcc gcc-c++ gcc-gfortran python2-Cython numpy make binutils git nano \
git clone https://github.com/manu080797/icesym \
cd icesym/ICESym-1D/src \
rm simCythonCPP.cpp \ 
sudo make install -B \
nano exec.py (modify accordingly to your model's path) \
python2.7 exec.py

# Install on macos:
install dependencies using brew \
follow same steps as linux \
(might be necessary to specify gfortran path in CFLAGS)

# Install on windows (cygwin):
Download batch file from https://raw.githubusercontent.com/manu080797/icesym/master/install.bat \
Run with administrative rigths and will install everything automatically (Currently no GUI. 

# Running icesym GUI:
Run GUI from icesym/icesym-GUI folder with the next command: "python2.7 SimulatorGUI.py" 

# Running from model file:
Modify exec.py file in icesym-1D/src folder to point to model's folder path and modify import statement to your model's name. \
Run "python2.7 exec.py" in icesym-1D/src to execute icesym.

# Credits
Author: Manuel Lima   \
Original Authors: Juan Marcelo Gimenez, Ezequiel Jose Lopez & Norberto Marcelo Nigro 
