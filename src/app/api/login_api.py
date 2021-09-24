from fastapi import APIRouter, HTTPException, Path
# from src.app.api.models import User
from app.api.models import User

router = APIRouter()


@router.post("/devops-system/login")
async def ops_login(request: User):
    # hard code a token at response, just to make the workflow happy
    resp = {
            "data": {
                "token": "1234"
                },
            "flag": True
            }
    return resp