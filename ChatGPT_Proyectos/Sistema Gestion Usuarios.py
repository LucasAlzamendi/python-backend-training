# Consigna - Crear un sistema de gestion de usuarios (en memoria). Los usuarios se deben guardar en una lista - 
# cada usuario puede ser solo un nombre (de momento) - usar while - Validar opciones inválidas
# El ingreso de usuarios es por teclado - Al finalizar el ingreso se debe mostrar los usuarios de manera enumerada 
# Se debe pedir un numero y eliminar al usuario correspondiente al numero 
# EXTRA: No admitir eliminaciones si la lista esta vacia - No admitir indices invalidos 

# Zona de datos 

usuarios = []
cierre = False

# Programa Principal

# Operaciones permitidas

print("Bienvenido al Sistema de Organizacion de Usuarios")
print("Operaciones Permitidas")
print("--------------------------------------------------")
print("1 - Ingresar usuarios")
print("2 - Mostrar usuarios")
print("3 - Eliminar usuarios")
print("4 - Salir del sistema")
print("--------------------------------------------------")

while not cierre:
    
    operacion = input("Ingrese la operación que desea realizar: ")
    # Agregar Usuario 
    if operacion == "1":
        usuarios.append(input("Ingrese un nuevo usuario: "))

    # Listar Usuarios
    elif operacion == "2":
        if not usuarios:
            print("No hay usuarios registrados")
        else:
            for indice, usuario in enumerate(usuarios,0):
                print(f"{indice + 1} - {usuario}")

    # Eliminar Usuario            
    elif operacion == "3":
        if not usuarios:
            print("No hay usuarios registrados para eliminar")
        else:
            indice = int(input("Ingrese la posicion del usuario que desea eliminar: "))-1
            if 0 <= indice < len(usuarios):
                usuarios.pop(indice)
            else:
                print("El numero ingresado no representa a un usuario registrado")

    # Salir
    elif operacion == "4":
        cierre = True
        print("Gracias por trabajar con mi Sistema de Organizacion de Usuarios")

if not usuarios:
    print("Tras el cierre del S.O.U no quedaron usuario registrados")
else:
    for indice,usuario in enumerate(usuarios,0):
        print(f"{indice + 1} - {usuario}")