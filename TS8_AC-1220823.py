# TS Intro a la programación sec. 17
# 28/09/2023
# Albert Gian Carlo Centeno
# 1220823
# Objetivo: Mostrar la secuencia de números en un rango

#Ejercicio 1: secuencia de 1 a 25 incrementando en 1 "for"
for i in range(1, 26):
    print (i, end=", ")
print()
#Ejercicio 2: secuencia de 1 a 25 incrementando en 1 "while"
i = 1
while i <=25:
    print(i, end=", ")
    i += 1
print()

#Ejercicio 3: secuencia de 5 a 50 incrementando en 5 "for"
for i in range(5, 51, 5):
    print (i, end=", ")
print()

#Ejercicio 4: secuencia de 5 a 50 incrementando en 5 "while"
i = 5
while i <=50:
    print(i, end=", ")
    i += 5
print()

#Ejercicio 5: secuencia de 20 a 0 decrementando en 2 "for"
for i in range(20, -1, -2):
    print (i, end=", ")
print()

#Ejercicio 6: secuencia de 20 a 0 decrementando en 2 "while"
i = 20
while i >=0:
    print(i, end=", ")
    i -= 2