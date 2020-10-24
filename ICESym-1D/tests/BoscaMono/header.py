rpms = [8000]

final_times = [0.09]

nstroke = 4
ncycles = 6
rho = 1.1647
Globals = dict()
Globals['engine_data'] = 1
Tubes = []
Tube0 = dict()
Tube0['label'] = 'TUBO0'
Tube0['nnod'] = 29
Tube0['ndof'] = 3
Tube0['histo'] = [0, 28]
Tubes.append(Tube0)

Tube1 = dict()
Tube1['label'] = 'TUBO1'
Tube1['nnod'] = 53
Tube1['ndof'] = 3
Tube1['histo'] = [0, 52]
Tubes.append(Tube1)

Tube2 = dict()
Tube2['label'] = 'TUBO2'
Tube2['nnod'] = 77
Tube2['ndof'] = 3
Tube2['histo'] = [0, 76]
Tubes.append(Tube2)

Tube3 = dict()
Tube3['label'] = 'TUBO3'
Tube3['nnod'] = 185
Tube3['ndof'] = 3
Tube3['histo'] = [0, 184]
Tubes.append(Tube3)

Tube4 = dict()
Tube4['label'] = 'TUBO4'
Tube4['nnod'] = 101
Tube4['ndof'] = 3
Tube4['histo'] = [0, 100]
Tubes.append(Tube4)

Tanks = []
Tank0 = dict()
Tank0['label'] = 'TANQUE0'
Tank0['nnod'] = 3
Tank0['ndof'] = 3
Tank0['extras'] = 0
Tank0['histo'] = [0, 1, 2]
Tanks.append(Tank0)

Tank1 = dict()
Tank1['label'] = 'TANQUE1'
Tank1['nnod'] = 3
Tank1['ndof'] = 3
Tank1['extras'] = 0
Tank1['histo'] = [0, 1, 2]
Tanks.append(Tank1)

Tank2 = dict()
Tank2['label'] = 'TANQUE2'
Tank2['nnod'] = 3
Tank2['ndof'] = 3
Tank2['extras'] = 0
Tank2['histo'] = [0, 1, 2]
Tanks.append(Tank2)

Junctions = []
Cylinders = []
Cylinder0 = dict()
Cylinder0['label'] = 'CILINDRO0'
Cylinder0['ndof'] = 3
Cylinder0['nvi'] = 1
Cylinder0['nve'] = 1
Cylinder0['extras'] = 1
Cylinder0['Q_fuel'] = 4.6e+07
Cylinder0['crank_radius'] = 0.044
Cylinder0['histo'] = [0, 1, 2]
Cylinder0['angleClose'] = 283
Cylinders.append(Cylinder0)

