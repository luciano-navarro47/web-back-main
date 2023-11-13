import json
from utils import generate_jwt, verify_token

def validate_user_token(token):

    if token != None:
        validated_token = verify_token(token)
        return validated_token
    else:
        new_token = generate_jwt()
        validated_token = verify_token(new_token)
        return validated_token 


def lambda_handler(event: dict, context):

    try:
        if not 'Authorization' in event['headers'] or event['headers']['Authorization'] == '':
            validated_decoded_token = validate_user_token(None)
        else:
            validated_decoded_token = validate_user_token(event['headers']['Authorization'])
    except:
        raise Exception('Unauthorized')
        
    return {
        "statusCode": 200,
        "body": json.dumps(validated_decoded_token), 
        "isBase64Encoded": False
    }


    
