def guardar(archivo1, archivo2, arch_existente):
    with open(arch_existente, "a") as s:
        archivo1 = open("r")
        s.write(archivo1.read())
        archivo1.close()


def join_files(file1,file2,file3):
    with open(file1,"r") as f1, open (file2,"r") as f2, open(file3,"a") as f3:
        f3.write(f1.read() + f2.read())