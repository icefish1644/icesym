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

echo ""
echo "ICEsym se ha instalado correctamente."
echo "Carpeta de instalacion: "
echo "     $HOME/icesym/ICESYM-1D/src"
echo ""
echo "Estos son los archivos en la carpeta de icesym:"
ls
echo ""
echo ""
echo "Para ejecutar el programa, modifique el archivo exec.py para que"
echo "apunte al archivo deseado con los parametros."
echo "Puede realizar esta tarea ejecutando:"
echo "      nano exec.py"
echo "Luego ejecute:"
echo "      python exec.py"
echo ""
echo ""
echo "Para volver a ejecutar icesym luego de cerrar esta ventana:"
echo " 1- Abra Cygwin64 Terminal."
echo " 2- Cambie al directorio donde se encuentra icesym:"
echo "      cd $HOME/icesym/ICESYM-1D/src"
echo " 3- Ejecute el programa: "
echo "      python exec.py"
echo ""
echo ""
echo "Puede acceder a los archivos de icesym desde el explorador de Windows"
echo "en la siguiente ruta (Cambie '/' por '\'): "
echo " C:\cygwin64$HOME/icesym/ICESYM-1D/src"


bash
