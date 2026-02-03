# Datos - El Curso de "SoyDalto" dura 1,5 HS // El promedio de otros cursos dura 4 HS // El mas rapido de otros cursos dura
# 2,5 HS // El mas lento de otros curosos dura 7 HS // El contenido CRUDO proemdio de otros cursos es de 5 HS // El
# contenido CRUDO del curso de "SoyDalto" es de 3.5 HS

# "Contenido CRUDO" = Contenido sin editar

# Datos

duracion_curso_soydalto = 1.5 

duracion_curso_promedio = 4
duracion_curso_mas_rapido = 2.5 
duracion_curso_mas_lento = 7 

contenido_crudo_soydalto = 3.5
contenido_crudo_promedio = 5

# Ejercicio_01_a - Calcular la diferencia porcentual entre el curso de "Soy Dalto" contra el mas rapido de los otros, el mas
# lento de los otros y el promedio. 

print("Ejercicio_01_a")

dif_promedio = (duracion_curso_promedio - duracion_curso_soydalto) / duracion_curso_soydalto * 100 
dif_mas_rapido = (duracion_curso_mas_rapido - duracion_curso_soydalto) / duracion_curso_soydalto * 100
dif_mas_lento = (duracion_curso_mas_lento - duracion_curso_soydalto) / duracion_curso_soydalto * 100

print(f"> El promedio de los cursos dura un {dif_promedio:.2f}% más que el curso de SoyDalto.")
print(f"> El curso mas rapido dura un %{dif_mas_rapido:.2f} más que el curso de SoyDalto.")
print(f"> El curso mas lento dura un %{dif_mas_lento:.2f} más que el curso de SoyDalto.")

# Ejercicio_01_b - Calcular que porcentaje de material inservible que se descarta tras la edicion de los videos de 
# "SoyDalto" y de los cursos promedios

print("Ejercicio_01_b")

descarte_curso_soydalto = (100 - (duracion_curso_soydalto * 100) / contenido_crudo_soydalto)
descarte_curso_promedio = (100 - (duracion_curso_promedio * 100) / contenido_crudo_promedio)

print(f"> En el curso de 'SoyDalto' se descarta %{descarte_curso_soydalto:.2f} de material inservible.")
print(f"> En los cursos promedios se descarta %{descarte_curso_promedio:.2f} de material inservible.")

# Ejercicio_01_c - Ver 10 hs del curso "SoyDalto" a cuantas horas equivale en otros cursos y viceversa

print("Ejercicio_01_c")

HORAS_ANALISIS = 10

# Calculo equivalente "SoyDalto" con otros cursos- equi => equivalente

equi_promedio = ((HORAS_ANALISIS * duracion_curso_promedio) / duracion_curso_soydalto)
equi_mas_rapido = ((HORAS_ANALISIS * duracion_curso_mas_rapido) / duracion_curso_soydalto)
equi_mas_lento = ((HORAS_ANALISIS * duracion_curso_mas_lento) / duracion_curso_soydalto)

# Informe equivalentes "SoyDalto" con otros cursos
print("Equivalente 'SoyDalto' con otros cursos")
print(f"> Ver {HORAS_ANALISIS} horas del curso SoyDalto equivale a {equi_promedio:.2f} horas del curso promedio.")
print(f"> Ver {HORAS_ANALISIS} horas del curso SoyDalto equivale a {equi_mas_rapido:.2f} horas del curso mas rapido.")
print(f"> Ver {HORAS_ANALISIS} horas del curso SoyDalto equivale a {equi_mas_lento:.2f} horas del curso mas lento.")

# Calculo equivalente otros cursos con "SoyDalto"

equi_inverso_promedio = ((HORAS_ANALISIS * duracion_curso_soydalto) / duracion_curso_promedio)
equi_inverso_mas_rapido = ((HORAS_ANALISIS * duracion_curso_soydalto) / duracion_curso_mas_rapido)
equi_inverso_mas_lento = ((HORAS_ANALISIS * duracion_curso_soydalto) / duracion_curso_mas_lento)

# Informe equivalentes otros cursos con "SoyDalto"
print("Equivalente otros cursos con 'SoyDalto'")
print(f"> Ver {HORAS_ANALISIS} horas de un curso promedio equivale a {equi_inverso_promedio:.2f} horas del curso SoyDalto.")
print(f"> Ver {HORAS_ANALISIS} horas del curso mas rapido equivale a {equi_inverso_mas_rapido:.2f} horas del curso SoyDalto.")
print(f"> Ver {HORAS_ANALISIS} horas del curso mas lento equivale a {equi_inverso_mas_lento:.2f} horas del curso SoyDalto.")