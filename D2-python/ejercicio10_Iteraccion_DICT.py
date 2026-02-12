# Iteracción DICT

diccionario = {
    "Nombre" : "Lucas",
    "Apellido" : "Alzamendi",
    "Edad" : 24
}

# Diferentes formatos de recorrer un DICT

# Imprimir Keys
for key in diccionario:
    print(f"> Keys del diccionario: {key}")

# Imprimir Values
for value in diccionario:
    print(f"> Values del diccionario: {diccionario[value]}")

# Imprimir elementos
for key,value in diccionario.items():
    print(f"> {key}: {value}")