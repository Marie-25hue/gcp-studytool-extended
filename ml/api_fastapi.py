from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

# Cargar modelo y vectorizador
modelo = joblib.load('modelo_clasificador.pkl')
vectorizer = joblib.load('vectorizer.pkl')

class TextoRequest(BaseModel):
    texto: str

@app.post("/clasificar")
def clasificar_texto(request: TextoRequest):
    vector = vectorizer.transform([request.texto])
    prediccion = modelo.predict(vector)
    return {"categoria": prediccion[0]}

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API de clasificación activa"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
