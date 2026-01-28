# Resultado de condicionales

# AND - se escribe & en python

print("Analizando & (and) y sus resultados")

resultado01 = True & True # Devuelve True
resultado02 = True & False # Devuelve False
resultado03 = False & True # Devuelve False
resultado04 = False & False # Devuelve False

print(f"Cuando las dos condiciones en un & son TRUE el resultado de la operacion da: {resultado01}")
print(f"Cuando al menos una de las dos condiciones en un & es FALSE el resultado de la operacion da: {resultado02}")
print(f"Cuando las dos condiciones en un & son FALSE el resultado de la operacion da: {resultado04}")

# OR - se escribe | en python

print("Analizando | (or) y sus resultados")

resultado05 = True | True # Devuelve True
resultado06 = True | False # Devuelve True
resultado07 = False | True # Devuelve True
resultado08 = False | False # Devuelve False

print(f"Cuando las dos condiciones en un | son TRUE el resultado de la operacion da: {resultado05}")
print(f"Cuando al menos una de las dos condiciones en un | es TRUE el resultado de la operacion da: {resultado06}")
print(f"Cuando las dos condiciones en un | son FALSE el resultado de la operacion da: {resultado08}")

# NOT - se escribe not en python

print("Analizando not y sus resultados")

resultado09 = not True # Devuelve False
resultado10 = not False # Devuleve True

print(f"Cuando la condicion en un -not- es TRUE el resultado de la operacion da: {resultado09}")
print(f"Cuando la condicion en un -not- es FALSE el resultado de la operacion da: {resultado10}")