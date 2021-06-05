import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import  Request, urlopen
from urllib.parse import urlencode,quote_plus
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback
from xml.dom.minidom import parse, parseString
key = 'pSBc4o72gz9WozCjlVYbDsY6fB+c4JZMtwo6ZsZ57cHCKkggLtaVjPN8ZK47Kyy/k9swoZdZvA/9UEsETfhRSA=='
TOKEN = '1783796762:AAGDzaJpZBvo-U8pa3X6TuRIk5cU8HKU43o'
MAX_MSG_LENGTH = 300

bot = telepot.Bot(TOKEN)

def getAreaData(loc_param, date_param):
    res_list = []
    baseurl = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/area'
    queryParams = '?' + urlencode({quote_plus(
        'ServiceKey'): 'pSBc4o72gz9WozCjlVYbDsY6fB+c4JZMtwo6ZsZ57cHCKkggLtaVjPN8ZK47Kyy/k9swoZdZvA/9UEsETfhRSA=='
                                      , quote_plus('ComMsgHeader'): ''
                                      , quote_plus('RequestTime'): '20100810:23003422'
                                      , quote_plus('CallBackURI'): ''
                                      , quote_plus('MsgBody'): ''
                                      , quote_plus('sido'): loc_param
                                      , quote_plus('gugun'): date_param
                                      , quote_plus('from'): '20200101', quote_plus('to'): '20211201'
                                      , quote_plus('place'): '1'

                                      , quote_plus('cPage'): '1'
                                      , quote_plus('rows'): '10', quote_plus('keyword'): ''
                                      , quote_plus('sortStdr'): '1'
                                   })


    request = Request(baseurl + queryParams)
    #print(url)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode("utf-8")
    parseData = parseString(response_body)
    PeriodInfo = parseData.childNodes
    row = PeriodInfo[0].childNodes
    for item in row:
        subitem = item.childNodes
    totalCount = int(subitem[0].childNodes[0].data)
    for i in range(10, 10 + totalCount):
        for j in range(1, 10):
            res_list.append(str(subitem[i].childNodes[j].childNodes[0].data))
    return res_list

def getPeriodData(loc_param, date_param):
    res_list = []
    baseurl = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period'
    queryParams = '?' + urlencode({quote_plus(
        'ServiceKey'): 'pSBc4o72gz9WozCjlVYbDsY6fB+c4JZMtwo6ZsZ57cHCKkggLtaVjPN8ZK47Kyy/k9swoZdZvA/9UEsETfhRSA=='
                                      , quote_plus('keyword'): ''
                                      , quote_plus('sortStdr'): '1'
                                      , quote_plus('ComMsgHeader'): ''
                                      , quote_plus('RequestTime'): '20210525:06273422'

                                      , quote_plus('from'): loc_param
                                      , quote_plus('to'):date_param, quote_plus('cPage'): '1'
                                      , quote_plus('rows'): '10', quote_plus('place'): '2'
                                   })


    request = Request(baseurl + queryParams)
    #print(url)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode("utf-8")
    parseData = parseString(response_body)
    PeriodInfo = parseData.childNodes
    row = PeriodInfo[0].childNodes
    for item in row:
        subitem = item.childNodes
    totalCount = int(subitem[0].childNodes[0].data)
    for i in range(8, 8 + totalCount):
        for j in range(1, 10):
            res_list.append(str(subitem[i].childNodes[j].childNodes[0].data))
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)