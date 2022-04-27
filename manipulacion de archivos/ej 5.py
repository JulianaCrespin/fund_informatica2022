#Escribí un programa que lea un archivo, reemplace una letra 
# por esa misma letra más un salto de línea y lo guarde en otro
# archivo.
def reemplazar(archivo, letra):
    # with open(archivo,"w") as file:
    #     /n 

      with open('nombreArchivo', 'r') as file: 
         fileContent = file.readlines()

      for fileline in fileContent: 
        fileline = fileline.replace('w', 'w \n')

      with open('otroArchivo', 'a') as f:
        for i in fileContent:
          f.write(i) 