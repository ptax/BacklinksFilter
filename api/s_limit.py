import requests
import json
from time import sleep
def s_limit():
    #with open('serpstat/s_token.txt') as token:
        #token = token.readline()
    token = '6be8482c0305d212c1286b9d8fc304f4'
    sleep(4)
    api_url = f'https://api.serpstat.com/v4/?token={token}'.strip()
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = { "id": 1, "method": "SerpstatLimitsProcedure.getStats"}
    response = requests.post(api_url, data=json.dumps(data), headers=headers)
    my_limit = json.loads(response.text)['result']['data']['left_lines']
    return my_limit

print(s_limit())