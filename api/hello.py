from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
app = FastAPI()

@app.get("/")
def hello():
    return PlainTextResponse("ok")
