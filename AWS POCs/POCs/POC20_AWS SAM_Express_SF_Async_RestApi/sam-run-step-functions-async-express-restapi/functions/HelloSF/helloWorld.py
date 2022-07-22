import json

import requests


def lambda_handler(event, context):
    
    try:
        ip= requests.get("http://checkip.amazonaws.com/")
        print ("e")
    except requests.RequestException as e:
        print (e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world from lambda",
                "location": ip.text.replace("\n", "")
            }
        ),
    }
