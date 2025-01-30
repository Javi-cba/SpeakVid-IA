import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.transcribe_router import router as transcribe_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "¡Hola, mundo!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

app.include_router(transcribe_router, prefix="/api", tags=["transcribe"])

