# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

import json
import time

from linebot.models import *
from .instance import wrapper

def index(request):
    return HttpResponse("#Ly Center LINE Messaging API BOT.")



api = wrapper()

def webhook(request):
    try:
        rjsons = json.loads(request.body.decode('utf-8'))
    except json.decoder.JSONDecodeError:
        return HttpResponse("#Ly Center LINE Messaging API BOT.")
    
    for rj in rjsons['events']:
        rjson = api.bot_response(rj)
        
        if type(rjson) is not bool:
            typ = rjson['type']
            chat = rjson['source']['type']
            sender = rjson['source'][chat + "Id"]
                
            if typ == "message":
                api.reply_text(rjson['replyToken'], typ)
            elif typ == "follow":
                api.reply_text(rjson['replyToken'], typ)
            elif typ == "join":
                api.reply_text(rjson['replyToken'], typ)

            
        else:
            return HttpResponse("#Ly Center LINE Messaging API BOT.")
    return HttpResponse(rjsons['events'])

    


