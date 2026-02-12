# INPUT - Permite pedirle datos al usuario por consola. 

nombre_usuario = input("Ingrese su nombre: ")

# PRINT - Muestra datos 

print(f"> Se ingreso el nombre: {nombre_usuario}")

# Siempre que se hace un INPUT lo que se ingresa por teclado se guarda como una cadena de texto por lo que si queremos 
# trabajar con otros valores hay que convertir el INPUT al valor que se desee antes de  guardarlo 

edad_usuario = int(input("Ingrese su edad: "))

print(f"> Se ingreso la edad: {edad_usuario}")