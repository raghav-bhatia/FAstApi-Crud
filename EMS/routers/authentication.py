from fastapi import APIRouter
from .. import schemas

router=APIRouter(
    tags=['Authenticate']
)

@router.post('/login')
def login(request:schemas.Login):
    return request