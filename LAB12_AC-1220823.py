# LAB DE PROGRA Sec 17
# ALBERT CENTENO 1220823
# 27/10/2023
# Objetivo: Crear un programa para administrar una lista de contactos

# Inicio
# Paso 1
lista_de_contactos = []

# Paso 2
cantidad_de_contactos = int(input("Ingrese la cantidad de contactos que va a ingresar: "))
for _ in range(cantidad_de_contactos):
    # Paso 3
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono del contacto: ")
    contacto = [nombre, numero]
    lista_de_contactos.append(contacto)

# Paso 4
print("Lista de contactos completa:")
print(lista_de_contactos)

# Paso 5
nombre_a_eliminar = input("Ingrese el nombre del contacto que desea eliminar: ")
for contacto in lista_de_contactos:
    if contacto[0] == nombre_a_eliminar:
        lista_de_contactos.remove(contacto)
        break

# Paso 6
print("Lista de contactos actualizada:")
print(lista_de_contactos)

# Paso 7
lista_de_contactos.sort(key=lambda x: x[0])

# Paso 8
print("Lista de contactos ordenada alfabéticamente:")
print(lista_de_contactos)

# Proceso
# Paso 9
nuevo_nombre = input("Ingrese el nombre del nuevo contacto en mayúsculas: ").upper()
nuevo_numero = input("Ingrese el número de teléfono del contacto nuevo: ")
lista_de_contactos.append([nuevo_nombre, nuevo_numero])

# Paso 10
posicion = int(input("Ingrese la posición donde desea agregar el nuevo contacto: "))
nuevo_nombre = input("Ingrese el nombre del contacto nuevo: ")
nuevo_numero = input("Ingrese el número de teléfono del contacto nuevo: ")
lista_de_contactos.insert(posicion, [nuevo_nombre, nuevo_numero])

# Paso 11
print("Lista de contactos completa luego de agregar un nuevo contacto:")
print(lista_de_contactos)

# Paso 12
copia_lista_ordenada = sorted(lista_de_contactos, key=lambda x: x[0], reverse=True)

# Salida
# Paso 13
print("Lista de contactos ordenada alfabéticamente de forma descendente a ascendente:")
print(copia_lista_ordenada)
print("Lista original para confirmar que no ha cambiado:")
print(lista_de_contactos)
