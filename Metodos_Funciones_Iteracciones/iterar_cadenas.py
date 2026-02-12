# Iterando cadenas - break y continue

frutas = ["manzana", "durazno", "pera", "mango", "banana", "anana"]
cadena = "Voy a comer: "
numeros = [1,2,3,4,5]

# Evitando que consuma una pera

for fruta in frutas:
    if fruta == "pera":
        print(f"Pero no pienso comer {fruta}")
        continue
    else:
        print(f"{cadena}{fruta}")

# Evitar que el bucle siga
print(" ")
for fruta in frutas:
    if fruta == "mango":
        print(f"Un {fruta} que asco ya no puedo comer")
        break
    else:
        print(f"{cadena}{fruta}")

# Recorriendo una cadena

for letra in cadena:
    print(letra)

# FOR en una linea de codigo

numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)