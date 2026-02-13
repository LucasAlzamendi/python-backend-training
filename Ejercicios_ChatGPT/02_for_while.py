# Practicando el uso de WHILE mediante el cierre de bucles por contadores y chequeo de condiciones. 

contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

# Practicando el uso de FOR. Consigna: pedir al usuario un numero y mostrar la tabla de multiplicar de numero ingresado

numero = int(input("Ingrese un numero: "))

print(f"Tabla del {numero}")
for num in range(1,11):
    print(f"{numero} x {num} = {numero*num}")

# Ademas de imprimir la tabla del numero ingresado muestra la tabla de los siguientes 10 numeros ingresados por el usuario

numero_nuevo = int(input("Ingrese un numero nuevo: "))

for x in range(1,11):
    print(f"Tabla del {numero_nuevo}")
    for num in range(1,11):
        print(f"{numero_nuevo} x {num} = {numero_nuevo * num}")
    numero_nuevo += 1

# 

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

for x,valor in enumerate(lista_numeros):
    lista_numeros[x] = valor * (x+1)
    
print(lista_numeros)

for x,valor in enumerate(lista_numeros):
    lista_numeros[x] = valor // (x+1)

print(lista_numeros)