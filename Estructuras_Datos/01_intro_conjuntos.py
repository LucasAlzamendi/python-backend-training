# Creando conjuntos con SET()

conjunto_01 = set(["dato_01","dato_02"])

# Union de conjuntos mediante frozenset()

conjunto_02 = frozenset(["dato_03", "dato_04"])
conjunto_03 = (conjunto_02,"dato_05", "dato_06", 7)

print(conjunto_03)

# Teoria de conjuntos

conjunto_01 = {1,3,5,7}
conjunto_02 = {1,3,7}

# Verificando si es un conjunto

# Forma de verificar si un subjunto pertenece a un superjunto
resultado_subconjunto = conjunto_02.issubset(conjunto_01) 
resultado_SBC = conjunto_02 <= conjunto_01 # Hace lo mismo que .issubset()

# Forma de verificar si un superjunto contiene a un subjunto
resultado_superconjunto = conjunto_01.issuperset(conjunto_02)
resultado_SPC = conjunto_02 > conjunto_01

# Forma de verificar si dos conjuntos no tienen algun numero en comun 

resultado_elemento = conjunto_02.isdisjoint(conjunto_01)

#Muestra resultados conjuntos

print(f"> Subjunto pertenece a superjunto: {resultado_subconjunto}")
print(f"> Superjunto contiene a subjunto: {resultado_superconjunto}")
print(f"> Los subjuntos analizados (02 y 01) poseen algun numero en comun: {resultado_elemento}")