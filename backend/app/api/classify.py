from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def classify_pdf():
    return {"message": "classify endpoint — coming soon"}
