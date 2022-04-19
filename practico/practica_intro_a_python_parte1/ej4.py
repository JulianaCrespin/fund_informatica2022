def capitalizar():
    nombre = input("introduzca su nombre: ")
    apellido1 = input ("introduzca su primer apellido: ")
    apellido2 = input ("introduzca su segundo apellido: ")
    nombre_cap= str.upper(nombre[0]) + nombre[1:]
    apellido1_cap= str.upper(apellido1[0]) + apellido1[1:]
    apellido2_cap= str.upper(apellido2[0]) + apellido2[1:]
    print(nombre_cap + " " + apellido1_cap + " " + apellido2_cap)
capitalizar()