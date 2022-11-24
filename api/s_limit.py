import requests
import json
from time import sleep
def s_limit():
    #with open('serpstat/s_token.txt') as token:
        #token = token.readline()
    token = 'd1395f5c0aa1847efac414fc330a8bba'
    sleep(4)
    api_url = f'https://api.serpstat.com/v4/?token={token}'.strip()
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = { "id": 1, "method": "SerpstatLimitsProcedure.getStats"}
    response = requests.post(api_url, data=json.dumps(data), headers=headers)
    my_limit = json.loads(response.text)['result']['data']['left_lines']
    return my_limit
