import http.client
from xml.dom.minidom import parse, parseString
class Contents:
    PeriodDataList=[]
    AreaDataList=[]
    ReleamDataList=[]
    def __init__(self):
        self.client_id="rxUZBymLQbyAVdAs19er"
        self.client_Secret="rxUZBymLQbyAVdAs19er"
        self.Period=http.client.HTTPConnection("culture.go.kr")
        self.Period.request("GET","/openapi/rest/publicperformancedisplays/period")
        self.area=http.client.HTTPConnection("culture.go.kr")
        self.area.request("GET","/openapi/rest/publicperformancedisplays/area")
        self.realm=http.client.HTTPConnection("culture.go.kr")
        self.realm.request("GET","/openapi/rest/publicperformancedisplays/realm")
        self.detail = http.client.HTTPConnection("culture.go.kr")
        self.detail.request("GET", "/openapi/rest/publicperformancedisplays/d/")
        self.Naver_url="https://openapi.naver.com/v1/search/image.xml?query="
    def SearchPeriod(self):
        pass

    def SearchArea(self):
        pass