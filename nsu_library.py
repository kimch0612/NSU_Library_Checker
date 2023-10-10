from bs4 import BeautifulSoup
import requests

def messageNSULibrary():
    strMessage = ""
    strUrl = "http://220.68.191.20/setting"
    requestSession = requests.Session()
    Response = requestSession.get(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()
    Response = dict(Response)
    first = "제1 자유열람실 : 여석 %s석 (%s석 사용중)\n" % (Response['data']['data'][0]['available'], Response['data']['data'][0]['inUse'])
    second = "제2 자유열람실 : 여석 %s석 (%s석 사용중)\n" % (Response['data']['data'][1]['available'], Response['data']['data'][1]['inUse'])
    third = "제3 자유열람실 : 여석 %s석 (%s석 사용중)" % (Response['data']['data'][2]['available'], Response['data']['data'][2]['inUse'])

    strMessage = "남서울대학교 열람실 좌석현황(성암기념중앙도서관)\n\n" + first + second + third
    
    return strMessage