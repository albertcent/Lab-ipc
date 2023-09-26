# Lab Intro a la programacion
# 26/09/2023
# Albert Centeno
# Objetivo: Realizar un programa que trabaje con la secuencia de fibonacci y factoriañ

# Entrada
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = [0, 1]
        while len(seq) < n:
            next_num = seq[-1] + seq[-2]
            seq.append(next_num)
        return seq
# Proceso
while True:
    # Visualizar el menu
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Opción 1: Factorial
        try:
            numero = int(input("Ingrese un número: "))
            resultado = factorial(numero)
            print(f"{numero}! = {resultado}")
        except ValueError:
            print("Ingrese un número que sea valido.")
    
    elif opcion == "2":
        # Opción 2: Secuencia de Fibonacci
        try:
            numero = int(input("Ingrese un número: "))
            secuencia = fibonacci(numero)
            print("Secuencia de Fibonacci:", ", ".join(map(str, secuencia)))
        except ValueError:
            print("Ingrese un número que sea valido.")
    
    elif opcion == "3":
        # Opción 3: Salir del programa
        print("Vuelva pronto")
        break
    # Salida
    else:
        print("Seleccione una opcion que sea valida")