from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import upload, search, classify

app = FastAPI(
    title="DocLens",
    description="Upload any PDF. Ask anything. Get answers — not just keywords.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api/upload", tags=["upload"])
app.include_router(search.router, prefix="/api/search", tags=["search"])
app.include_router(classify.router, prefix="/api/classify", tags=["classify"])


@app.get("/")
def health_check():
    return {"status": "ok", "app": "DocLens"}
