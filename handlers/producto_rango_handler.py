import requests

def productos_rango(valor1, valor2):
    url = "https://riccos.somee.com/api/Producto?activo=true&disponible=true"
    response = requests.get(url)
    
    if response.status_code == 200:
        productos = response.json()  # Lista de productos
        
        # Filtrar productos según el rango de precios
        if valor1 is None or valor2 is None:
            return "Por favor, proporciona un rango de precios válido."
        
        # Asegurarse de que valor1 sea el menor y valor2 el mayor
        if valor1 > valor2:
            valor1, valor2 = valor2, valor1
        
        productos_filtrados = [
            producto for producto in productos 
            if valor1 <= producto['precio'] <= valor2
        ]
        
        # Si no hay productos dentro del rango
        if not productos_filtrados:
            return f"No se encontraron productos en el rango de {valor1} a {valor2}."

        # Crear una respuesta con los productos encontrados
        response_text = f"Productos en el rango de {valor1} a {valor2}:\n"
        for producto in productos_filtrados:
            response_text += f"- {producto['nombre']} - {producto['precio']} soles\n"
            response_text += f"  Descripción: {producto['descripcion']}\n"
            response_text += f"  Imagen: {producto['urlImagen']}\n\n"
        
        return response_text
    else:
        return "Hubo un problema al consultar los productos. Por favor, intenta más tarde."
