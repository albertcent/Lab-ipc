#Lab de intro a la programación sec. 17
#10/10/2023
#Albert Gian Carlo Centeno Herrarte
#Objetivo: Crear un módulo con las funciones necesarias para convertir una cantidad expresada en centímetros 
#Entrada

#Centimetros a metros
def cm_a_m(cantidad):
    return cantidad/100 

#Centimetros a kilometros
def cm_a_km(cantidad):
    return cantidad/100000

#Centimetros a pulgadas
def cm_a_pulg(cantidad):
    return cantidad/2.54

#Centimetros a pies
def cm_a_pies(cantidad):
    return cantidad/30.48

#Proceso
while True:
    try:
        centimetros = float((input("Ingrese la cantidad en centimetros:")))
        print("Seleccione la unidad de conversión que desea utilizar:")
        print("1. Centimetros a metros")
        print("2. Centimetros a kilometros")
        print("3. Centimetros a pulgadas")
        print("4. Centimetros a pies")
        opcion = int(input("Opción:"))

        if opcion == 1:
            resultado = round(cm_a_m(centimetros),2)
            unidad = "metros"
        elif opcion == 2:
            resultado = round(cm_a_km(centimetros),2)
            unidad = "kilometros"
        elif opcion == 3:
            resultado = round(cm_a_pulg(centimetros),2)
            unidad = "pulgadas"
        elif opcion == 4:
            resultado = round(cm_a_pies(centimetros),2)
            unidad = "pies"
        else:
            print("Por favor escoja una opción valida")
        print(f"{centimetros} centímetros son {resultado} {unidad}")

        respuesta = input("¿Realizar otra conversión? (Sí/No): ")
        if respuesta.lower() != "si":
            break
#Salida
    except ValueError:
        print("Por favor, ingrese una cantidad válida.")
