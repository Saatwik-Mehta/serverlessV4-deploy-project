import json
import requests
from Utils.common.all_apis import sample_post

def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!"
    }
    print(sample_post("https://www.google.com"))
    return {"statusCode": 200, "body": json.dumps(body)}
