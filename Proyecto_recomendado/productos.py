#Data quemada diccionario
productos = {
    1: {"nombre": "Manzana", "precio": 500, "stock": 100},
    2: {"nombre": "Pera", "precio": 600, "stock": 100},
    3: {"nombre": "Sandia", "precio": 700, "stock": 100},
    4: {"nombre": "Melon", "precio": 800, "stock": 100},
    5: {"nombre": "Naranja", "precio": 900, "stock": 100},
    6: {"nombre": "Mango", "precio": 1000, "stock": 100},
    7: {"nombre": "Banano", "precio": 1100, "stock": 100},
    8: {"nombre": "Papaya", "precio": 1200, "stock": 100},
    9: {"nombre": "Aguacate", "precio": 1300, "stock": 100},
    10: {"nombre": "Fresa", "precio": 1400, "stock": 100},
    11: {"nombre": "Cereza", "precio": 1500, "stock": 100},
    12: {"nombre": "Uva", "precio": 1600, "stock": 100},
    13: {"nombre": "Kiwi", "precio": 1700, "stock": 100},
    14: {"nombre": "Granadilla", "precio": 1800, "stock": 100},
    15: {"nombre": "Maracuya", "precio": 1900, "stock": 100},
    16: {"nombre": "Limon", "precio": 2000, "stock": 100},
    17: {"nombre": "Mandarina", "precio": 2100, "stock": 100},
    18: {"nombre": "Durazno", "precio": 2200, "stock": 100},
    19: {"nombre": "Coco", "precio": 2300, "stock": 100},
    20: {"nombre": "Papaya", "precio": 2400, "stock": 100},
}

#Función para buscar productos por nombre

'''
def buscar_por_nombre(nombre):
    resultado = []
    for id_prod, producto in productos.items():
        if nombre.lower() in producto["nombre"].lower():
            resultado.append((id_prod, producto["nombre"], producto["precio"], producto["stock"]))
    return resultado
'''
#Historial de ventas
historial_ventas = []

#Función para obtener el producto
def obtener_producto(id_prod):
    '''retorna un producto por su id'''
    return productos.get(id_prod, None) #get() es capturar se usa para capturar un valor de un diccionario pero se puede utilizar para cualquier objeto iterable

#Función para calcular el total de la compra
def calcular_total(lista_productos):
    '''retorna el total de la compra'''
    total = 0
    for producto in lista_productos:
            total += producto["precio"] 
    return total

#Funcion para agregar producto
def agregar_producto(id_prod, cantidad, lista_productos):
    '''agrega un producto a la lista de productos'''
    producto = obtener_producto(id_prod)
    if producto:
        lista_productos.append({"id_prod": id_prod, "nombre": producto["nombre"], "precio": producto["precio"]* cantidad})
        
        #Registrar venta en el historial
        historial_ventas.append({
             "Peoducto": producto["Nombre"],
             "Cantidad": cantidad,
             "Total": producto["precio"]* cantidad
             })
    else:
         raise ValueError(f"Producto con ID {id_prod} no encontrado")
    

#Función para actualizar el stock
'''def actualizar_stock(lista_productos):
    actualiza el stock de los productos
    for producto in lista_productos:
        productos[producto["id_prod"]]["stock"] -='''