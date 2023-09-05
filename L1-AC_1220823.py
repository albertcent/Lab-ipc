
# Laboratorio de introduccion a la programacion seccion : 17
# 05/09/2023
# Albert Gian Carlo Centeno
# OBJETIVO
# ENTRADA: numero1 y numero2
# PROCESO:

# Paso 1: Ingresar numeros
numero1= float(input("Ingresar el primer numero"))
numero2= float(input("Ingresar el segundo numero"))

#Paso 2: Realizar operaciones
suma= numero1 + numero2
resta= numero1 - numero2
multiplicacion= numero1 * numero2

# Asegurar denominador no queda cero en la division
if numero2 != 0:
    division = numero1/numero2
else:
    division = "No se puede dividir"

#   Paso 3: Arrojar resultados
print("Suma", suma)
print("Resta", resta)
print("Multiplicacion", multiplicacion)
print("Division",division)