from fastapi import FastAPI
from src.api.routes import router 
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(router)


@app.get("/")
def root():
    return {"message": "Valura AI Service Running"}