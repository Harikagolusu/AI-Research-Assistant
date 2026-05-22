from fastapi import APIRouter, UploadFile, File
from app.utils.pdf_utils import extract_text_from_pdf
from app.utils.chunk_utils import create_chunks
from app.utils.vector_store import create_vector_store
import os

router = APIRouter()

UPLOAD_FOLDER = "app/data"


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # Create chunks
    chunks = create_chunks(extracted_text)

    vector_store = create_vector_store(chunks)

    if vector_store:

        return {
            "message": f"{file.filename} uploaded successfully",
            "total_chunks": len(chunks),
            "vector_store_created": True
    }

    else:

        return {
            "message": "Vector store creation failed"
        }