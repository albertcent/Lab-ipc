# Lab Intro a la programación sec. 17
# 07/11/2023
# Albert Centeno 1220823
# Objetivo: crear una clase llamada automovil

#Entrada
class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = False
        self.tipoCambioDolar = 0.0
        self.descuentoAplicado = 0.0
    
    def DefinirModelo(self, unModelo):
        self.modelo = unModelo
    
    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio
    
    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca
    
    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio
    
    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible
    
    def MostrarDisponibilidad(self):
        return "Disponible" if self.disponible else "No se encuentra disponible actualmente"
    
    def MostrarInformacion(self):
        precio_dolares = self.precio / self.tipoCambioDolar
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares: ${precio_dolares:.2f}. {self.MostrarDisponibilidad()}"
    
    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        precio_con_descuento = self.precio * (1 - self.descuentoAplicado)
        self.DefinirPrecio(precio_con_descuento)
# Proceso
automovil = Automovil()
automovil.DefinirModelo(int(input("Ingrese el año del automóvil: ")))
automovil.DefinirPrecio(float(input("Ingrese el precio del automóvil en quetzales: ")))
automovil.DefinirMarca(input("Ingrese la marca del automóvil: "))
automovil.DefinirTipoCambio(float(input("Ingrese el tipo de cambio actual: ")))

opcion = input("¿Se encuentra disponible? si/no: ")
automovil.CambiarDisponibilidad() if opcion.lower() == 'si' else None

opcion_descuento = input("¿Desea aplicar un descuento? si/no: ")
if opcion_descuento.lower() == 'si':
    descuento = float(input("Ingrese la cantidad de descuento: "))
    automovil.AplicarDescuento(descuento / 100)

# Salida
print("\nInformación del automóvil:")
print(automovil.MostrarInformacion())
