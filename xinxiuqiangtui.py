import requests
import json
from datetime import datetime, timedelta

# Convert UTC time to China Standard Time (CST)
def get_china_time():
    return (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")


# URL of the webpage

novels = []
url = 'https://gongzicp.com/webapi/home/recommend?page_id=0&tid=0&page=2'
headers = {"User-Agent": "Mozilla/5.0"}
fetch_time = get_china_time()
response = requests.get(url, headers=headers)
if response.status_code == 200:
    text = response.text
    data = json.loads(text)
for obj in data['data']['list']:
  if obj['object_id'] == 69:
    for novel in obj['object_list'][0]['list']:
      novels.append({
      "ID": novel["novel_id"],
      "Name": novel["novel_name"],
      "Popularity": novel["novel_allpopu"],
      "Collection": novel["novel_allcoll"],
      "Timestamp": fetch_time
    })

with open('xinxiuqiangtui.json', "w", encoding="utf-8") as file:
      json.dump(novels, file, ensure_ascii=False, indent=4)
