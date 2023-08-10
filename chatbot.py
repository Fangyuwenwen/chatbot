import requests
import statistics
import errno
import json
import os
import sys
from bs4 import BeautifulSoup
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

line_bot_api = LineBotApi('Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('8b1a56575bae472963d126b9253209fc')

if __name__ == '__main__':
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    options = arg_parser.parse_args()

    httpd = wsgiref.simple_server.make_server('', options.port, application)
    httpd.serve_forever()