
import json
import pandas as pd

t = '''
    {"id": "1",
    "result": {
        "data": [
            {
                "url_from": "https://www.wmlou.com/",
                "url_to": "https://serpstat.com/?ref=326045",
                "nofollow": "follow",
                "link_type": "href",
                "links_ext": 330,
                "link_text": "Serpstat",
                "first_seen": "2020-11-24",
                "last_visited": "2021-03-29 09:19:13",
                "domain_rank": 22
            },
            {
                "url_from": "https://www.vsesv.com/",
                "url_to": "http://serpstat.com",
                "nofollow": "follow",
                "link_type": "href",
                "links_ext": 11,
                "link_text": "Serpstat",
                "first_seen": "2021-08-06",
                "last_visited": "2021-08-06 10:42:54",
                "domain_rank": 17
            }
        ],
        "summary_info": {
            "left_lines": 999806,
            "page": 1,
            "count": 2,
            "total": 167,
            "sort": "url_from",
            "order": "DESC"
        }
    }
}'''


if __name__ == '__main__':

    data = json.loads(t)
    df = pd.DataFrame(data['result']['data'])
    print (df)
    df.to_csv('data.csv',index=False)
