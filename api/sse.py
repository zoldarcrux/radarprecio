from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
app = FastAPI()

@app.get("/")
def hello():  # en sse.py: def sse(); en callback.py: async def oauth_callback(request)
    return PlainTextResponse("ok")
