from fastapi import FastAPI
from pydantic import BaseModel
import openai
import uvicorn

app = FastAPI()

openai.organization = ''
openai.api_key = 's'

class Palabra(BaseModel):
    palabra: str

def invertir_palabra(palabra):
    if len(palabra) <= 1:
        return palabra
    else:
        primera_letra = palabra[0]
        ultima_letra = palabra[-1]
        letras_medias = palabra[1:-1]
        palabra_invertida = ultima_letra + letras_medias + primera_letra
        return palabra_invertida

@app.post('/invertir')
def invertir_texto(palabra: Palabra):
    prompt = palabra.palabra

    respuesta = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Invierte la primera letra y la última letra de la palabra"},
            {"role": "user", "content": prompt}
        ]
    )

    respuesta_invertida = invertir_palabra(respuesta.choices[0].message.content)

    return {'resultado': respuesta_invertida}

if __name__ == '__main__':
    uvicorn.run(app, host='128.0.0.1', port=8001)
