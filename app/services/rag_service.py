from app.utils.retrieval import load_vector_store
from app.services.gemini_service import ask_gemini


def ask_pdf_question(question):

    vector_store = load_vector_store()

    docs = vector_store.similarity_search(question, k=5)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are an AI Research Assistant.

    Answer the question ONLY using the provided context.

    If the answer is not present in the context, say:
    "I could not find the answer in the uploaded document."

    Do NOT use external knowledge.
    Do NOT guess.
    Do NOT make assumptions.

    Context:
    {context}

    Question:
    {question}
    """

    answer = ask_gemini(prompt)

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": len(docs)
    }