import requests 
import csv
from datetime import datetime
# KEY는 나중에 암호화
# api 사용
import os
MY_API_KEY = os.getenv("WEATHER_API_KEY")
city_name = "Seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={MY_API_KEY}"
url += "&units=metric"

# get 방식으로 요청할 때, requests

import requests # get 방식으로 요청할때 사용
response = requests.get(url)
response.status_code
# 3가지 방법으로 처리
# 1) text : response.text
# 2) byte : response.content
# 3) json : response.json()
result = response.json()

temp = result["main"]["temp"]
sup = result["main"]["humidity"]
pu = result["wind"]["speed"]
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# weather.csv를 만들자
# 최초 생성 시 -> 헤더도 추가
# 파일이 존재하면 -> 덮어쓰기
csv_exist = os.path.exists("Weather.csv")
header = ["current_time", "temp", "sup", "pu"]


with open("weather.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if not csv_exist:
        writer.writerow([header])
    writer.writerow([current_time, temp, sup, pu])
print("날씨 저장 완료")    
    
