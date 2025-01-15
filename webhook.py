from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Recibir datos del webhook de Dialogflow
    req = request.get_json(silent=True, force=True)
    print(f"Request JSON: {req}")
    
    # Extraer la intención
    intent = req.get("queryResult").get("intent").get("displayName")
    
    # Manejar las intenciones
    if intent == "Saludo":
        response_text = "¡Hola! ¿Cómo puedo ayudarte hoy?"
    elif intent == "Despedida":
        response_text = "¡Hasta luego! Que tengas un excelente día."
    else:
        response_text = "Lo siento, no entiendo esa petición."
    
    # Crear respuesta en el formato requerido por Dialogflow
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == "__main__":
    app.run(debug=True)
