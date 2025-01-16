from flask import Flask, request, jsonify

app = Flask(__name__)

# Función para manejar la intención "Producto"
def manejar_producto(producto):
    if producto:
        return f"1.- tu intento es Producto y el producto es {producto}."
    else:
        return "No se especificó un producto."

# Función para manejar la intención "Categoria"
def manejar_categoria(categoria):
    if categoria:
        return f"2.- tu intento es Categoria y la categoría es {categoria}."
    else:
        return "No se especificó una categoría."

# Función para manejar otras intenciones generales
def manejar_intencion_generica(intent, producto):
    return f"Intento --> {intent} <-- /// Parametro -->{producto}<--"

@app.route('/webhook', methods=['POST'])
def webhook():
    # Recibir datos del webhook de Dialogflow
    req = request.get_json(silent=True, force=True)
    print(f"Request JSON: {req}")
    
    # Extraer la intención
    intent = req.get("queryResult").get("intent").get("displayName")
    
    # Extraer los parámetros de la solicitud (los argumentos enviados desde Dialogflow)
    parameters = req.get("queryResult").get("parameters")
    
    # Ahora puedes capturar los valores de los parámetros de acuerdo a la estructura de tu intent
    producto = parameters.get('producto') if 'producto' in parameters else None
    categoria = parameters.get('categoria') if 'categoria' in parameters else None
    
    # Manejar las intenciones y argumentos, llamando a las funciones correspondientes
    if intent == "Producto":
        response_text = manejar_producto(producto)
    elif intent == "Categoria":
        response_text = manejar_categoria(categoria)
    else:
        response_text = manejar_intencion_generica(intent, producto)
    
    # Crear respuesta en el formato requerido por Dialogflow
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == "__main__":
    app.run(debug=True)
