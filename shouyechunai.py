import requests
import json
from datetime import datetime, timedelta

# Convert UTC time to China Standard Time (CST)
def get_china_time():
    return (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")


# URL of the webpage

novels = []
url = 'https://gongzicp.com/webapi/home/recommend?page_id=0&tid=0&page=3'
headers = {"User-Agent": "Mozilla/5.0"}
fetch_time = get_china_time()
response = requests.get(url, headers=headers)
if response.status_code == 200:
    text = response.text
    data = json.loads(text)
    # print(data)
    # print(data['data']['list'][0].keys())
    # print(data['data']['list'][0].keys())
for k in range(len(data['data']['list'])):
  if 'object_list' in data['data']['list'][k].keys():
    if  data['data']['list'][k]['object_id'] == 71:
      print(data['data']['list'][k]['object_name'])
      for novel in data['data']['list'][k]['object_list'][0]['list']:
        print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
        novels.append({
        "ID": novel["novel_id"],
        "Name": novel["novel_name"],
        "Popularity": novel["novel_allpopu"],
        "Collection": novel["novel_allcoll"],
        "Timestamp": fetch_time
      })
  with open('chunaishouye.json', "w", encoding="utf-8") as file:
        json.dump(novels, file, ensure_ascii=False, indent=4)
