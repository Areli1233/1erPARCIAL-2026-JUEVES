import datetime
class ProductoKwikE:

    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock, categoria=None):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def cambiar_datos(self, descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def dias_para_expirar(self, fecha_referencia=None):
        if fecha_referencia is None:
            fecha_referencia = datetime.date.today()
        dias = (self.fecha_vencimiento - fecha_referencia).days
        if dias < 0:
            print("El producto '" + self.descripcion + "' ya expiro hace " + str(-dias) + " dias. Stock en 0.")
            self.stock = 0
            return 0
        return dias

    #ESTO ES PARTE DEL EJERCICIO 6
    def __str__(self):
        return ("Producto: " + self.descripcion + " | ID: " + str(self.id_producto) +
            " | Precio: $" + format(self.precio, ".2f") +
            " | Stock: " + str(self.stock))

    def __eq__(self, otro):
        if not isinstance(otro, ProductoKwikE):
            return False
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion

p1 = ProductoKwikE("Donuts Glaseadas", 123, datetime.date(2026, 10, 20), 1.50, 50, "Panaderia")
p2 = ProductoKwikE("Leche Entera", 456, datetime.date(2026, 9, 15), 2.25, 30, "Lacteos")
referencia = datetime.date(2026, 10, 1)
print(p1)
p1.cambiar_datos(precio=1.75, stock=40)
print(p1)
print(p1.dias_para_expirar(referencia))   
print(p2.dias_para_expirar(referencia)) 
print(p2.stock)
