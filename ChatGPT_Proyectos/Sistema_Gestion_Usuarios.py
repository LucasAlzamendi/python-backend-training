# Consigna - Crear un sistema de gestion de usuarios (en memoria). Los usuarios se deben guardar en una lista - 
# cada usuario puede ser solo un nombre (de momento) - usar while - Validar opciones inválidas
# El ingreso de usuarios es por teclado - Al finalizar el ingreso se debe mostrar los usuarios de manera enumerada 
# Se debe pedir un numero y eliminar al usuario correspondiente al numero 
# EXTRA: No admitir eliminaciones si la lista esta vacia - No admitir indices invalidos 

# Datos 

usuarios = []
cierre = False

# ==============================
# Sistema de Organización de Usuarios
# ==============================

print("Bienvenido al Sistema de Organizacion de Usuarios")

while not cierre:
    
    # Operaciones permitidas
    print("Operaciones Permitidas")
    print("--------------------------------------------------")
    print("1 - Ingresar usuarios")
    print("2 - Mostrar usuarios")
    print("3 - Eliminar usuarios")
    print("4 - Salir del sistema")
    print("--------------------------------------------------")
    
    operacion = input("Ingrese la operación que desea realizar: ")
    print("")
    # Agregar Usuario 
    if operacion == "1":
        usuarios.append(input("Ingrese un nuevo usuario: "))

    # Listar Usuarios
    elif operacion == "2":
        if not usuarios:
            print("No hay usuarios registrados")
        else:
            for indice, usuario in enumerate(usuarios,start=0):
                print(f"{indice + 1} - {usuario}")

    # Eliminar Usuario            
    elif operacion == "3":
        if not usuarios:
            print("No hay usuarios registrados para eliminar")
        else:
            # Ingresa que usuario se va a eliminar
            entrada = input("Ingrese la posicion del usuario que desea eliminar: ")
            print("")
            # Cheuea si el valor ingresado es valido y de serlo elimina e informa que usuario fue
            if not entrada.isdigit():
                print("El valor ingresado no es valido")
            else:
                indice = int(entrada) - 1
                if 0 <= indice < len(usuarios):
                    eliminado = usuarios.pop(indice)
                    print(f"Usuario '{eliminado}' eliminado correctamente")
                else:
                    print("El numero ingresado no representa a un usuario registrado")

    # Salir
    elif operacion == "4":
        cierre = True
        print("Gracias por trabajar con mi Sistema de Organizacion de Usuarios")
    print("")

# Informa cantidad de usuarios tras el uso del S.O.U
if not usuarios:
    print("Tras el cierre del S.O.U no quedaron usuario registrados")
else:
    for indice,usuario in enumerate(usuarios,start=0):
        print(f"{indice + 1} - {usuario}")