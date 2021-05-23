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
        self.Period.request("GET","/openapi/rest/publicperformancedisplays/period?serviceKey=pSBc4o72gz9WozCjlVYbDsY6fB%2Bc4JZMtwo6ZsZ57cHCKkggLtaVjPN8ZK47Kyy%2Fk9swoZdZvA%2F9UEsETfhRSA%3D%3D")
        self.area=http.client.HTTPConnection("culture.go.kr")
        self.area.request("GET","/openapi/rest/publicperformancedisplays/area?serviceKey=pSBc4o72gz9WozCjlVYbDsY6fB%2Bc4JZMtwo6ZsZ57cHCKkggLtaVjPN8ZK47Kyy%2Fk9swoZdZvA%2F9UEsETfhRSA%3D%3D")
        self.realm=http.client.HTTPConnection("culture.go.kr")
        self.realm.request("GET","/openapi/rest/publicperformancedisplays/realm?serviceKey=pSBc4o72gz9WozCjlVYbDsY6fB%2Bc4JZMtwo6ZsZ57cHCKkggLtaVjPN8ZK47Kyy%2Fk9swoZdZvA%2F9UEsETfhRSA%3D%3D")
        self.detail = http.client.HTTPConnection("culture.go.kr")
        self.detail.request("GET", "/openapi/rest/publicperformancedisplays/d/")
        self.Naver_url="https://openapi.naver.com/v1/search/image.xml?query="
    def SearchPeriod(self):
        pass

    def SearchArea(self):
        req=self.area.getresponse()
        a=10