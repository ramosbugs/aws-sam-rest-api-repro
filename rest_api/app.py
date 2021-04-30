import json

# import requests

def lambda_handler(event, context):
    import pprint
    pprint.pprint(event)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "routed to handler %s" % (event["requestContext"].get("operationName", "<missing operationName>")),
        }) + "\n",
    }
