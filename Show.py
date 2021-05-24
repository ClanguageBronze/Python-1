import http.client
from tkinter import *
from tkinter import font
import tkinter.ttk
from xml.dom.minidom import parse, parseString
from urllib.request import  Request, urlopen
from urllib.parse import urlencode,quote_plus
from PIL import Image
import urllib.request
class Contents:
    PeriodDataList=[]
    AreaDataList=[]
    ReleamDataList=[]
    CheckPeriodOrArea=False
    PeriodLst=[]
    InfoText=[]

    def __init__(self):
        self.client_id="rxUZBymLQbyAVdAs19er"
        self.client_Secret="rxUZBymLQbyAVdAs19er"
    def SetPeriodEntry(self,Button):
        self.PeriodEntry=Button
    def SetAreaEntry(self,Button):
        self.AreaEntry=Button
    def SetListBox(self,Box):
        self.ListBox=Box
    def SetCanvas(self,Canvas,img):
        self.ImageCanvas=Canvas
        self.LoadImg=img
    def GetPeriodDataList(self):
        return self.PeriodDataList
    def SearchPeriod(self):
        url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period'
        Value=self.PeriodEntry.get()
        lst= [eval(i) for i in Value.split()]

        for i in range(len(lst)):
            self.PeriodLst.append(str(lst[i]))
            if len(str(lst[i])) == 6:
                self.PeriodLst[i]+='01'
        queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'pSBc4o72gz9WozCjlVYbDsY6fB+c4JZMtwo6ZsZ57cHCKkggLtaVjPN8ZK47Kyy/k9swoZdZvA/9UEsETfhRSA=='
                                          , quote_plus('keyword') : ''
                                          , quote_plus('sortStdr') : '1'
                                          , quote_plus('ComMsgHeader') : ''
                                          , quote_plus('RequestTime') : '20100810:23003422'
                                          , quote_plus('CallBackURI') : ''
                                          , quote_plus('MsgBody') : '', quote_plus('from') : self.PeriodLst[0]
                                          , quote_plus('to') : self.PeriodLst[1], quote_plus('cPage') : '1'
                                          , quote_plus('rows') : '10', quote_plus('place') : '2'
                                            })

        request = Request(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read().decode("utf-8")
        parseData=parseString(response_body)
        PeriodInfo=parseData.childNodes
        row=PeriodInfo[0].childNodes
        for item in row:
            subitem=item.childNodes
        totalCount=int(subitem[0].childNodes[0].data)
        for i in range(8,8+totalCount):
            for j in range(1,8):
                self.PeriodDataList.append(str(subitem[i].childNodes[j].childNodes[0].data))

        print(self.PeriodDataList)
        self.SortInfo(self.PeriodDataList)
        print(self.InfoText)
        for i in range(len(self.InfoText)):
            self.ListBox.insert(i,self.InfoText[i])

    def SearchArea(self):
        url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period'
        queryParams = '?' + urlencode({quote_plus(
            'ServiceKey'): 'pSBc4o72gz9WozCjlVYbDsY6fB+c4JZMtwo6ZsZ57cHCKkggLtaVjPN8ZK47Kyy/k9swoZdZvA/9UEsETfhRSA=='
                                          , quote_plus('keyword'): ''
                                          , quote_plus('sortStdr'): '1'
                                          , quote_plus('ComMsgHeader'): ''
                                          , quote_plus('RequestTime'): '20100810:23003422'
                                          , quote_plus('CallBackURI'): ''
                                          , quote_plus('MsgBody'): '', quote_plus('cPage'): '1'
                                          , quote_plus('rows'): '10', quote_plus('place'): '1'
                                            , quote_plus('gpsxfrom'): '129.101',
                                       quote_plus('gpsyfrom'): '35.142', quote_plus('gpsxto'): '129.101',
                                       quote_plus('gpsyto'): '35.142'
                                       })

        request = Request(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read().decode("utf-8")
        print(response_body)


    def SortInfo(self,lst):
        for i in range(0,int(len(lst)/7)):
            self.InfoText.append('[제목]:'+self.PeriodDataList[0+(i*7)]+'   [시작일]:'+self.PeriodDataList[1+(i*7)]+'  [마감일]'+
                                 self.PeriodDataList[2+(i*7)]+' [장소:]'+self.PeriodDataList[3+(i*7)]+' [분야]:'+self.PeriodDataList[4+(i*7)]
                                 +'   [지역]:'+self.PeriodDataList[5+(i*7)])


    def GetImage(self):
        pass
