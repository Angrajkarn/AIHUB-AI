from firebase_admin import auth
from fastapi import HTTPException, Header

def verify_firebase_token(id_token: str = Header(...)):
    try:
        decoded = auth.verify_id_token(id_token)
        return decoded
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Token")