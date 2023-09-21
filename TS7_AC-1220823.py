# TS Lab Intro a la programación sec. 17
# 21/09/2023
# Albert Centeno
# Objetivo: Utilizar la instruccion for
# Entrada:

# Mostrar nombre completo
print("Albert Gian Carlo Centeno Herrarte")

#Proceso
# Solicita al usuario que ingrese un número en el rango de 1 a 10
numero = int(input("Por favor, ingresar un número del 1 al 10: "))

# Verifica que esté en el rango correcto
if 1 <= numero <= 10:
    # Salida
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
else:
    print("El número ingresado no está en el rango correcto (Entre 1 o 10).")