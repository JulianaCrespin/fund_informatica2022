def eliminar_saltos(entrada,salida):
    with open(entrada,"r") as f, open(salida,"w") as s:
        for line in f:
            s.write(line.strip("\n"))