#Dados como datos 100 números enteros, mostrar cada uno de ellos indicando si es
#‘POSITIVO’ ó ‘NEGATIVO’, según corresponda.
for num in range(100):
	dato = (int(input("ingrese el numero:")))
	if dato == 0:
		print("el numero es cero")
	else:
		if dato > 0:
			print("el numero es positivo")
		else:
			print("el numero es negativo")

