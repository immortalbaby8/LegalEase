import os 
import google.generativeai as genai

class GeminiDocumentGenerator:
    def __init__(self,model_name="gemini-3.1-flash-lite"):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    def generate_document(self,document_type,parties,terms,dates):
        prompt = f"write a {document_type} document for the following parties: {parties}. Include the following terms: {terms}. Ensure that the document is professional, clear, and structured. The relevant dates are: {dates}."
        response = self.model.generate_content(prompt)
        return response.text