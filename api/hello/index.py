from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")             # cuando Vercel normaliza a "/"
@app.get("/api/hello")    # cuando pasa la ruta completa
def hello():
    return PlainTextResponse("ok")
