#네이버 실시간 인기 쇼핑 키워드 크롤링하는 프로그램
import requests
from bs4 import BeautifulSoup
import json

#AOO 전체, M01~M05 10대~50대 남성, F01~F05 50대 여성
#ALL 전체, 50000000 패션의류, 50000001 패션잡화, 50000002 화장품미용, 50000003 디지털가전, 50000004 가구인테리어
#50000005 출산육아, 50000006 식품, 50000007 스포츠레저, 50000008 생활건강, 50000009 여가생활편의

"""
age_gender
A00
M01
M02
M03
M04
M05
F01
F02
F03
F04
F05

categoryCategoryId
ALL
50000000
50000001
50000002
50000003
50000004
50000005
50000006
50000007
50000008
50000009
"""
category_id = 'ALL'
age_gender = 'A00' #연령대별

url = 'https://search.shopping.naver.com/best/category/keyword?categoryCategoryId={}categoryDemo={}&categoryRootCategoryId=ALL&chartRank=1&period=P1D'.format(category_id, age_gender)
headers = {'Accept-Language' : 'ko-KR, ko;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,zh;q=0.5','User-Agent':'Mozila/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/100.0.4896.127 Safari/537.36', 'Accept-Encoding' : 'gzip'}

raw = requests.get(url=url, headers=headers)
html = BeautifulSoup(raw.text, 'html.parser')

test = html.find('script', {'id' : '__NEXT_DATA__'}).text #텍스트만
dict_result = json.loads(test) #json으로 변환하기
popular_kws = dict_result['props']['pageProps']['dehydratedState']['queries'][2]['state']['data']['charts']

for popular_kw in popular_kws:
    rank = popular_kw['rank'] #순위
    real_kw = popular_kw['exposeKeyword'] #키워드
    print(str(rank) + '순위 키워드 : ' + str(real_kw))