# Vemos algunos metodos / funciones comunes con diccionarios

diccionario = {
    "nombre": "Lucas",
    "apellido": "Alzamendi",
    "edad": 24
}

# KEYS - Devuelve las claves de un diccionario. Tambien sirve para iterar (lo vemos mas adelante en el curso)

claves = diccionario.keys()

print(f"> Devuelve las KEYS de un dict: {claves}")

# GET - Segun un indice devuelve el elemento que hay en ese indice. 
# NOTA : Los elementos de un diccionario pueden ser "llamados" como si fuese una lista aunque se comporten de manera 
# diferente. 
# Si el GET no encunetra el valor devuelve -none- y continua

valor_nombre = diccionario.get("nombre") # Esta forma es mas aceptada a la hora de trabajar con DICT para no confundir con la 
# busqueda de una lista

print(f"> Devuelve el valor almacenado en la KEY 'nombre': {valor_nombre}")

valor_apellido = diccionario["apellido"] # Otra forma de buscar elementos en un DICT

print(f"> Devuelve el valor almacenado en la KEY 'apellido': {valor_apellido}")

# CLEAR - elimina todos los elementos de un DICT

diccionario_para_borrar = dict(diccionario) 

print(f"> Diccionario original copiado: {diccionario_para_borrar}")

diccionario_para_borrar.clear()

print(f"> Borrando copia del diccionario original: {diccionario_para_borrar}")

# POP - elimina un elemento del DICT. Mediante el uso de comas se pueden eliminar varios elementos con POP

diccionario.pop("nombre")

print(f"> Del DICT original se elimina 'nombre': {diccionario}")

# ITEMS - devuelve cada uno de los elementos del DICT (KEY y VALUE). 

diccionario_iterable = diccionario.items()

print(f"> Elementos del diccionario original:  {diccionario_iterable}")
