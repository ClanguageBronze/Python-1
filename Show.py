import http.client
from xml.dom.minidom import parse, parseString
class Contents:
    def __init__(self):
        self.Period=http.client.HTTPConnection("culture.go.kr")
        self.Period.request("GET","/openapi/rest/publicperformancedisplays/period")
        self.area=http.client.HTTPConnection("culture.go.kr")
        self.area.request("GET","/openapi/rest/publicperformancedisplays/area")
        self.realm=http.client.HTTPConnection("culture.go.kr")
        self.realm.request("GET","/openapi/rest/publicperformancedisplays/realm")
        self.detail = http.client.HTTPConnection("culture.go.kr")
        self.detail.request("GET", "/openapi/rest/publicperformancedisplays/d/")