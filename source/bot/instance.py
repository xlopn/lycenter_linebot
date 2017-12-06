# -*- coding: utf-8 -*-

from django.http import HttpResponse
from linebot.models import *

import os
import json
import requests

class wrapper:

    """Reference:: https://developers.line.me/ja/docs/messaging-api/reference"""

    api_uri       = "https://api.line.me/v2/bot"
    
    chat_member   = api_uri + "/%s/%s/member/%s" #chatType,chatId,userId [GET]
    leave         = api_uri + "/%s/%s/leave" #chatType,chatId [POST]
    profile       = api_uri + "/profile/%s" #userId [GET]
    reply         = api_uri + "/message/reply" #[POST]
    get_contents  = api_uri + "/message/%s/content" #messageId [GET]
    nat_rich      = api_uri + "/richmenu/%s" #richmenuId [GET,DELETE] 
    make_rich     = api_uri + "/richmenu" #[POST]
    usr_rich      = api_uri + "/user/%s/richmenu" #userId [GET,DELETE]
    link_usr_rich = api_uri + "/user/%s/richmenu/%s" #userId,richmenuId [POST]
    rich_image    = api_uri + "/richmenu/%s/content" #richmenuId [POST,GET]
    get_rich      = api_uri + "/richmenu/list" #[GET]
    
    access_token = os.environ.get('ACCESS_TOKEN', 3)
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token
    }
    get_header = {
        "Authorization": "Bearer " + access_token
    }

    def reply_text(self, reply_token, text):
        messages = [TextSendMessage(text=text)]
    
        payload = {
            "replyToken":reply_token,
            "messages": [message.as_json_dict() for message in messages]
        }

        requests.post(self.reply, headers=self.header, data=json.dumps(payload))
    
    def leave_chat(self, _id, chat=None):
        if chat is not None:
            requests.post(self.leave % (chat, _id), headers=self.header)

    def bot_response(self, json):
        try:
            typ = json['type']
            return json
        except KeyError:
            return False

    

    

    

    
