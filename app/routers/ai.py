from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def process_ai_request():
    return {"message": "AI request received!"}


@router.get("/")
def process_ai_request():
    return {"message": "AI request received!"}
