# LegalEase

**LegalEase** is a containerized microservice application that leverages Google’s Gemini AI to dynamically draft professional legal documents based on user specifications. It features a responsive web interface built with Streamlit, a robust FastAPI backend, and multi-format export capabilities (TXT, Branded PDF, and DOCX with automated tables).

---

## 🏗️ Architecture & Tech Stack

*   **Frontend:** Streamlit (Python UI framework)
*   **Backend:** FastAPI (Python asynchronous API framework)
*   **AI Engine:** Google GenAI SDK using `gemini-3.1-flash-lite`
*   **Document Generation & Styling:** 
    *   `python-docx` (Word document structuring, custom image scaling, and table generation)
    *   `FPDF` (Branded PDF exports with custom header/footer layout)
*   **Containerization:** Docker & Docker Compose

---

## 📂 Project Directory Structure

```text
LegalEase/
│
├── aicore/
│   └── gemini_generator.py    # Core logic interacting with Gemini AI
├── legalEaseAPI/
│   └── routes.py              # FastAPI endpoints (/generate)
├── frontend/
│   └── app.py                 # Streamlit user interface & export handlers
├── Image/
│   └── Logo.jpg               # Company branding logo
├── Dockerfile                 # Container build instructions
├── docker-compose.yml         # Multi-container orchestration
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables (API keys)
create a ".env" 
create a var "GEMINI_API_KEY"
add your api to "GEMINI_API_KEY"


Setup and Installation
Prerequisites
Docker and Docker Compose installed on your system.

A valid Google Gemini API Key.

Step-by-Step Deployment
Clone the Repository:

Bash
git clone [https://github.com/your-username/LegalEase.git](https://github.com/your-username/LegalEase.git)
cd LegalEase
Configure Environment Variables:
Create a file named .env in the root directory of the project and add your Gemini API key:

Code snippet
GEMINI_API_KEY=your_actual_gemini_api_key_here
Build and Run with Docker:
Execute the following command to spin up both the FastAPI backend and Streamlit frontend containers:

Bash
docker compose up --build
Access the Application:

Streamlit Frontend UI: Open your browser and navigate to http://localhost:8501

FastAPI Backend Docs: View Swagger documentation at http://localhost:8000/docs

🚀 Key Features
AI Legal Drafting: Enter document types, parties involved, effective dates, and custom terms to instantly generate legally structured agreements using gemini-3.1-flash-lite.

Live Text Editing: Review and modify the AI-generated contract text directly within the Streamlit workspace prior to downloading.

Multi-Format Export:

Plain Text (.TXT): Instant raw export of the agreement.

Word (.DOCX): Styled document embedded with your company logo and an automatically formatted grid table containing your key terms.

PDF (.PDF): Cleanly formatted formal legal layout featuring custom header images and footer copyright notices.

🛡️ Environment & Security Notes
For security best practices, the .env file is excluded from version control via .gitignore.

When deploying or cloning the project to a new environment, ensure the .env file is manually recreated with valid API credentials.