# Laboratorio de programacion seccion 17
# 12/09/2023
# Albert Gian Carlo Centeno
# Objetivo: Determinar si un numero entero es positivo, negativo o cero
# Entrada
# Proceso
# Salida

#Mostrar en pantalla "Ejercicio 1"
print("Ejercicio 1")

#Solicitar los datos de entrada
num1=input("Ingresar numero entero:")

#Entrada a numero entero
num1=int(num1)

# Comparar datos
if num1 > 0:
    resultado = "positivo"
elif num1 < 0:
    resultado = "negativo"
else:
    resultado = "cero"

print("Resultado:", resultado)