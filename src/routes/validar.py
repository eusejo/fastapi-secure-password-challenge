from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from services.passwordValidator import validatePassword

router = APIRouter()

class passwords(BaseModel):
    password: str

@router.post('/validate')
async def validarSenha(password: passwords):
    
    isValid, message = validatePassword(password.password)
    
    if isValid:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=message
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )