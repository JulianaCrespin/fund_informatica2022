#12
cantidad = int(input("introducir cantidad de alumnos: "))
alumnos = {}

for num in range(0, cantidad):
    alumno = input ("alumno: ")
    notas = []
    nota = int(input("nota: "))
    while nota >= 0:
        notas.append(nota)
        nota = int(input("nota: "))
# print(alumnos)
    alumnos[alumno] = notas
for alumno in alumnos:
    print(alumno,sum(alumnos[alumno])/len(alumnos[alumno]))