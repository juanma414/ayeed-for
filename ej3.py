#Ingresando una sucesión de 300 números enteros, determinar la cantidad de números.
#positivos que hay en ella.
con = 0
for num in range(300):
	dato = int(input("ingrese el numero:"))
	if dato > 0 :
		con = con + 1
print("la cantidad de numeros positivos ingresados es:",con)		