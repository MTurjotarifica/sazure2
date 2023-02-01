import slack
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slackeventsapi import SlackEventAdapter
# from vis_functions import *
from slack_sdk.signature import SignatureVerifier
import os
import pandas as pd
import numpy as np
import json
import urllib
from flask import Flask, request, Response




def lambda_handler(event, context):
    app = Flask(__name__)
    slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'], '/slack/events', app)

    #getting slack_bot_token from our stored environment variable
    client = WebClient(token=os.environ['SLACK_TOKEN'])
    #obtains bot id
    BOT_ID = client.api_call("auth.test")['user_id'] #gives us the bot id
    signature_verifier = SignatureVerifier(os.environ["SIGNING_SECRET"])
    @app.route('/slack/interactive-endpoint', methods=['GET','POST'])
    def interactive_trigger():
        print("trigger works")
     
    @app.route('/hello', methods=['POST'])
    def hello():
        
        print("hello works")
        client.chat_postMessage(channel='#random', 
                                            text="hello world  ",
                                            )
        #returning empty string with 200 response
        return '', 200


