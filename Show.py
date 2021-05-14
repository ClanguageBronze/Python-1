import http.client
from xml.dom.minidom import parse, parseString
class Contents:
    def __init__(self):
        self.Period=http.client.HTTPConnection("culture.go.kr")
        self.contents.request("GET","/openapi/rest/publicperformancedisplays/period")
