#Ejercicio: Crear lista numeros - Mostrar elementos de la lista - Convertir todos a Strings - Mostrar los elementos

#Crear lista numeros

lista_N5 = [1,2,3,4,5]

# Forma 1 - índice
for i in range(len(lista_N5)):
    print(lista_N5[i])

#Forma 1.1 - índice 
for elemento in lista_N5:
    print(elemento)
    
# Forma 2 - directa
print(lista_N5)

# Forma 3 - iterador
it = iter(lista_N5)

print(it)
print(type(it))

for i in range(len(lista_N5)):
    print(next(it))

# Convertir a string
for i in range(len(lista_N5)):
    lista_N5[i] = str(lista_N5[i])

# Mostrar resultado final
print(lista_N5)