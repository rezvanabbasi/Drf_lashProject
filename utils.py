from kavenegar import *

API_KEY = '6E4B6B475561704C33494A5138766F5335566F7A61495868476B432B30304261485A4551596F71756733343D'


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
