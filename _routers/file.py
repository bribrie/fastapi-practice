from typing import Annotated
from fastapi import File, UploadFile, Form, APIRouter

router = APIRouter()

@router.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

# Optional File Upload
# @router.post("/uploadfile/")
# async def create_upload_file(file: UploadFile | None = None):
#     return {"filename": file.filename}

# UploadGile with Additional Metadata
@router.post("/uploadfile/")
async def create_upload_file(file: Annotated[UploadFile, File(description="A file read as UploadFile")]):
    return {"filename": file.filename}

# Multiple File Uploads
@router.post("/multi-files/")
async def create_files(files: Annotated[list[bytes], File(description="Multiple files as bytes")]):
    return {"multi_file_sizes": [len(file) for file in files]}

@router.post("/multi-uploadfiles/")
async def create_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}

# Request Forms and Files
@router.post("/files-form/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()]
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type
    }