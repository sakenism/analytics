import os
import json
import requests

def exec_sql(sql_query: str):
    url = f"{os.getenv('HASURA_URL')}/query"
    payload = json.dumps({
        "type": "run_sql",
        "args": {
            "sql": sql_query
        }
    })
    headers = {
        "Content-Type": "application/json",
        "X-Hasura-Admin-Secret": os.getenv('HASURA_SECRET')
    }

    req = requests.post(url, headers=headers, data=payload)
    resp = req.json()
    head = resp["result"][0]
    data = resp["result"][1:]
    for i in range(len(data)):
        data[i] = dict(zip(head, data[i]))
    return data
