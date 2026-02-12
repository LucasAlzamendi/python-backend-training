# Creando diccionarios con DICT()

diccionario = dict(nombre="Lucas", apellido="Alzamendi")

print(diccionario)

# Las listas no pueden ser claves a menos que se use la funcion frosenset

# Creando diccionarios con fromkeys() - Crea un diccionario con todos los valores sin asignar
# Al crear un dict de esta manera hay que indicar las keys y el valor con el cual se inicializan las keys de caso contrario
# las keys se inicializan con el valo none - fromkeys(keys, valores) - Se puede pasar una lista como keys - Si se pasa una
# cadena toma cada char individual de esa cadena como una keys

diccionario_fromkeys = dict.fromkeys(["nombre", "apellido"],"void") 

print(diccionario_fromkeys) 

# Creando un dict a partir de dos tuplas

abecedario = (
    "A","B","C","D","E","F","G","H","I","J",
    "K","L","M","N","O","P","Q","R","S","T",
    "U","V","W","X","Y","Z"
)

abecedario_morse =(
    ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
    "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
    "..-","...-",".--","-..-","-.--","--.."
)

# ZIP - Esta funcion no es porpia de los dict. Se usa generalmente para combinar dos iterables y mediante dict() esa 
# combinacion se puede convertir en un diccionario

diccionario_morse = dict(zip(abecedario,abecedario_morse))

print(diccionario_morse)