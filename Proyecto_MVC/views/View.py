import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class ViewShopping:
    def __init__(self, controller):
        self.controller = controller
        self.controller.view = self
        self.window = tk.Tk()
        self.window.title("CAJA FRUBER - Frutas y Verduras")
        self.window.geometry("800x600")

        self.bg_image = Image.open('./assets/background.jpg')
        self.bg_image = self.bg_image.resize((800, 600), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        self._configurar_interfaz()
        self._cargar_productos()

        self.window.mainloop()

    def _configurar_interfaz(self):
        self.treeview_products = ttk.Treeview(self.window, columns=("Nombre", "Precio", "Stock"), show="headings")
        self.treeview_products.heading("Nombre", text="Nombre")
        self.treeview_products.heading("Precio", text="Precio")
        self.treeview_products.heading("Stock", text="Stock")

        self.entry_quantity = tk.Entry(self.window)
        self.button_add_product = tk.Button(self.window, text="Agregar Producto", command=self.agregar_producto)
        self.button_finish = tk.Button(self.window, text="Finalizar Compra", command=self.controller.finish_shopping)
        self.etiqueta_total = tk.Label(self.window, text="Total: $0.00")
        
        self.canvas.create_window(400, 150, window=self.treeview_products)
        self.canvas.create_window(400, 350, window=self.entry_quantity)
        self.canvas.create_window(400, 400, window=self.button_add_product)
        self.canvas.create_window(400, 450, window=self.button_finish)
        self.canvas.create_window(400, 500, window=self.etiqueta_total)

    def _cargar_productos(self):
        for id_producto, product in self.controller.get_products().items():
            self.treeview_products.insert("", "end", iid=str(id_producto), values=(product.nombre, product.precio, product.stock))

    def agregar_producto(self):
        try:
            selected_item = self.treeview_products.selection()[0]
            id_producto = int(selected_item)
            quantity = int(self.entry_quantity.get())
            self.controller.add_to_cart(id_producto, quantity)
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def actualizar_vista_productos(self):
        for row in self.treeview_products.get_children():
            self.treeview_products.delete(row)
        for id_producto, product in self.controller.get_products().items():
            self.treeview_products.insert("", "end", iid=str(id_producto), values=(product.nombre, product.precio, product.stock))
        total = self.controller.calculate_total()
        self.etiqueta_total.config(text=f"Total: ${total}")

    def reset_total(self):
        self.etiqueta_total.config(text="Total: $0.00")
