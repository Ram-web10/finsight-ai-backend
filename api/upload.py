from fastapi import APIRouter, UploadFile, File
import shutil
import os
import uuid

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        return {
            "error": "Only PDF files are allowed."
        }

    try:

        unique_filename = f"{uuid.uuid4()}_{file.filename}"

        filepath = os.path.join(
            UPLOAD_FOLDER,
            unique_filename
        )

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {

            "message": "Upload Successful",

            "filename": file.filename,

            "stored_filename": unique_filename,

            "pdf_path": filepath

        }

    except Exception as e:

        return {

            "error": str(e)

        }