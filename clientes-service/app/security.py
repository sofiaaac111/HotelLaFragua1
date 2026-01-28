from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
security = HTTPBearer()

SECRET_KEY = "hotel_lafragua_123"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload   
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

def require_admin(user=Depends(get_current_user)):
    if user["rol"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="No autorizado: solo administradores"
        )
    return user