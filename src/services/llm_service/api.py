from fastapi import FastAPI, HTTPException
from .model_manager import ModelManager

app = FastAPI()
model_manager = ModelManager()

@app.post("/generate")
async def generate_text(prompt: str):
    try:
        response = model_manager.generate(prompt)
        return {"generated_text": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
