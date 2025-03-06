# CAJA FRUBER - Frutas y Verduras

Este es un proyecto de una tienda de frutas y verduras que implementa el patrón de diseño **Modelo-Vista-Controlador (MVC)** en Python con Tkinter.

## 📌 Descripción

La aplicación permite:
- Ver productos disponibles con su precio y stock.
- Agregar productos al carrito de compras.
- Finalizar la compra y actualizar el stock.
- Visualizar el historial de ventas.
- Manejar excepciones para evitar errores en la compra.

## 📸 Capturas de Pantalla

![Pantalla Principal](/assets/background.jpg)

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** (Lógica de negocio y estructura del proyecto)
- **Tkinter** (Interfaz gráfica de usuario)
- **ttk** (Themed Tkinter Widgets para mejorar la apariencia)
- **Pillow** (Para manejo de imágenes)

## 📂 Estructura del Proyecto

```
Proyecto_MVC/
│── assets/               # Imágenes y recursos
│── controllers/          # Controladores (Lógica de negocio)
│   └── Controller.py
│── models/               # Modelos (Datos y estructura)
│   └── Model.py
│── views/                # Vistas (Interfaz gráfica)
│   └── View.py
│── main.py               # Punto de entrada de la aplicación
│── README.md             # Documentación del proyecto
```

## 🚀 Instalación y Ejecución

1. **Clona el repositorio**
   ```bash
   git clone 
   cd tu-repositorio
   ```

2. **Instala las dependencias necesarias**
   ```bash
   pip install pillow
   ```

3. **Ejecuta la aplicación**
   ```bash
   python main.py
   ```

## ✨ Funcionalidades

1. **Interfaz gráfica con Tkinter**
   - Lista de productos con nombre, precio y stock.
   - Campo de entrada para la cantidad de productos.
   - Botones para agregar al carrito, finalizar compra y ver historial de ventas.
   - Sección donde se muestra el total acumulado de la compra.

2. **Selección y compra de productos**
   - Permite seleccionar productos de una lista y especificar la cantidad a comprar.
   - Verifica la disponibilidad antes de agregar al carrito.
   - Actualiza el total de la compra en tiempo real.

3. **Finalización de compra y recibo**
   - Al presionar "Finalizar Compra", se muestra un resumen con los productos adquiridos y el total a pagar.
   - Se registra la venta y se actualiza el stock.
   - Se limpia el carrito de compras después de finalizar la compra.

4. **Historial de ventas**
   - Se muestra el historial de compras realizadas con:
     - Nombre del producto.
     - Cantidad vendida.
     - Precio total.
   - Se muestra la ganancia total acumulada.

5. **Manejo de excepciones**
   - Evita la selección de productos sin especificar cantidad.
   - Valida que solo se ingresen números en el campo de cantidad.
   - No permite comprar más unidades de las disponibles.
   - Muestra mensajes de error cuando se detectan operaciones incorrectas.

## 👤 Autores

- ** Cristhian Javier Garzon - Diego Fernando Chacón**
- 📧 Contacto: [---](---)
- 🌐 GitHub: [--](--)