my_json = {
    "id": 1,
    "method": "SerpstatBacklinksProcedure.getNewBacklinks",
    "params": {
        "query": "{domain}",
        "searchType": f"dassd",
        "sort": f"adsdd",
        "order": f"asdsdsdsdsdsdsdsdsdsd",
        "page": f"dddddddddddd",
        "size": f"vvvvvvvvvvvvvv",
        "linkPerDomain": f"ffffffffffffffffffffff"
    }
}
list_or = ['list_or']
list_and = ['list_and']
my_json['params']['complexFilter'] = [list_or]
my_json['params']['complexFilter'] = [list_or, list_and]
print (my_json)