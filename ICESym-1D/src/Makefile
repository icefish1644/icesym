.PHONY: default src build install clean

default: build

src: simCythonCPP.cpp

simCythonCPP.cpp: simCythonCPP.pyx $(wildcard *.pyx)
	cython --cplus --working . -I. $<

build: src
	python2.7 setup.py build

install: build
	python2.7 setup.py install

install_gdb: build
	python2.7 setup_gdb.py install

install_home: build
	python2.7 setup.py install --home=${HOME}

clean:
	python2.7 setup.py clean --all
	${RM} simCythonCPP.cpp *.pyc *~
