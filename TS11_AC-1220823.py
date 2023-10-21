# TS Intro a la programación
# Albert Centeno
# 1220823
# 19/10/2023
# Objetivo: Utilizar cadenas
# Entrada
palabra = input("Ingrese una palabra: ")

# Mostrar las primeras tres letras de la palabra ingresada
primeras_tres_letras = palabra[:3]
print("Las primeras tres letras son:", primeras_tres_letras)

# Almacenar las primeras tres letras en una nueva cadena
nueva_subcadena = primeras_tres_letras

# Solicitar un nuevo texto al usuario
nuevo_texto = input("Ingrese un nuevo texto: ")

# Reemplazar las vocales "O" por la letra "x" en el nuevo texto
nuevo_texto_modificado = ""
for letra in nuevo_texto:
    if letra.upper() == "O":
        nuevo_texto_modificado += "x"
    else:
        nuevo_texto_modificado += letra

# Mostrar el nuevo texto formado
print("El nuevo texto con las vocales 'O' reemplazadas por 'x' es:", nuevo_texto_modificado)
