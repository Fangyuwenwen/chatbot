import requests
import statistics
import errno
import json
import os
import sys
import requests 
#from bs4 import BeautifulSoup
import pandas as pd
import re
import wsgiref.simple_server
from argparse import ArgumentParser

from urllib.request import urlopen
from argparse import ArgumentParser


from flask import Flask, request, abort

from builtins import bytes
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,MessageTemplateAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage,PostbackTemplateAction)

from linebot.utils import PY3

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None or channel_access_token is None:
    print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

def handle_message(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        if event.message.type == 'text':
            message_text = event.message.text
            if message_text == '含水度':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="若含水量大於100，請檢查有無進水處。若含水量介於50~100%，請通知業主觀察。若含水量小於50%，則符合標準"))
            elif message_text == '油質老化度':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="若油質老化度小於800，請建議業主更換新油。若油質老化度大於800，則符合標準"))
            elif message_text == '油質檢測':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="若油質檢測中的三個數值，其中一數值分別大於18、16、13，請啟動離線過濾器。若數值小於18、16、13則符合標準"))
            elif message_text == '油溫檢查':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="若油溫小於60度，通知業主油壓系統異常。若油溫大於60度，請進行下一個項目"))
            elif message_text == '出口壓力':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="出口壓力設定值須等於測量值，若無問題可進行下一個項目"))
            elif message_text == '出口流量':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="出口壓力設定值須等於測量值，若無問題可進行下一個項目"))
            elif message_text == '目視檢查':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="目視檢查是否有漏油，若有漏油請判斷是否須返廠，若無漏油請進行下一個項目"))
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='請輸入正確關鍵字'))

def application(environ, start_response):
    # check request path
    if environ['PATH_INFO'] != '/callback':
        start_response('404 Not Found', [])
        return create_body('Not Found')

    # check request method
    if environ['REQUEST_METHOD'] != 'POST':
        start_response('405 Method Not Allowed', [])
        return create_body('Method Not Allowed')

    # get X-Line-Signature header value
    signature = environ['HTTP_X_LINE_SIGNATURE']

    # get request body as text
    wsgi_input = environ['wsgi.input']
    content_length = int(environ['CONTENT_LENGTH'])
    body = wsgi_input.read(content_length).decode('utf-8')

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        start_response('400 Bad Request', [])
        return create_body('Bad Request')

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if isinstance(event, MessageEvent):           
            handle_message(event)

    start_response('200 OK', [])
    return create_body('OK')



def create_body(text):
    if PY3:
        return [bytes(text, 'utf-8')]
    else:
        return text

if __name__ == '__main__':
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    options = arg_parser.parse_args()

    httpd = wsgiref.simple_server.make_server('', options.port, application)
    httpd.serve_forever()