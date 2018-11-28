#### ---- ####
# Archivo generado por SimulatorGUI
# CIMEC - Santa Fe - Argentina 
# Adecuado para levantar desde Interfaz Grafica 
# O para correr desde consola mediante $python main.py 
#### ---- ####


#--------- Inicializacion de Simulator

Simulator0 = dict()
Simulator0['dtheta_rpm'] = 1.0
Simulator0['calc_engine_data'] = 1
Simulator0['Courant'] = 0.8
Simulator0['heat_flow'] = 1.0
Simulator0['R_gas'] = 287.0
Simulator0['rpms'] = [1000, 2000, 3000, 4000, 5000, 6000]
Simulator0['filesave_state'] = 'monocyl4TSI'
Simulator0['ncycles'] = 5
Simulator0['folder_name'] = 'monocyl4TSI'
Simulator0['ga'] = 1.3
Simulator0['viscous_flow'] = 1.0
Simulator0['nsave'] = 5
Simulator0['ig_order'] = [0]
Simulator0['get_state'] = 2
Simulator0['nappend'] = 5.0
Simulator0['engine_type'] = 0
Simulator0['nstroke'] = 4
Simulator0['nzones'] = 1

Simulator = Simulator0


#--------- FIN Inicializacion de Simulator


#--------- Inicializacion de Cylinders

Cylinders = []

Cylinders0 = dict()
Cylinders0['crank_radius'] = 0.05
Cylinders0['type_ig'] = 0
Cylinders0['ndof'] = 3
Cylinders0['full_implicit'] = 0.0
Cylinders0['model_ht'] = 1
Cylinders0['factor_ht'] = 1.0
Cylinders0['piston_area'] = 0.0050265
Cylinders0['ownState'] = 1
Cylinders0['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Cylinders0['nnod'] = 3
Cylinders0['label'] = 'cyl'
Cylinders0['twall'] = [450.0]
Cylinders0['state_ini'] = [[1.1769, 101330.0, 300.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Cylinders0['nve'] = 1
Cylinders0['head_chamber_area'] = 0.0078191
Cylinders0['type_temperature'] = 0
Cylinders0['rod_length'] = 0.125
Cylinders0['species_model'] = 0
Cylinders0['nvi'] = 1
Cylinders0['delta_ca'] = 0.0
Cylinders0['extras'] = 1
Cylinders0['histo'] = [0]
Cylinders0['Vol_clearance'] = 5.58505360638e-05
Cylinders0['Bore'] = 0.08
Cylinders0['scavenge'] = 0.0


#--------- Inicializacion de fuel

fuel0 = dict()
fuel0['y'] = 2.25
fuel0['hvap_fuel'] = 350000.0
fuel0['Q_fuel'] = 44300000.0

Cylinders0['fuel'] = fuel0


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de combustion

combustion0 = dict()
combustion0['phi'] = 0.265
combustion0['a_wiebe'] = 5.0
combustion0['dtheta_comb'] = 1.0471975512
combustion0['combustion_model'] = 1
combustion0['m_wiebe'] = 1.64
combustion0['theta_ig_0'] = 5.8643062867

Cylinders0['combustion'] = combustion0


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de injection

injection0 = dict()

Cylinders0['injection'] = injection0


#--------- FIN Inicializacion de injection

Cylinders0['position'] = (328,194)
Cylinders0['exhaust_valves'] = []
Cylinders0['intake_valves'] = []

Cylinders.append(Cylinders0)


#--------- FIN Inicializacion de Cylinders


#--------- Inicializacion de Valves

Valves = []

Valves0 = dict()
Valves0['angle_VC'] = 3.83972435439
Valves0['Lvmax'] = 0.009
Valves0['label'] = 'ivalve'
Valves0['histo'] = 0
Valves0['Nval'] = 1
Valves0['Dv'] = 0.035
Valves0['type_dat'] = 0
Valves0['Cd'] = [[0.0, 0.8], [0.009, 0.8]]
Valves0['type'] = 0
Valves0['angle_V0'] = 12.3918376892
Valves0['valve_model'] = 1
Valves0['position'] = (289,193)
Valves0['tube'] = 0
Valves0['ncyl'] = 0
Valves0['typeVal'] = 'int'
Cylinders0['intake_valves'].append(Valves0)
Valves.append(Valves0)

Valves1 = dict()
Valves1['angle_VC'] = 0.349065850399
Valves1['Lvmax'] = 0.009
Valves1['label'] = 'evalve'
Valves1['histo'] = 0
Valves1['Nval'] = 1
Valves1['Dv'] = 0.035
Valves1['type_dat'] = 0
Valves1['Cd'] = [[0.0, 0.75], [0.009, 0.75]]
Valves1['type'] = 1
Valves1['angle_V0'] = 8.55211333477
Valves1['valve_model'] = 1
Valves1['position'] = (361,193)
Valves1['tube'] = 1
Valves1['ncyl'] = 0
Valves1['typeVal'] = 'exh'
Cylinders0['exhaust_valves'].append(Valves1)
Valves.append(Valves1)


#--------- FIN Inicializacion de Valves


#--------- Inicializacion de Tubes

Tubes = []

Tubes0 = dict()
Tubes0['diameter'] = [0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045]
Tubes0['numNorm'] = 3
Tubes0['nnod'] = 81
Tubes0['twall'] = [300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0]
Tubes0['ndof'] = 3
Tubes0['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes0['label'] = 'tube0'
Tubes0['histo'] = [0, 40, 80]
Tubes0['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4]
Tubes0['posNorm'] = [0.0, 0.5, 1.0]
Tubes0['longitud'] = 0.4
Tubes0['typeSave'] = 1
Tubes0['position'] = (231,201)
Tubes0['nleft'] = 0
Tubes0['tleft'] = 'atmosphere'
Tubes0['nright'] = 0
Tubes0['tright'] = 'cylinder'

Tubes.append(Tubes0)

Tubes1 = dict()
Tubes1['diameter'] = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
Tubes1['numNorm'] = 3
Tubes1['nnod'] = 101
Tubes1['twall'] = [450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0, 450.0]
Tubes1['ndof'] = 3
Tubes1['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes1['label'] = 'tube1'
Tubes1['histo'] = [0, 50, 100]
Tubes1['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495, 0.5]
Tubes1['posNorm'] = [0.0, 0.5, 1.0]
Tubes1['longitud'] = 0.5
Tubes1['typeSave'] = 1
Tubes1['position'] = (424,193)
Tubes1['nleft'] = 0
Tubes1['tleft'] = 'cylinder'
Tubes1['nright'] = 1
Tubes1['tright'] = 'atmosphere'

Tubes.append(Tubes1)


#--------- FIN Inicializacion de Tubes


#--------- Inicializacion de Tanks

Tanks = []


#--------- FIN Inicializacion de Tanks


#--------- Inicializacion de Junctions

Junctions = []


#--------- FIN Inicializacion de Junctions


#--------- Inicializacion de Atmospheres

Atmospheres = []

Atmospheres0 = dict()
Atmospheres0['nnod'] = 1
Atmospheres0['ndof'] = 3
Atmospheres0['state_ini'] = [1.1769, 1.0, 101330.0]
Atmospheres0['position'] = (160,196)

Atmospheres.append(Atmospheres0)

Atmospheres1 = dict()
Atmospheres1['nnod'] = 1
Atmospheres1['ndof'] = 3
Atmospheres1['state_ini'] = [1.1769, 1.0, 101330.0]
Atmospheres1['position'] = (474,190)

Atmospheres.append(Atmospheres1)


#--------- FIN Inicializacion de Atmospheres



kargs = {'Simulator':Simulator, 'Cylinders':Cylinders, 'Junctions':Junctions, 'Tubes':Tubes, 'Tanks':Tanks, 'Atmospheres':Atmospheres}
