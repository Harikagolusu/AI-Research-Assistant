from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()


def create_vector_store(chunks):

    try:

        embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

        vector_store = FAISS.from_texts(
            chunks,
            embedding=embeddings
        )

        vector_store.save_local("faiss_index")

        return vector_store

    except Exception as e:
        print("VECTOR STORE ERROR:", e)
        return None