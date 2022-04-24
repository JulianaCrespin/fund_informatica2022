#ej 4 mejorado
def capitalizar():
    nombre = input("introduzca su nombre: ")
    apellido1 = input ("introduzca su primer apellido: ")
    apellido2 = input ("introduzca su segundo apellido: ")
    nombre_cap= str.capitalize(nombre)
    apellido1_cap= str.capitalize(apellido1)
    apellido2_cap= str.capitalize(apellido2)
    print(nombre_cap + " " + apellido1_cap + " " + apellido2_cap)
capitalizar()