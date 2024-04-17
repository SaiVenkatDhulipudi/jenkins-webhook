import json
import os
import requests


def lambda_handler(event, context):
    print(event)
    body = event.get("body")
    jenkins_url = os.environ.get("JENKINS_URL")
    if body and jenkins_url:
        body = json.loads(body)
        print(body)
        req = requests.post(
            jenkins_url,
            data=json.dumps(body).encode("utf-8"),
            headers=event.get("headers"),
        )
        print(req.__dict__)
    return {"statusCode": 200, "body": "Success"}
