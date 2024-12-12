import openai
import os
import json

# Configura tu clave API de OpenAI de manera más segura
openai.api_key = os.getenv("OPENAI_API_KEY")  # Asegúrate de que la clave esté en un archivo .env

def procesar_texto(texto_usuario, contexto=""):
    """Procesa el texto del usuario y genera una respuesta."""
    prompt = f"{contexto}\nUsuario: {texto_usuario}\nBot:"
    
    try:
        respuesta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        # Se puede actualizar el contexto con la respuesta del bot para mantener la conversación
        contexto += f"\nUsuario: {texto_usuario}\nBot: {respuesta.choices[0].text.strip()}"
        return respuesta.choices[0].text.strip(), contexto
    except openai.OpenAIError as e:
        return f"Error de API: {e}", contexto

# Ejemplo de uso con contexto
texto_usuario = "¿Cómo puedo restablecer mi contraseña?"
respuesta_bot, contexto = procesar_texto(texto_usuario, contexto="")
print(respuesta_bot)
