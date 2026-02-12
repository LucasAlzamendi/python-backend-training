# Diferentes formas de crear y trabajar con Tuplas
# NOTA : a la hora de trabajar con datos que NO SE DEBEN MODIFICAR se recomienda el uso de tuplas 

# Convirtiendo una lista a tupla con tuple()

tupla_01 = tuple(["dato_01", "dato_02"])

# Creando tupla sin parentesis

tupla_02 = "dato_03", "dato_04"

# Creando tupla sin parentesis de un solo elemento

tupla_03 = "dato_05",

print(tupla_01)
print(tupla_02)
print(tupla_03)

#Probando limites con tuplas

tupla = ('x', 5, 'u', 35, '35s', 62, 'mateo')
tupla_1 =(2, 5, 8, 7) 
lista = []
lista_1 = ['Basura', 'mucho', 8, 9, 56]

#lista = tupla
#Si no se convierte una tupla cuando se asigna a una lista, esta va a quedar guardada como si fuese una tupla 
# con todas las caracteristicas que esto conlleva 

lista = list(tupla)

print(type(lista))
print(lista)

#Se pueden comparar: tuplas con listas // listas con listas // tuplas con tuplas
print(lista_1 != tupla)

print(lista == lista_1)

print(tupla == tupla_1)

# Se pueden compara las longitudes de: tuplas con listas // listas con listas // tuplas con tuplas

print(len(lista) != len(lista_1))

print(len(lista) != len(tupla))

print(len(tupla) != len(tupla_1))