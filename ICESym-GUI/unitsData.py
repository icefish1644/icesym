import os, sys

possibleUnits = dict()
possibleUnits['density'] = ['kg/m^3']
possibleUnits['pressure'] = ['Pa', 'kPa', 'MPa','Bar','Atm']
possibleUnits['velocity'] = ['m/s']
possibleUnits['temperature'] = ['K',"C"]

possibleUnits['convective heat-transfer coeff'] = ['W/(K.m^2)']
possibleUnits['radiactive heat-transfer coeff'] = ['W/(K.m^2)']
possibleUnits['convective heat-transfer rate'] = ['W','kW']
possibleUnits['radiactive heat-transfer rate'] = ['W','kW']
possibleUnits['burned mass fraction'] = []
possibleUnits['burned mass fraction rate'] = []
possibleUnits['mass flow rate trought intake port'] = ['kg/s','g/s']
possibleUnits['mass flow rate trought exhaust port'] = ['kg/s','g/s']
possibleUnits['Volume'] = ['m^3','cm^3']
possibleUnits['mass of fuel'] = ['kg','g']
possibleUnits['mass of air'] = ['kg','g']
possibleUnits['mass of residual gas'] = ['kg','g']
possibleUnits['total heat-transfer rate'] = ['W','kW']
possibleUnits['fuel chemical energy release'] = ['W','kW']
possibleUnits['power_indicated'] = ['W', 'kW', 'hp', 'cv']
possibleUnits['power_effective'] = ['W', 'kW', 'hp', 'cv']
possibleUnits['torque'] = ['N.m','kgf']
possibleUnits['torque_indicated'] = ['N.m','kgf']
possibleUnits['torque_effective'] = ['N.m','kgf']
possibleUnits['IMEP_per_cylinder'] = ['Pa', 'kPa', 'MPa','Bar','Atm']
possibleUnits['IMEP_global'] = ['Pa', 'kPa', 'MPa','Bar','Atm']
possibleUnits['FMEP_per_cylinder'] = ['Pa', 'kPa', 'MPa','Bar','Atm']
possibleUnits['FMEP_global'] = ['Pa', 'kPa', 'MPa','Bar','Atm']
possibleUnits['BMEP_per_cylinder'] = ['Pa', 'kPa', 'MPa','Bar','Atm']
possibleUnits['BMEP_global'] = ['Pa', 'kPa', 'MPa','Bar','Atm']
possibleUnits['SFC_indicated'] = ['kg/(W.s)', 'g/(kW.h)','lbm/(hp.h)']
possibleUnits['SFC_effective'] = ['kg/(W.s)', 'g/(kW.h)','lbm/(hp.h)']
possibleUnits['mechanical_efficiency'] = []
possibleUnits['volumetric_efficiency_per_cylinder'] = []
possibleUnits['volumetric_efficiency_global'] = []
possibleUnits['fuel_conversion_efficiency_indicated'] = []
possibleUnits['fuel_conversion_efficiency_effective'] = []

possibleUnits['mass flow rate'] = ['kg/s','g/s']
possibleUnits['enthalpy flow rate'] = []
possibleUnits['mass'] = ['kg','g']

#las conversiones son desde el sistema internacional a la unidad requerida
conversions = dict()
#presion
conversions['Pa'] = 1
conversions['Bar'] = 1e-5
conversions['kPa'] = 1e-3
conversions['MPa'] = 1e-6
conversions['Atm'] = 9.87e-6
#energia
conversions['W'] = 1
conversions['kW'] = 1e-3
conversions['hp'] = 1.34e-3
conversions['cv'] = 1.36e-3
#eficiencia
conversions['kg/(W.s)'] = 1
conversions['g/(kW.h)'] = 1e3*3600.0/1e-3
conversions['lbm/(hp.h)'] = 2.2*3600.0/1.34e-3
#temperatura
conversions['K'] = 1
conversions['C'] = 273.15
# volumen
conversions['m^3'] = 1
conversions['cm^3'] = 1e6
#otras
conversions['kg/m^3'] = 1
conversions['m/s'] = 1
conversions['W/(K.m^2)'] = 1
# caudal masico
conversions['kg/s'] = 1
conversions['g/s'] = 1e3
# masa
conversions['kg'] = 1
conversions['g']  = 1e3
#momento de fuerza
conversions['N.m'] = 1
conversions['kgf'] = 0.1


def conversion(data,units):
	# print "llega aca: ", data, units
	if not(units == ''):
		dataRet = []
		if units in ['C']:
			for i in range(len(data)):
				aux = (data[i][0],data[i][1]-conversions[units])
				dataRet.append(aux)
		else:
			for i in range(len(data)):
				aux = (data[i][0],data[i][1]*conversions[units])
				dataRet.append(aux)
		data = dataRet
	# print "sale aca: ", data
	return data

