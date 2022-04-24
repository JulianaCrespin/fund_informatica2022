def bien_escrito(correo):
    if "@" in correo:
        print("Es válido")
    else:
        print("No es válido")

bien_escrito("nombre@correo.dominio")
