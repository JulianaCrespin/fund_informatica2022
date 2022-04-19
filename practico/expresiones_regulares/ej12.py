#barra vertical (|).
import re
string = "este documento se llama: expresiones_regulares.py"
patron = "[\s_:]"
print(re.sub(patron, "|", string))