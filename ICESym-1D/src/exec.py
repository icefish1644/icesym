# coding= utf-8
from numpy import array
import time
import sys
import os
from simCythonCPP import Simulator

sys.path.append("/Users/manu/Documents/Ingeniería/Proyecto investigación/icesym/ICESym-GUI/saves")
data = __import__("QUB400")
now = time.time()
Sim = Simulator(**data.kargs)
print "termina de inicializar"
Sim.printData()
Sim.solver()
now2 = time.time()
print now2-now
