import http.client

from xml.dom.minidom import parse, parseString
from urllib.request import  Request, urlopen
from urllib.parse import urlencode,quote_plus
class Contents:
    PeriodDataList=[]
    AreaDataList=[]
    ReleamDataList=[]
    CheckPeriodOrArea=False
    PeriodLst=[]
    def __init__(self):
        self.client_id="rxUZBymLQbyAVdAs19er"
        self.client_Secret="rxUZBymLQbyAVdAs19er"
    def SetPeriodEntry(self,Button):
        self.PeriodEntry=Button
    def SetAreaEntry(self,Button):
        self.AreaEntry=Button
    def GetPeriodDataList(self):
        return self.PeriodDataList
    def SearchPeriod(self):
        url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period'
        Value=self.PeriodEntry.get()
        lst= [eval(i) for i in Value.split()]

        for i in range(len(lst)):
            self.PeriodDataList.append(str(lst[i]))
            if len(str(lst[i])) == 6:
                self.PeriodDataList[i]+='01'
        queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'pSBc4o72gz9WozCjlVYbDsY6fB+c4JZMtwo6ZsZ57cHCKkggLtaVjPN8ZK47Kyy/k9swoZdZvA/9UEsETfhRSA=='
                                          , quote_plus('keyword') : ''
                                          , quote_plus('sortStdr') : '1'
                                          , quote_plus('ComMsgHeader') : ''
                                          , quote_plus('RequestTime') : '20100810:23003422'
                                          , quote_plus('CallBackURI') : ''
                                          , quote_plus('MsgBody') : '', quote_plus('from') : self.PeriodDataList[0]
                                          , quote_plus('to') : self.PeriodDataList[1], quote_plus('cPage') : '1'
                                          , quote_plus('rows') : '10', quote_plus('place') : '1'
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
            for j in range(1,6):
                self.PeriodDataList.append(str(subitem[i].childNodes[j].childNodes[0].data))

        print(self.PeriodDataList)

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
                                          , quote_plus('rows'): '10', quote_plus('place'): ''
                                            , quote_plus('gpsxfrom'): '129.101',
                                       quote_plus('gpsyfrom'): '35.142', quote_plus('gpsxto'): '129.101',
                                       quote_plus('gpsyto'): '35.142'
                                       })

        request = Request(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read().decode("utf-8")
        print(response_body)

