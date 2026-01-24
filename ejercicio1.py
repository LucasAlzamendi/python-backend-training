#-- Hacer un programa que pida nombre, edad e informe "Hola [nombre], en 5 años tendras [años * 5]"
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
futuro = int(input("Ingrese cantidad de años: "))
e_F = edad + futuro
texto = f"Hola {nombre}, en {futuro} años tendras {e_F}"
print(texto)