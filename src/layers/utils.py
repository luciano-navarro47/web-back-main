import os
import jwt
from uuid import uuid4
from jwt import ExpiredSignatureError, PyJWTError
from datetime import datetime, timedelta

from dotenv import load_dotenv
load_dotenv()
secret_key = str(os.getenv("SECRET_KEY"))

def generate_jwt():
    
    payload = {
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(days=5),
        "sub": "user",
        "user_id": str(uuid4()),
        "user_fields": {
            "date_joined": str(datetime.now().replace(microsecond=0))
        }
    }

    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def verify_token(token):
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms='HS256')
        if(decoded_token != None):
            return decoded_token
    except (ExpiredSignatureError, PyJWTError) as error:
        token = generate_jwt()
        print(error,'\nNew token created: ', token)
        verified_token = verify_token(token)
        return verified_token

# TODO: Refactorize code
