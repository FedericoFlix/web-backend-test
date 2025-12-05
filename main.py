from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "Servidor funcionando correctamente"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}
