from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def sse():
    return PlainTextResponse("RadarPrecio SSE activo")
