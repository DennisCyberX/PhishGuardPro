from fastapi import FastAPI
from .detection import analyze_url
from .authentication import authenticate_user

app = FastAPI()

@app.post("/analyze")
async def analyze(url: str):
    result = analyze_url(url)
    return {"status": "success", "result": result}

@app.post("/login")
async def login(username: str, password: str):
    user = authenticate_user(username, password)
    return {"status": "success", "user": user}
