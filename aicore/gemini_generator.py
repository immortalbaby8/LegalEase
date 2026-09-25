import os 
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiDocumentGenerator:
    def __init__(self, model_name="gemini-3.1-flash-lite"):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(model_name)
        
    def generate_document(self, document_type, parties, terms, dates):
        prompt = (
            f"Generate a comprehensive legal document titled '{document_type}'\n"
            f"Involved parties: {parties}\n"
            f"Effective Date: {dates}\n"
            f"Terms and conditions: {terms}\n"
            "Ensure formal legal structure with multiple sections and legal clauses."
        )
        response = self.model.generate_content(prompt)
        return response.text