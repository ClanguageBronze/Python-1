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
    m_bPeriod=False
    m_bArea=False
    m_Common=[]

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
    def GetListBox(self):
        return self.ListBox
    def GetPeriodDataList(self):
        return self.PeriodDataList
    def GetPeriod(self):
        return self.m_bPeriod
    def GetArea(self):
        return self.m_bArea
    def SearchPeriod(self):
        self.m_bPeriod=True
        self.PeriodDataList.clear()
        self.ListBox.delete(0, len(self.InfoText))
        self.InfoText.clear()
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
                                          , quote_plus('RequestTime') : '20210525:06273422'

                                          , quote_plus('from') : self.PeriodLst[0]
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
            for j in range(1,10):
                self.PeriodDataList.append(str(subitem[i].childNodes[j].childNodes[0].data))

        if self.m_bArea == True and self.m_bPeriod == True:
            self.CommonInfo()
            self.SortInfo(self.m_Common, self.InfoText)
        else:
            self.SortInfo(self.PeriodDataList, self.InfoText)
        self.ListBox.delete(0, len(self.InfoText) + 1)
        for i in range(len(self.InfoText)):
            self.ListBox.insert(i, self.InfoText[i])
    def SearchArea(self):
        self.m_bArea=True
        url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/area'
        Value = self.AreaEntry.get()
        lst = [str(i) for i in Value.split()]
        queryParams = '?' + urlencode({quote_plus(
            'ServiceKey'): 'pSBc4o72gz9WozCjlVYbDsY6fB+c4JZMtwo6ZsZ57cHCKkggLtaVjPN8ZK47Kyy/k9swoZdZvA/9UEsETfhRSA=='
                                          , quote_plus('ComMsgHeader'): ''
                                          , quote_plus('RequestTime'): '20100810:23003422'
                                          , quote_plus('CallBackURI'): ''
                                          , quote_plus('MsgBody'): ''
                                          , quote_plus('sido'): str(lst[0])
                                          , quote_plus('gugun'): str(lst[1])
                                          , quote_plus('from'): '20200101', quote_plus('to'): '20211201'
                                          , quote_plus('place'): '1'

                                          , quote_plus('cPage'): '1'
                                          , quote_plus('rows'): '10', quote_plus('keyword'): ''
                                          , quote_plus('sortStdr'): '1'
                                       })

        request = Request(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read().decode("utf-8")
        parseData = parseString(response_body)
        AreaInfo = parseData.childNodes
        row = AreaInfo[0].childNodes
        for item in row:
            subitem = item.childNodes
        totalCount = int(subitem[0].childNodes[0].data)
        self.AreaDataList.clear()

        for i in range(10, 10 + totalCount):
            for j in range(1, 10):
                self.AreaDataList.append(str(subitem[i].childNodes[j].childNodes[0].data))

        if self.m_bArea == True and self.m_bPeriod == True:
            self.CommonInfo()
            self.SortInfo(self.m_Common,self.InfoText)
        else:
            self.SortInfo(self.AreaDataList,self.InfoText)


        print(self.InfoText)
        self.ListBox.delete(0,len(self.InfoText)+1)
        for i in range(len(self.InfoText)):
            self.ListBox.insert(i, self.InfoText[i])


    def SortInfo(self,lst,lst2):
        lst2.clear()
        for i in range(0,int(len(lst)/9)):
            lst2.append('[제목] :'+lst[0+(i*9)]+'   [시작일] :'+lst[1+(i*9)]+'  [마감일] :'+
                                 lst[2+(i*9)]+' [장소] :'+lst[3+(i*9)]+' [분야] :'+lst[4+(i*9)]
                                 +'   [지역]:'+lst[5+(i*9)])


    def CommonInfo(self):
        self.m_Common.clear()
        for i in range(0,int(len(self.PeriodDataList)),9):
            for j in range(0,int(len(self.AreaDataList)),9):
                if self.PeriodDataList[i]==self.AreaDataList[j]:
                    for h in range(9):
                        self.m_Common.append(self.PeriodDataList[h+i])


        print(self.m_Common)

