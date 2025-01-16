from flask import Flask, request, jsonify

app = Flask(__name__)

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
    if 'producto' in parameters:
        producto = parameters.get('producto')  # Aquí 'producto' es el nombre del argumento en Dialogflow
    else:
        producto = None
        
    if 'categoria' in parameters:
        categoria = parameters.get('categoria')  # Aquí 'categoria' es el nombre del argumento en Dialogflow
    else:
        categoria = None
    
    # Manejar las intenciones y argumentos
    if intent == "Producto":
        response_text = f"1.- tu intento es {intent} y el producto es {producto}."
    elif intent == "Categoria":
        response_text = f"2.- tu intento es {intent} y la categoría es {categoria}."
    else:
        response_text = f"El nombre de tu intento es --> {intent} <--"
    
    # Crear respuesta en el formato requerido por Dialogflow
    return jsonify({
        "fulfillmentText": response_text
    })


if __name__ == "__main__":
    app.run(debug=True)
