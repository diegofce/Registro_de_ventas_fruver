from tkinter import messagebox

class ControllerShopping:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.cart = [] 

    def get_products(self):
        return self.model.products

    def add_to_cart(self, id_prod, quantity):  
        producto = self.model.get_product(id_prod)
        if producto:
            if quantity > producto.stock:
                raise ValueError("Stock insuficiente")
            self.cart.append({"producto": producto.nombre, "cantidad": quantity, "precio_total": producto.precio * quantity})
        else:
            raise ValueError("Producto no encontrado")
        
    def calculate_total(self):
        total = sum(item['precio_total'] for item in self.cart)
        return total

    def finish_shopping(self):
        total = sum(item["precio_total"] for item in self.cart)
        messagebox.showinfo('Compra finalizada', f'Total: {total}')
        for item in self.cart:
            producto_id = next((p_id for p_id, p in self.model.products.items() if p.nombre == item["producto"]), None)
            if producto_id is not None:
                self.model.register_sale(producto_id, item["cantidad"])
            else:
                messagebox.showerror("Error", "Producto no encontrado en la tienda")

        if self.view:
            self.view.actualizar_vista_productos() 
        self.cart.clear()
        self.view.reset_total()

    def get_sales_history(self):
        return self.model.history