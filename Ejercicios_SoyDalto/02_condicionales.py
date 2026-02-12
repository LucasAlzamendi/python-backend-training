# Repasando condicionales en python
while True:
    try:
        edad = int(input('Ingrese su edad: '))
        if 0 < edad:
            break
        else:
            print('Edad no valida.')
    except ValueError:
        print('Ingrese su edad en numeros.')    

# Condicional if - else

if 18 <= edad:
    print('Podes pasar')
else:
    print('No podes pasar')    

while True:
    try:
        nueva_edad = int(input('Ingrese una nueva edad: '))
        if 0 < nueva_edad:
            break
        else:
            print('Edad no valida.')
    except ValueError:
        print('Ingrese una edad en numeros.')   

# Condicional if - elif

if 18 <= nueva_edad:
    print('No hay problema. Podes pasar.')
elif 14 <= nueva_edad < 18:
    print('Hay un problema. No te da la edad. No podes pasar.')
else:
    print('Pibe, ¿Qué haces aca? ¿Dónde estan tus papas?')