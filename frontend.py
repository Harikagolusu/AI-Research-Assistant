import streamlit as st
import requests

# Page Config
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
with st.sidebar:

    st.title("📚 AI Research Assistant")

    st.markdown("---")

    st.write("""
    Upload PDFs and ask intelligent questions using RAG architecture powered by Gemini.
    """)

    st.markdown("### ⚡ Features")

    st.write("✅ PDF Upload")
    st.write("✅ Semantic Search")
    st.write("✅ RAG Pipeline")
    st.write("✅ Gemini AI Responses")

    st.markdown("---")

    st.caption("Built with FastAPI + Streamlit + Gemini")

# Main Title
st.title("🤖 AI Research Assistant")

st.write("Ask questions from your uploaded documents.")

st.markdown("---")

# Upload Section
st.subheader("📄 Upload PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type="pdf"
)

if uploaded_file is not None:

    with st.spinner("Processing PDF..."):

        response = requests.post(
            "http://127.0.0.1:8000/upload-pdf",
            files={
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }
        )

    data = response.json()

    st.success(data["message"])

    if "total_chunks" in data:
        st.info(f"Total Chunks Created: {data['total_chunks']}")

st.markdown("---")

# Question Section
st.subheader("💬 Ask Questions")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask AI"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating AI response..."):

            response = requests.get(
                "http://127.0.0.1:8000/ask-pdf",
                params={
                    "question": question
                }
            )

            data = response.json()

        st.markdown("### 🤖 AI Response")

        st.write(data["answer"])

        st.markdown("---")

        st.caption(
            f"Retrieved Chunks: {data['retrieved_chunks']}"
        )