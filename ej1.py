remuneracion = float(input("ingrese la remuneracion:"))
for operario in range(50):
	horas = float(input("ingrese la cantidad de horas:"))
	sueldo = horas * remuneracion
	print("el sueldo del operario es:",sueldo)