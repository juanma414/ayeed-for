#Para 1000 usuarios residenciales de energía eléctrica se cuenta con pares de valores
#que indican, para cada medidor, el consumo de Kilowatios al final del mes anterior y el
#consumo de Kilowatios al final del mes actual. Además se tiene el precio por Kilowatio.
#Exhibir, para cada usuario, el precio del Kilowatio, el consumo del mes y el importe a
#abonar.
precioKw = float(input("ingrese el precio del Kw"))
for user in range(1000):
	consMesAnterior = float(input("ingrese el consumo del mes anterior"))
	conMesEnCurso = float(input("ingrese el consumo del mes en curso"))
	print("el precio del Kw es:", precioKw)
	print("este mes consumió:", conMesEnCurso)
	print("su importe a abonar es:", consMesAnterior*precioKw)