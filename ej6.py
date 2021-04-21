#Sabiendo que una carrera universitaria cuenta con X cantidad de materias, ingresar las
#notas con que un alumno aprobó cada una de las materias durante su carrera
#universitaria y finalmente mostrar la nota promedio de dicho alumno.
cantDeMaterias = int(input("ingrese la cantidad de materias totales:"))
sum = 0
for num in range(cantDeMaterias):
	nota = float(input("ingrese la nota:"))
	sum = nota + sum
print("el promedio es:", sum/cantDeMaterias)