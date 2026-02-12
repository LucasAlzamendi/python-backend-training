# LIST - Crea una lista. No es lo mas comun de usar

lista = list(["Lucas","tiene",24,"años"])

print(f"> Se creo la lista: {lista}")

# LEN - Cuenta la cantidad de elementos de una lista

cantidad_elementos  = len(lista)

print(f"> Cantidad de elementos de la lista: {cantidad_elementos}")

# APPEND - Agrega un elemento a la lista

lista.append("de edad")

print(lista)

# INSERT -  Agrega un elemento a la lista en un indice especificado

lista.insert(1,"Alzamendi")

print(lista)

# EXTEND - Agrega una lista al final de otra lista

lista.extend(["y","esta","estudiando","el","curso","de","SoyDalto"])

print(lista)

# POP - Elimina un elemento de la lista por su indice. Esto tambien achica la cantidad de elementos
# de la lista. Si indice -1 se elimina el ultimo, si indice -2 se elimina el ante-ultimo y asi sucesivamente. 

lista.pop(4)

print(lista)

lista.pop(-8)

print(lista)

# REMOVE - Remueve un elemento de la lista por su valor

lista.remove("Alzamendi")

print(lista)

# CLEAR - Elimina todos los elementos de una lista dejandola vacia

lista.clear()

print(lista)

lista = [25,335,48,79,True,False] 

# SORT - Ordena una lista de forma ascendente a descendente. Si una lista tiene cadenas no las puede ordenar y da error.
# Ordena valores Booleanos tambien, primero los FLASE, segundo los TRUE y despues el resto de numeros.

lista.sort() 

print(lista)

lista.sort(reverse = True) # El parametro "reverse = True" lo ordena en reversa

print(lista)

# REVERSE - Invierte los elementos de una lista 

lista.reverse()

print(lista)

# INDEX - Busca elementos en una lista y devuelve su posicion.

elemento_encontrado = lista.index(True)

print(f"> Se encontro el elemento en la posicion: {elemento_encontrado}")