
class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)

    def __len__(self):
        return self.header._elem

    def esta_vacia(self):
        return self.header._elem == 0

    def agregar(self, dato):
        nuevo = Nodo(dato)
        actual = self.header
        while actual._nxt is not None:
            actual = actual._nxt
        actual._nxt = nuevo
        self.header._elem += 1

    def remover_primero(self, condicion):
        anterior = self.header
        actual = anterior._nxt
        while actual is not None:
            if condicion(actual._elem):
                anterior._nxt = actual._nxt
                self.header._elem -= 1
                return True
            anterior = actual
            actual = actual._nxt
        return False

    def remover_todos(self, condicion):
        removidos = 0
        anterior = self.header
        actual = anterior._nxt
        while actual is not None:
            if condicion(actual._elem):
                anterior._nxt = actual._nxt
                self.header._elem -= 1
                removidos += 1
            else:
                anterior = actual
            actual = actual._nxt
        return removidos

#iteradorr
    def __iter__(self):
        return IteradorListaEnlazada(self)


class IteradorListaEnlazada:
    def __init__(self, lista):
        self._actual = lista.header._nxt

    def __iter__(self):
        return self

    def __next__(self):
        if self._actual is None:
            raise StopIteration
        dato = self._actual._elem
        self._actual = self._actual._nxt
        return dato



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

    def __str__(self):
        return ("Producto: " + self.descripcion + " | ID: " + str(self.id_producto) +
                " | Precio: $" + format(self.precio, ".2f") +
                " | Stock: " + str(self.stock))

    def __eq__(self, otro):
        if not isinstance(otro, ProductoKwikE):
            return False
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion


class KwikEMart:
    def __init__(self):
        self.bebidas = ListaEnlazada()
        self.snacks = ListaEnlazada()
        self.conveniencia = ListaEnlazada()

    def _obtener_pasillo(self, pasillo):
        if pasillo == "Bebidas":
            return self.bebidas
        if pasillo == "Snacks":
            return self.snacks
        if pasillo == "Conveniencia":
            return self.conveniencia
        return None

    def _todos_los_pasillos(self):
        return [self.bebidas, self.snacks, self.conveniencia]

    def buscar_producto(self, id_producto):
        for lista in self._todos_los_pasillos():
            for producto in lista:
                if producto.id_producto == id_producto:
                    return producto
        return None

    def agregar_producto(self, pasillo, producto):
        lista = self._obtener_pasillo(pasillo)
        if lista is None or not isinstance(producto, ProductoKwikE):
            return False
        if self.buscar_producto(producto.id_producto) is not None:
            return False
        lista.agregar(producto)
        return True

    def remover_producto(self, pasillo, id_producto):
        lista = self._obtener_pasillo(pasillo)
        if lista is None:
            return False
        return lista.remover_primero(lambda p: p.id_producto == id_producto)

    def actualizar_stock(self, pasillo, id_producto, nuevo_stock):
        lista = self._obtener_pasillo(pasillo)
        if lista is None or nuevo_stock < 0:
            return False
        for producto in lista:
            if producto.id_producto == id_producto:
                producto.stock = nuevo_stock
                return True
        return False

    def remover_por_expirar(self, fecha_referencia=None):
        if fecha_referencia is None:
            fecha_referencia = datetime.date.today()
        total = 0
        for lista in self._todos_los_pasillos():
            total += lista.remover_todos(
                lambda p: (p.fecha_vencimiento - fecha_referencia).days <= 1)
        return total

    def mostrar_mercado(self):
        for nombre, lista in (("Bebidas", self.bebidas), ("Snacks", self.snacks),
                            ("Conveniencia", self.conveniencia)):
            print(" ", nombre + " (" + str(len(lista)) + "):")
            if lista.esta_vacia():
                print("    (vacio)")
            for p in lista:
                print("    " + str(p))

