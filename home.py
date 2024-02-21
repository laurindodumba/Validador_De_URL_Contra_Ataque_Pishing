from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, HTMLResponse
from pathlib import Path
import joblib
from pydantic import BaseModel

app = FastAPI()

# Carregamento do modelo salvo em pkl
phish_model = open('phishing_model/phishing.pkl', 'rb')
phish_model_ls = joblib.load(phish_model)


# Definir o formato dos dados de entrada usando o Pydantic BaseModel
class URL(BaseModel):
    url: str

# Rota da API
@app.post('/predict/')
async def predict(url: URL):
    feature = url.url
    X_predict = [feature]
    y_Predict = phish_model_ls.predict(X_predict)
    result = "Alerta! Este é um ataque de Phishing." if y_Predict[0] == 'bad' else "Fique tranquilo! Este não é um ataque de Phishing."
    return {'url': feature, 'result': result}

# Rota para servir o arquivo index.html
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_path = Path(__file__).parent / "static" / "index.html"
    if not index_path.is_file():
        raise HTTPException(status_code=404, detail="Arquivo HTML não encontrado")
    return StreamingResponse(index_path.open('rb'))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
