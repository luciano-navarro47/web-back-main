import os
import jwt
from jwt import ExpiredSignatureError, PyJWTError
from uuid import uuid4
from datetime import datetime, timedelta

secret_key = str(os.getenv('SECRET_KEY'))

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
    print(token)
    return token

def decode_token(token):
    decoded_token = jwt.decode(token, secret_key, algorithms='HS256')
    return decoded_token


def verify_token(token):
    try:
        verified_token = decode_token(token)
        if(verified_token != None):
            print("Verified token")
        else:
            new_token = generate_jwt()
            verified_token = decode_token(new_token)          
        return verified_token
    except (ExpiredSignatureError, PyJWTError) as err:
        print(err) 


# TODO: Refactorize code
