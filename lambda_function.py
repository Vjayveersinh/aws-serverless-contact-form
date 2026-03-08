import json
import os
import uuid
from datetime import datetime, timezone

import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb", region_name="ca-central-1")
TABLE_NAME = os.environ["TABLE_NAME"]
table = dynamodb.Table(TABLE_NAME)


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "https://dc61g20ci9ox4.cloudfront.net",
            "Access-Control-Allow-Headers": "content-type",
            "Access-Control-Allow-Methods": "POST,OPTIONS"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event, context):
    try:
        # Handle preflight request if needed
        if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
            return response(200, {"ok": True})

        body = event.get("body")
        if not body:
            return response(400, {"ok": False, "error": "Missing request body"})

        # If API Gateway sends body as string
        if isinstance(body, str):
            try:
                body = json.loads(body)
            except json.JSONDecodeError:
                return response(400, {"ok": False, "error": "Invalid JSON body"})

        name = str(body.get("name", "")).strip()
        email = str(body.get("email", "")).strip()
        message = str(body.get("message", "")).strip()

        if not name:
            return response(400, {"ok": False, "error": "Name is required"})
        if not email:
            return response(400, {"ok": False, "error": "Email is required"})
        if not message:
            return response(400, {"ok": False, "error": "Message is required"})

        item = {
            "submissionId": str(uuid.uuid4()),
            "name": name,
            "email": email,
            "message": message,
            "createdAt": datetime.now(timezone.utc).isoformat()
        }

        table.put_item(Item=item)

        return response(200, {
            "ok": True,
            "message": "Form submitted successfully",
            "submissionId": item["submissionId"]
        })

    except ClientError as e:
        return response(500, {
            "ok": False,
            "error": "DynamoDB error",
            "details": str(e)
        })
    except Exception as e:
        return response(500, {
            "ok": False,
            "error": "Internal server error",
            "details": str(e)
        })