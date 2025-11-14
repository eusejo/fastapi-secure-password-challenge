from fastapi import APIRouter
from services.gerenatePassword import gerador

router = APIRouter()

@router.get('/genpassword')
async def genpassword():
    password = gerador()
    
    return {
        "password" : password
    }