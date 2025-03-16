import httplib
import json

API_HOST = "api.deepseek.com"  
API_KEY = "sk-53751d5c6f344a5dbc0571de9f51313e"  
ENDPOINT = "/v1/chat/completions" 

PROMPT_INICIAL = "Eres un asistente virtual que responde con la personalidad del guerrero sun tzu, creador del arte de la guerra. entrega las respuestas codificadas en UTF-8."
def obtener_respuesta(mensaje):
    conn = httplib.HTTPSConnection(API_HOST)
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY
    }
    
    data = json.dumps({
        "model": "deepseek-chat",  # Ajusta segun el modelo disponible
        "messages": [
            {"role": "system", "content": PROMPT_INICIAL}, 
            {"role": "user", "content": mensaje}
        ]
    }ensure_ascii=False)
    
    conn.request("POST", ENDPOINT, body=data.encode('utf-8'), headers=headers)
    response = conn.getresponse()
    
    if response.status == 200:
        respuesta_json = json.loads(response.read().decode('utf-8'))
        return respuesta_json["choices"][0]["message"]["content"]
    else:
        return "Error al obtener respuesta de la API."

def chatbot():
    print("Hola! Soy tu chatbot de DeepSeek. Escribe un mensaje o 'salir' para terminar.")
    
    while True:
        user_input = raw_input("\n\nTu: ").strip().decode('utf-8')  # raw_input() es para Python 2.7
        
        if user_input.lower() == "salir":
            print("Chatbot: Hasta luego!")
            break
        
        respuesta = obtener_respuesta(user_input)
        print("\n\nChatbot:", respuesta.encode('utf-8'))

chatbot()

