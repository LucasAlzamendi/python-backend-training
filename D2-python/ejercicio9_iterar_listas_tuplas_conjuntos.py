# Iteracion de (listas - tuplas - conjuntos) mediante FOR 

nombres = ["Mateo", "Ignacio", "Lucas", "Facundo"]
numeros = (1,3,53,12,2,34)

for nombre in nombres:
    print(f"Alumnos en primer año: {nombre}")

for numero in numeros:
    resultado = numero * 2
    print(resultado)

# Mediante la funcion ZIP() es posible recorrer multiples listas simultaneamente. IMPORTANTE: si las listas unidas por el ZIP()
# son de distinto tamaño solo se recorrera hasta el final de la lista mas corta.

for nombres,numero in zip(nombres,numeros):
    print(f"> Recorriendo la lista 1: {nombre}")
    print(f"> Recorriendo la lista 2: {numero}")

# Desplazando con la funcion RANGE()

for num in range(1,15):
    print(f"> Imprimiendo numeros mediante RANGE: {num}")

# Recorriendo una lista con RANGE - No es la mas optima - Este formato no funciona con conjuntos

for indice in range(len(numeros)):
    print(f"> En la posicion {indice + 1} se aloja: {numeros[indice]}")

# Forma correcta de recorrer una lista - FOR indice,valor IN enumerate()

for i,val in enumerate(numeros):
    print(f"> En la posición {i + 1} se encontro el valor: {val}")

# Usando el FOR-ELSE - Un else de un FOR siemrpre se va a ejecutar al finalizar el FOR

for num in numeros:
    print(f"> Numeros: {num}")
else: 
    print("Fin impresión")