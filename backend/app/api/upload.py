from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def upload_pdf():
    return {"message": "upload endpoint — coming soon"}
