# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.
def palabra_larga(archivo):
    palabra_mas_larga = ""
    with open(archivo,"r") as file:
        for line in file:
            for palabra in line: 
                if len(palabra)> palabra_mas_larga:
                    palabra_mas_larga = palabra
                caracteres = len(palabra_mas_larga)
        print("la palabra más larga es: " + palabra_mas_larga + " y tiene " + caracteres + " caracteres.")