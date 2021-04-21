cont = 0 
sum = 0
for num in range (200):
    importe = float(input("ingrese el importe:"))
    if importe < 100:
        cont = cont + 1
    else :
        sum = sum + importe
print("la cantidad de ventascon importes menores a 100 fue:",cont)
print("la suma total de las ventas mayores o iguales a 100 es:",sum)