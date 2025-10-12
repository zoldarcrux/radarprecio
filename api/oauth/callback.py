from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
app = FastAPI()

@app.get("/")
async def oauth_callback(request: Request):
    code = request.query_params.get("code", "")
    return PlainTextResponse(f"Auth code recibido: {code}")
