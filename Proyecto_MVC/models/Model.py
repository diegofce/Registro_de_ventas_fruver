class Product:
    def __init__(self, id_prod, nombre, precio, stock):
        self.id_prod = id_prod
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError('No hay suficiente stock')
        self.stock -= quantity

class Shopping:
    def __init__(self):
        self.products = {}  # Diccionario para almacenar productos por su id
        self.history = []  # Lista para almacenar el historial de ventas

    def add_product(self, id_prod, nombre, precio, stock):
        """Añade un producto a la lista de productos."""
        self.products[id_prod] = Product(id_prod, nombre, precio, stock)  

    def get_product(self, id_prod):
        """Busca un producto por su id y lo retorna."""
        return self.products.get(id_prod, None) 
    
    def register_sale(self, id_prod, quantity):
        """Registra una venta y actualiza el stock del producto."""
        product = self.get_product(id_prod)
        if product:
            product.reduce_stock(quantity)
            total = product.precio * quantity
            self.history.append({
                "Nombre": product.nombre,
                "Cantidad": quantity,
                "Precio_total": total
            })
        else:
            raise ValueError('Producto no encontrado')
