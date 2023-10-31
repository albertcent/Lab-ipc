# Lab Intro a la programación sec. 17
# 31/10/2023
# Albert Centeno
# Objetivo: crear una clase

#Entrada
from datetime import datetime

class Persona:
    def __init__(self):
        self.nombres = input("Ingrese los nombres: ")
        self.apellidos = input("Ingrese los apellidos: ")
        self.apellido_casada = input("Ingrese el apellido de casada (o presione Enter si no tiene): ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (en formato AÑO-MES-DÍA en números): ")
        if fecha_nacimiento:
            self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
        else:
            self.fecha_nacimiento = None
#Proceso
    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        if self.apellido_casada:
            return f"{self.apellidos} de {self.apellido_casada}"
        else:
            return self.apellidos

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def obtener_nombre_completo(self):
        return f"{self.nombres} {self.obtener_apellidos()}"

    def obtener_edad(self):
        if self.fecha_nacimiento:
            hoy = datetime.now().date()
            edad = hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
            return edad
        else:
            return "Fecha de nacimiento no brindada"

# Salida
persona = Persona()

print("Nombres:", persona.obtener_nombres())
print("Apellidos:", persona.obtener_apellidos())
print("Fecha de Nacimiento:", persona.obtener_fecha_nacimiento())
print("Nombre Completo:", persona.obtener_nombre_completo())
print("Edad:", persona.obtener_edad())
