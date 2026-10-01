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