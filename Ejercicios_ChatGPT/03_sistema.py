# Consigna - Crear un pequeño sistema en bucle del cual el usuario pueda elegir, mediante un imput, si salir o seguir 

cierre = False
bucles = 0

while not cierre:
    bucles += 1
    
    print("1 - Saludar")
    print("2 - Mostrar mensaje")
    print("3 - Salir")
    
    opcion = input("Seleccione alguna de las opciones: ")
    
    if opcion == "1":
        print("Hola usuario")
    elif opcion == "2":
        print("Hoy es un gran día para programar")
    elif opcion == "3":
        print("Saliendo del sistema...")
        cierre = True
    else:
        print("Opción inválida")

print(f"Usted uso el sistema {bucles} veces")