from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def search_pdf():
    return {"message": "search endpoint — coming soon"}
