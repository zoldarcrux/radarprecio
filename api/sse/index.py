from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
@app.get("/api/sse")
def sse():
    return PlainTextResponse("RadarPrecio SSE activo")
