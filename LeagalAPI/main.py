import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
class RequestBody(BaseModel):
    doc_type: str
    detials: str
app = FastAPI()
@app.post("/generate")
def gen_doc(request: RequestBody):
    try:
        model = genai.GenerativeModel("gemini-3.1-flash-lite")
        promt = f" Act as an expert legal assistant. Generate a {request.doc_type} document with the following details: {request.detials}. Make it professional, clear, and structured"
        response = model.generate_content(promt)
        return {"document": response.text}
    except Exception as e:
        return {"error": str(e)}
    