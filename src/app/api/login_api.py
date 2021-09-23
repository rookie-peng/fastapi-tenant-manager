from fastapi import APIRouter, HTTPException, Path


router = APIRouter()


@router.post("/devops-system/login")
def ops_login(request):
    # hard code a token at response, just to make the workflow happy
    resp = {
            "data": {
                "token": "1234"
                },
            "flag": True
            }
    return resp