# Lab Introduccion a la programacion sec. 17
# 19/09/2023
# Albert Centeno
# Objetivo
# Entrada

#Imprimir en pantalla el mensaje
print("Ejercicio 1: operaciones aritmeticas")

#Ingresar los dos valores
N1= input("Ingresar un numero:")
N2= input("Ingresar otro numero:")
N3=""

#Realizar las operaciones
while N3!="fin":
    N3=input("Ingrese la operacion que desee realizar (suma, resta, multiplicacion, division, modulo, exponenciacion o cociente)")
    N1=int(N1)
    N2=int(N2)
    suma=N1+N2
    resta=N1-N2
    multiplicacion=N1*N2
    division=N1/N2
    modulo=N1%N2
    exponenciacion=N1**N2
    cociente=N1//N2

#Mostrar los resultados
    if N3=="suma":
        print(str(N1)+"+"+str(N2)+"="+str(suma))
    elif N3=="resta":
        print(str(N1)+"-"+str(N2)+"="+str(resta))
    elif N3=="multiplicacion":
        print(str(N1)+"*"+str(N2)+"="+str(multiplicacion))
    elif N3=="division":
        print(str(N1)+"/"+str(N2)+"="+str(division))
    elif N3=="modulo":
        print(str(N1)+"%"+str(N2)+"="+str(modulo))
    elif N3== "exponenciacion":
        print(str(N1)+"**"+str(N2)+"="+str(exponenciacion))
    elif N3=="cociente":
        print(str(N1)+"//"+str(N2)+"="+str(cociente))
    elif N3=="fin":
        print("Programa finalizado")
