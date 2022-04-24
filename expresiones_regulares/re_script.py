import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.findall(patron,texto))
print(texto[22:26])