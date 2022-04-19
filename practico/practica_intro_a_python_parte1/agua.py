def calcular_cantidad_de_agua(cant_personas):
  agua = cant_personas*30
  if agua>1000:
    return "tenés que cargar " + str(agua) + " ml. ¡OJO! vas a necesitar otro termo"
  else:
    return "tenés que cargar " + str(agua) + " ml."