# coding= utf-8
from numpy import array
import time
import sys
import os
from simCythonCPP import Simulator

sys.path.append("/icesym/ICESym-GUI/saves")
os.system("rm /icesym/ICESym-GUI/saves*.pyc ")
os.system("rm cyl_debug.csv ")
os.system("rm tube_debug.csv ")
os.system("rm convergence_debug.csv ")
data = __import__("multicyl4TSI")
now = time.time()
Sim = Simulator(**data.kargs)
print "termina de inicializar"
Sim.printData()

Sim.solver()

now2 = time.time()
print now2-now
