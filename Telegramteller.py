#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import Telegramnoti


def replyAptData(date_param, user, loc_param='11710'):
    res_list = Telegramnoti.getData( loc_param, date_param )
    msg = ''
    for r in res_list:
        if len(r+msg)+1>Telegramnoti.MAX_MSG_LENGTH:
            Telegramnoti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        Telegramnoti.sendMessage( user, msg )
    else:
        Telegramnoti.sendMessage( user, '%s 기간에 해당하는 데이터가 없습니다.'%date_param )


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        Telegramnoti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('지역') and len(args)>1:
        replyAptData( args[2], chat_id, args[1] )
    else:
        Telegramnoti.sendMessage(chat_id, '모르는 명령어입니다.\n지역 [서울 강남구]을 입력하세요.')


def Running():
    bot = telepot.Bot(Telegramnoti.TOKEN)
    bot.message_loop(handle)
