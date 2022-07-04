from fastapi import FastAPI
from server.models.routes.student import router as StudentRouter

app = FastAPI()

@app.get('/',tags=['root'])
async def read_root():
    return{"Message":"Hello from async FastAPI"}
    
app.include_router(StudentRouter, tags=['Student'], prefix='/student')