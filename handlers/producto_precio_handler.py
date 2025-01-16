import requests

def producto_precio(producto):
    if producto:
        # Realizamos una solicitud a la API para obtener los productos disponibles
        url = "https://riccos.somee.com/api/Producto?activo=true&disponible=true"
        response = requests.get(url)
        
        if response.status_code == 200:
            productos = response.json()  # Lista de productos
            
            # Buscamos el producto que coincida con el nombre solicitado
            for item in productos:
                if producto.lower() in item['nombre'].lower():
                    # Si se encuentra el producto, devolver detalles
                    nombre_producto = item['nombre']
                    descripcion = item['descripcion']
                    precio = item['precio']
                    urlImagen = item['urlImagen']

                    return f"El producto '{nombre_producto}' tiene un precio de {precio}. Descripción: {descripcion} >>{urlImagen}<<"
            
            # Si no se encuentra el producto específico
            return f"Lo lmentamos, el producto '{producto}' no se encuentra disponible."
        else:
            return "Hubo un problema al consultar los productos. Por favor, intenta más tarde."
    else:
        return "No se especificó un producto."
