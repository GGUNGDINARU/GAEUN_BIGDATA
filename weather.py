import requests
from bs4 import BeautifulSoup

print("#"*30)
print("\n부산의 일주일 날씨입니다!\n")
print("#"*30)

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

for item in soup.find_all('data'):
    print(item.find('tmef').text, item.find('wf').text, item.find('tmn').text, item.find('tmx').text)

# 엑셀에 데이터 쓰기
from openpyxl import Workbook

# 엑셀파일 쓰기
write_wb = Workbook()

# 이름이 있는 시트를 생성
write_ws = write_wb.create_sheet('부산 일주일 날씨')  

# Sheet1에다 입력 
write_ws = write_wb.active
write_ws['A1'] = '날짜와 시간'
write_ws['B1'] = '날씨'
write_ws['C1'] = '최저온도'
write_ws['D1'] = '최고온도'

#행 단위로 추가 날짜와 시간, 날씨, 최저온도, 최고온도
data = []
for item in soup.find_all('data'):
    date_time = item.find('tmef').text
    how_weather = item.find('wf').text
    mini = item.find('tmn').text
    maxi = item.find('tmx').text
    write_ws.append([f'{date_time}',(f'{how_weather}'),f'{mini}',f'{maxi}'])

write_wb.save('부산 일주일 날씨.xlsx')