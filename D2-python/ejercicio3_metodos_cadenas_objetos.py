# Viendo el funcionamiento de algunos METODOS aplicados a CADENAS y OBJETOS

# Una de las diferncias, vistas en el video de SoyDalto, entre un metodo y una funcion es su forma de
# aplicarse, una funcion como DIR se aplica sobre una variable de la siguiente manera dir(variable) y un metodo
# como UPPER se aplica sobre una variable de la siguiente manera variable.upper()

# Variables de prueba 

cadena_prueba_01 = "Esta Cadena se creo para probar metodos"
cadena_prueba_02 = "Esta cadena tambien pero quiero que tenga mas palabras que la primera"

# Metodo DIR - devuelve la lista de atributos válidos del objeto pasado. DIR no es un metodo es una funcion

contenedor_dir = dir(cadena_prueba_01)

print(contenedor_dir)

# Metodo UPPER - convierte a Mayuscula una cadena. UPPER es un metodo

mayuscula_texto = cadena_prueba_01.upper()

print(mayuscula_texto)

# Metodo LOWER - convierte a Minuscula una cadena. LOWER es un metodo

minuscula_texto = cadena_prueba_01.lower()

print(minuscula_texto)

# Metodo CAPITALIZE - convierte la Primera Letra en Mayuscula. NOTA: para hacerlo primero pasa todo el texto a minuscula 
# y despues pasa la primera letra a Mayuscula

primera_letra_mayuscula = cadena_prueba_01.capitalize()

print(primera_letra_mayuscula)

# Metodo FIND - encuentra la primera aparición del valor especificado, sino devuelve 1

# Metodo INDEX - encuentra la primera aparición del valor especificado, sino devuelve una excepción

# Metodo ISNUMERIC - si es numérico devuelve TRUE

# Metodo ISALPHA - si es alfa numérico devuelve TRUE

# Metodo COUNT - devuelve el número de ocurrencia de una subcadena en la cadena dada

# Metodo LEN - cuenta los caracteres de una cadena

# Metodo ENDSWITH - verifica si una cadena ¿empieza? con ??? (Ver si Dalto lo aclara)

# Metodo STARSWITH - verifica si una cadena ¿termina? con ??? (Ver si Dalto lo aclara)

# Metodo REPLACE - remplaza un valor por otro

# Metodo SPLIT - separa por el parametero dado