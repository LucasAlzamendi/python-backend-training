# Ejercicio ChatGPT - Crear un pequeño menu de login en el cual se le pida al usuario que ingrese: "nombre_de_usuario" y 
# "contraseña_usuario" y si son iguales a: "nombre_usario_guardado" y "contraseña_usuario_guardada"

# Datos del usuario

id = "admin"

password = "1234"

attemps = 3

acceso = False
# Ingreso y verificación de los datos del usuario

# WHILE - Mientras la condicion sea TRUE se sigue ejecutando, tras cada loop se verifica la condicion y si es FALSE termina
# el WHILE

while 0 < attemps and not acceso:
    user_id = input("Ingrese su nombre de usuario: ")
    user_password = input("Ingrese su contraseña: ")
    if user_id == id and user_password == password:
        print("Login exitoso")
        acceso = True
    else:
        attemps -= 1
        print(f"Credenciales incorrectas. Intetnos restantes {attemps}")

if not acceso:
    print("Acceso denegado. Cuenta bloqueada")