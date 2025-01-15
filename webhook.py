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
        response_text = "saludo desde webhook"
    elif intent == "Despedida":
        response_text = "saludo desde webhook"
    elif intent == "weswes":
        response_text = "wuut?"
    else:
        response_text = f"llegué con {intent}."
    
    # Crear respuesta en el formato requerido por Dialogflow
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == "__main__":
    app.run(debug=True)
