from Proyecto_recomendado.productos import obtener_producto

def calcular_total(lista_productos):
    '''retorna el total de la compra'''
    total = 0  # inicializamos el total en 0
    for producto in lista_productos:
            total += producto["precio"] 
    return total
def agregar_producto(id_prod, cantidad, lista_productos):
    '''agrega un producto a la lista de productos'''
    producto = obtener_producto(id_prod)
    if producto:
        lista_productos.append({"id_prod": id_prod, "nombre": producto["nombre"], "precio": producto["precio"]* cantidad})
    else:
        raise ValueError(f"Producto con ID {id_prod} no encontrado")