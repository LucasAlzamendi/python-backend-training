# Datos - Una persona normal habla a una velocidad de dos palabras por segundo // Dalto habla un %30 mas rapido que una 
# persona normal

velocidad_normal = 2 
velocidad_dalto = velocidad_normal* 0.3 + 2 

# Ejercicio_02_a - Pedir al usuario que ingrese una frase y devolver cuanto tardaría en decirlo, cuanto tardía Dalto y
# cuantas palabras dijo.

frase = input("Ingrese una frase para saber cuanto tardarias en decirla: ")

cant_palabras = len(frase.split(" "))
tiempo_usuario = cant_palabras / velocidad_normal

print(f"> Tardarías {tiempo_usuario:.1f} segundos en decir la frase.")
print(f"> Ingresaste una frase de {cant_palabras} palabras")

# Ejercicio_02_b - Si se tarda mas de un minuto informar "Espera un poco tampoco te pedi un testamento."

if (60 < tiempo_usuario):
    print(f"> Espera un poco tampoco te pedi un testamento")

# Ejercicio_02_c - Si Dalto habla un %30 mas rapido informar cuanto tardaria en decirlo.

tiempo_dalto = cant_palabras / velocidad_dalto

print(f"> Dalto tardaria {tiempo_dalto:.1f} segundos en decir la frase.")