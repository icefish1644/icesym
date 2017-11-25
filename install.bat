@ECHO OFF
REM -- Automates cygwin installation

SETLOCAL

REM -- Change to the directory of the executing batch file
CD %~dp0

REM -- Configure our paths
SET PWD=%~dp0
SET SITE=http://mirrors.kernel.org/sourceware/cygwin/
SET LOCALDIR=%LOCALAPPDATA%/cygwin64
SET ROOTDIR=C:/cygwin64

REM -- These are the packages we will install (in addition to the default packages)
SET PACKAGES=git,nano,bash-completion
SET PACKAGES=%PACKAGES%,gcc-core,gcc-fortran,gcc-g++,libgfortran3,binutils,make
SET PACKAGES=%PACKAGES%,python2,python2-devel,python2-numpy,python2-cython,python2-pip,python2-wx
REM SET PACKAGES=%PACKAGES%,libgtk3-devel,python2-opengl,libgstreamer1.0-devel,gstreamer1.0,gstreamer1.0-plugins-base,libwebkitgtk3.0-devel,libnotify-devel,libjpeg-devel,libtiff-devel,libSDL-devel,libSDL2-devel,libglut-devel,libSM-devel,libgtk2.0-devel,libwebkitgtk1.0-devel,libgstbad1.0-devel,libgstgl1.0-devel
SET PACKAGES=%PACKAGES%,xorg-server,xinit

REM -- Do it!
ECHO *** INSTALLING PACKAGES
bitsadmin.exe /transfer "Downloading Cygwin installer" https://cygwin.com/setup-x86_64.exe %PWD%setup-x86_64.exe
bitsadmin.exe /transfer "Downloading post-install script" https://raw.githubusercontent.com/manu080797/icesym/master/post-install.sh %PWD%post-install.sh
%PWD%setup-x86_64.exe -q -D -L -g -o -s %SITE% -l "%LOCALDIR%" -R "%ROOTDIR%" -C Base -P %PACKAGES%

REM -- Show what we did
ECHO.
ECHO.
ECHO cygwin installation updated
ECHO  - %PACKAGES%
ECHO.

REM -- Execute post-install script
REM -- WARNING: Do not edit the script with windows text editor. Must be formatted in Unix style.
ECHO.
ECHO.
ECHO running post-install script, SimulatorGUI will be launched automatically
ECHO.

set PATH=C:\cygwin64\bin;%PATH%
chdir C:\cygwin64\bin
bash --login %PWD%post-install.sh

ENDLOCAL

PAUSE
EXIT /B 0