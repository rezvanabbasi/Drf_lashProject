from utils import *
from config.celery import app


@app.task
def kave_negar_token_send(receptor, token):
    try:
        api = KavenegarAPI(API_KEY)
        params = {
            'receptor': receptor,
            'template': 'your_template',
            'token': token
        }
        response = api.verify_lookup(params)
    except APIException as e:
        raise Exception(e)
    except HTTPException as e:
        raise Exception(e)
