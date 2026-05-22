from fastapi import FastAPI
from app.services.gemini_service import ask_gemini
from app.routes.pdf_routes import router as pdf_router
from app.services.rag_service import ask_pdf_question

app = FastAPI(
    title="AI Research Assistant",
    description="RAG-based Multi PDF Conversational AI System",
    version="1.0"
)

app.include_router(pdf_router)

@app.get("/")
def home():
    return {
        "message": "AI Research Assistant Backend Running"
    }


@app.get("/ask")
def ask(question: str):

    answer = ask_gemini(question)

    return {
        "question": question,
        "answer": answer
    }

@app.get("/ask-pdf")
def ask_pdf(question: str):

    response = ask_pdf_question(question)

    return response