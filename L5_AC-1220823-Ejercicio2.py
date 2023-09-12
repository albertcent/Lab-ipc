#Introduccion a la programacion
#12/09/2023
#Albert Centeno
#1220823
#Objetivo: Determinar los dias de la semana a traves de ingresar numeros

#Ejercicio 02
#Entrada: ingresar numero de dia
x = input("Ingresar un numero de dia:")
x = int(x)
d=""
#Proceso
if x<0 or x>7:
    d= "¡Error!, ingresar un numero entre 1 y 7"
elif x==1:
    d="Lunes"
elif x==2:
    d="Martes"
elif x==3:
    d="Miercoles"
elif x==4:
    d="Jueves"
elif x==5:
    d="Viernes"
elif x==6:
    d="Sabado"
else:
    d="Domingo"
print("Dia: " + d)
#Salida: numero de dia con dia