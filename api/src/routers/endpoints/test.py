from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test():
    return {"teste": "testado!"}