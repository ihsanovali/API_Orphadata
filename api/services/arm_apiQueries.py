from datetime import datetime, timedelta
import base64
import hmac
import json
from typing import Dict
import random
import requests
import string
import os
import hashlib

from ..services.arm_settings import APIM_BASE_URL


def generate_token(lifetime: Dict={'minutes': 2}):
    try:
        key = os.getenv('APIM_PK', None).strip()
    except:
        print('No APIM_PK has been found... please check your environment variables relative to Azure API management.\n')
        exit()    

    uid = "integration"
    end_date = datetime.now() + timedelta(**lifetime)
    expiry = f'{end_date.isoformat()}0Z'
    chained_message = f'{uid}\n{expiry}'

    signature = (
        base64.b64encode(
            hmac.new(
                bytearray(key, "utf-8"), 
                bytearray(chained_message,"utf-8"), 
                hashlib.sha512).digest()
        )
    ).decode("utf-8")
    token = f"SharedAccessSignature uid={uid}&ex={expiry}&sn={signature}"

    return token


def create_user(user_contract: Dict):
    """Creates a new user in Azure API management service instance

    Parameters
    ----------
    user_contract: Dict
        Allowed keys are:
            email (mandatory): string
                user email address 
            password (optional): string
                user password
            firstName (mandatory): string
                user firstname
            lastName (mandatory) : string
                user mandatory
            notify (optional): boolean - default=True
                True to send a notification to the user after account creation, False otherwise
    """
    token = generate_token()
    userId = ''.join(random.choices(string.ascii_letters + string.digits + '-', k=26))

    data = {"properties": user_contract}

    URL = APIM_BASE_URL + 'users/{}?api-version=2021-08-01'.format(userId)

    headers = {
        "Content-Type": 'application/json',
        "Authorization": '{}'.format(str(token))
    }
    response = requests.put(url=URL, data=json.dumps(data), headers=headers)

    return response.json()


def authenticate_user(email: str, password: str):
    credentials = base64.b64encode(bytearray('{}:{}'.format(email, password), "utf-8")).decode('utf-8')

    headers = {
        "Content-Type": 'application/json',
        "Authorization": 'Basic {}'.format(credentials)
    }

    URL = APIM_BASE_URL + 'identity?api-version=2021-08-01'
    response = requests.get(URL, headers=headers)

    try:
        response_data = {
            'authenticated': True,
            'sasToken': response.headers.get("Ocp-Apim-Sas-Token"),
            'userId': response.json()['id']
        }
        return response_data
    except:
        return {'authenticated': False, 'error': {'code': response.status_code}}


def get_shared_access_token(user_id) -> Dict:
    token = generate_token()
    end_date = datetime.now() + timedelta(hours=12)

    data = {
        "properties": {
            "keyType": "primary",
            "expiry": f'{end_date.isoformat()}0Z'
        }
    }

    URL = APIM_BASE_URL + 'users/{}/token?api-version=2021-08-01'.format(user_id)

    headers = {
        "Content-Type": 'application/json',
        "Authorization": '{}'.format(str(token))
    }
    response = requests.post(url=URL, data=json.dumps(data), headers=headers)

    return response.json()


def get_product(product_id: str):
    token = generate_token()

    URL = APIM_BASE_URL + 'products/{}?api-version=2021-08-01'.format(product_id)

    headers = {
        "Content-Type": 'application/json',
        "Authorization": '{}'.format(str(token))
    }
    response = requests.get(url=URL, headers=headers)
    return response.json()
