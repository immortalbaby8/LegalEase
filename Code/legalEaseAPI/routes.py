from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from aicore.gemini_generator import GeminiDocumentGenerator

router = APIRouter()
generator = GeminiDocumentGenerator()

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

@router.post("/generate")
def create_document(request: DocumentRequest):
    result = generator.generate_document(
        document_type=request.document_type,
        parties=request.parties,
        terms=request.terms,
        dates=request.dates
    )
    return {"document": result}