from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/api/sse")
async def sse():
    return PlainTextResponse("RadarPrecio MCP placeholder activo")
