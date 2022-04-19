def cargarSocios(socios):
    numero = int(input("Número de socio: "))
    while numero != 0:
        nombre = input("Nombre y apellido: ")
        fecha = input("Fecha de ingreso: ")
        cuota = input("¿Cuota al día? s/n: ")
        pago = cuota.lower() == "s"
        socios[numero] = [nombre, fecha, pago]
        numero = int(input("Número de socio: "))
    return socios
    
def modificarFecha(socios, fechaAnterior, fechaNueva):
    for datos in socios.values():
        if datos[1] == fechaAnterior:
            datos[1] = fechaNueva
    return socios
    
    
def numeroSocio(socios, nombre):
        for numero,datos in socios.items():
            if datos[0].lower() == nombre.lower():
                return numero
        return 0
                
                
def formatoFecha(fecha):
    return fecha[:2] + "/" + fecha[2:4] + "/" + fecha[4:]


def imprimirListado(socios):
    for numero,datos in socios.items():
        print("Número: ", numero)
        print("Nombre: ", datos[0])
        print("Fecha de ingreso ", formatoFecha(datos[1]))
        if datos[2]:
            print("Cuota al día")
        else:
            print("En deuda")
        print("---------------")
    return None

socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}

print("Cargar socios")
socios_activos = cargarSocios(socios_activos)

print("El club tiene", len(socios_activos), "socios")

print("Registrar pago de cuotas")
numero = int(input("Numero de socio: "))
socios_activos[numero][2] = True

print("Modificando fecha de ingreso...")
socios_activos = modificarFecha(socios_activos, "21102017", "22102017")

print("Eliminar socio:")
nombre = input("Nombre y apellido: ")
numero = numeroSocio(socios_activos, nombre)
del socios_activos[numero]

imprimirListado(socios_activos)