import requests
import json
import requests

class BadRequest(Exception):
    pass
class Unauthorized(Exception):
    pass
class PaymentRequired(Exception):
    pass
class Forbidden(Exception):
    pass
class NotFound(Exception):
    pass

FIFTEEN_MINUTES = 900

def checkError(code):
    if code == 400:
        raise BadRequest
    if code == 401:
        raise Unauthorized
    if code == 402:
        raise PaymentRequired
    if code == 403:
        raise Forbidden
    if code == 404:
        raise NotFound

def isSuccess(r):
    if r['status']=='failed':
        raise NotFound(r['message'])

def checkID(id:int):
    r = requests.get(f'https://discordscammers.com/api/v1/search/{id}', verify = False,timeout=2)
    code = r.status_code
    back = r.json
    isSuccess(r.json())
    checkError(code)
    return back

def report(scammerId:str, scammerName:str, scammerInfo:str):
    sendThis = {'ScammerID': scammerId,'ScammerUsername': scammerName,'AdditionalInfo': scammerInfo}
    r = requests.post(f'https://discordscammers.com/api/v1/report',json=sendThis, verify = False)
    code = r.status_code
    checkError(code)
    back = r.json()
    return back