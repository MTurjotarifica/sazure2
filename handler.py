import logging
import os
import json
import requests

import azure.functions as func
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.signature import SignatureVerifier

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Verify the Slack request signature
    signature_verifier = SignatureVerifier(os.environ["SLACK_SIGNING_SECRET"])
    try:
        signature_verifier.validate(
            req.headers.get("X-Slack-Request-Timestamp"),
            req.headers.get("X-Slack-Signature"),
            req.get_body()
        )
    except Exception as e:
        return func.HttpResponse("Signature verification failed", status_code=400)

    # Parse the request body
    request_body = req.get_json()
    command = request_body["command"]
    text = request_body["text"]

    # Handle the command
    if command == "/mycommand":
        # Your code to handle the command goes here
        # ...
        response = {
            "response_type": "in_channel",
            "text": "Your command was processed successfully!"
        }
        return func.HttpResponse(json.dumps(response), mimetype="application/json")

    return func.HttpResponse("Unknown command", status_code=400)
