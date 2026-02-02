# Viendo el funcionamiento de algunos METODOS aplicados a CADENAS y OBJETOS

# Los metodos son funciones epecificas de un objeto, si no es una funcion de un objeto no es un metodo.
# Una de las diferncias, vistas en el video de SoyDalto, entre un metodo y una funcion es su forma de
# aplicarse, una funcion como DIR se aplica sobre una variable de la siguiente manera dir(variable) y un metodo
# como UPPER se aplica sobre una variable de la siguiente manera variable.upper().

# Variables de prueba 

cadena_prueba_01 = "Esta Cadena se creo para probar metodos"
cadena_prueba_02 = "Esta cadena tambien pero quiero que tenga mas palabras que la primera"
cadena_prueba_03 = "124 538785"
cadena_prueba_04 = "A453SCII"

# Metodo DIR - devuelve la lista de atributos válidos del objeto pasado. DIR no es un metodo es una funcion

contenedor_dir = dir(cadena_prueba_01)

print(f"> Mostrame los atributos de la cadena {contenedor_dir}")

# Metodo UPPER - convierte a Mayuscula una cadena. UPPER es un metodo

mayuscula_texto = cadena_prueba_01.upper()

print(f"> {mayuscula_texto}")

# Metodo LOWER - convierte a Minuscula una cadena. LOWER es un metodo

minuscula_texto = cadena_prueba_01.lower()

print(f"> {minuscula_texto}")

# Metodo CAPITALIZE - convierte la Primera Letra en Mayuscula. NOTA: para hacerlo primero pasa todo el texto a minuscula 
# y despues pasa la primera letra a Mayuscula

primera_letra_mayuscula = cadena_prueba_01.capitalize()

print(f"> {primera_letra_mayuscula}")

# Metodo FIND - encuentra la primera aparición del valor especificado, sino se encuentra devuelve -1. 
# IMPORTANTE recordar que python es CaseSensitive y que los espacios cuentan como posicion a la hora de buscar.

objetivo = "cadena"

busqueda_find = cadena_prueba_02.find(objetivo)

print(f"> En 'cadena_prueba_02' se encontro la palabra '{objetivo}' en la posicion {busqueda_find}")

# Metodo INDEX - encuentra la primera aparición del valor especificado, sino se encuentra devuelve una excepción. 
# Mas adelante en el curso vamos a ver como manejar las excepciones 

busqueda_index = cadena_prueba_01.index("a")

print(f"> Se encontro el caracter en la posicion {busqueda_index}")

# Metodo ISNUMERIC - si es numérico devuelve TRUE. Para que se considere una cadena numerica tiene que contener 
# explicitamente. De contener un espacio tambien daria FALSE la operacion.

busqueda_isnumeric = cadena_prueba_03.isnumeric()

print(f"> La 'cadena_prueba_03' es meramente numerico: {busqueda_isnumeric}")

# Metodo ISALPHA - si es alfa numérico devuelve TRUE. Si detecta un valor que no es alfa numérico da FALSE
# Los espacios no son considerados alfa numéricos por lo que de poseer uno da FALSE.

busqueda_isalpha = cadena_prueba_04.isalpha()

print(f"> La 'cadena_prueba_04' es meramente alfanumerica: {busqueda_isalpha}")

# Metodo COUNT - devuelve la cantidad de veces que encuentra un valor en una cadena, si no se encuentra devuelve cero

objetivo_02 = "*"

contar_coincidencias = cadena_prueba_02.count(objetivo_02)

print(f"> La palabra '{objetivo_02}' se encontro {contar_coincidencias}")

# Metodo LEN - cuenta los caracteres de una cadena. LEN es una funcion no un metodo. Cuenta los espacios como caracteres

contar_caracteres = len(cadena_prueba_01)

print(f"> En 'cadena_prueba_01' hay {contar_caracteres} caracteres")

# Metodo STARSWITH - verifica si una cadena empieza con una cadena dada (Ver si Dalto lo aclara)

objetivo_03 = "A4"

empieza_con = cadena_prueba_04.startswith(objetivo_03)

print(f"> La 'cadena_prueba-04' empieza con {objetivo_03}: {empieza_con}")

# Metodo ENDSWITH - verifica si una cadena empieza con otra cadena dada (Ver si Dalto lo aclara)

objetivo_04 = "4"

termina_con = cadena_prueba_03.startswith(objetivo_04)

print(f"> La 'cadena_prueba-03' termina con {objetivo_04}: {termina_con}")

# Metodo REPLACE - remplaza el primer valor que le damos por el valor 2 que le damos. 
# Para remplazar y mantener la modificacion hay que guardar la modificación en la variable que esta siendo modificada

remplazo = "4"

remplazado = "7"

cadena_nueva = cadena_prueba_03.replace(remplazo,remplazado)

print(f"> Quedo guardado {cadena_nueva} en la variable 'cadena_nueva'")

cadena_prueba_03 = cadena_nueva # Esto guarda la modificacion en la cadena principal. 
# cadena_prueba_03 = cadena_prueba_03.replace() -- esto tambien guarda la modificacion 

print(f"> Quedo guardado {cadena_prueba_03} en la cadena principal")

# Metodo SPLIT - separa una cadena con la cadena o parametro que le pasemos y crea una lista con la cantidad de elementos
# por separacion.

cadena_separada = cadena_prueba_01.split(" ")

print(f"> Separando la 'cadena_prueba_01' {cadena_separada}")

