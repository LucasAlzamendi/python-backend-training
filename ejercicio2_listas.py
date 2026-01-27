#Ejercicios con  Listas y Tuplas. Actualizacion de edades

#El indice de Tuplas y Lista empieza en cero

#Listas. Se pueden modificar

#Tuplas. No se puede modificar

lista_edades = [15, 35, 44, 66, 95, 65]
tupla_nombres = ("Lucas", "Maria", "Carlos", "Juan", "Juliana", "Cecilia")

#Le pido al usuario que ingrese un indice para ver a quien se le modifica la edad

while True:
    try:
        indice = int(input("Ingrese un índice entre 1 y 6: "))
        if 1 <= indice <= 6:
            break
        else:
            print("Fuera de rango")
    except ValueError:
        print("Debe ingresar un número")

# Se pide al usuario que ingrese años en el futuro

while True:
    try:
        incremento_edad = int(input("Ingrese cuantos años desea sumar: "))
        if incremento_edad >= 0:
            break
        else:
            print("Debe ingresar un número positivo")
    except ValueError:
        print("Debe ingresar un número")

# Modifico el indice para que python lo interprete correctamente
indice -= 1

edad_original = lista_edades[indice]

lista_edades[indice]+=  incremento_edad

print(f"{tupla_nombres[indice]} tiene {edad_original} y en {incremento_edad} años tendra {lista_edades[indice]}")

print(f"{tupla_nombres[indice]} // {lista_edades[indice]}")