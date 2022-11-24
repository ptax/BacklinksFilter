import json
import pandas as pd

def read_config():
    with open('config/search_config.json') as data:
        data = json.loads(data.read())
    table = pd.DataFrame(data)
    t = (pd.DataFrame(table['params']['complexFilter']))
    print (len(t))
    #return table.head()

print (read_config())


def greatread_config():
    with open('config/search_config.json') as data:
        data = json.loads(data.read())
    table = pd.DataFrame(data)
    t = (pd.DataFrame(table['params']['complexFilter']))
    print (t)
    return table.head()