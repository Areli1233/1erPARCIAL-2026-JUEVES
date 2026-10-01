class KwikEMart:
    def __init__(self):
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []

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
        lista.append(producto)
        return True

    def remover_producto(self, pasillo, id_producto):
        lista = self._obtener_pasillo(pasillo)
        if lista is None:
            return False
        for producto in lista:
            if producto.id_producto == id_producto:
                lista.remove(producto)
                return True
        return False


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
            for producto in list(lista):
                dias = (producto.fecha_vencimiento - fecha_referencia).days
                if dias <= 1:
                    lista.remove(producto)
                    total += 1
        return total


    def mostrar_mercado(self):
        for nombre, lista in (("Bebidas", self.bebidas),("Snacks", self.snacks),("Conveniencia", self.conveniencia)):
            print(" ", nombre + ":")
            if len(lista) == 0:
                print("    (vacio)")
            for p in lista:
                print("    " + str(p))



