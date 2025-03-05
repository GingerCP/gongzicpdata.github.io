import requests
import json
from datetime import datetime, timedelta

# Convert UTC time to China Standard Time (CST)
def get_china_time():
    return (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")


# URL of the webpage


with open('syxy.json', "w", encoding="utf-8") as file:
      json.dump(novels, file, ensure_ascii=False, indent=4)

novels = []
url = 'https://gongzicp.com/webapi/home/recommendList?identifier=zyyc&tid=75&swap=1&style_id=7'
headers = {"User-Agent": "Mozilla/5.0"}
fetch_time = get_china_time()
response = requests.get(url, headers=headers)
if response.status_code == 200:
    text = response.text
    data = json.loads(text)
for novel in data['data']:
  # print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
      # print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
  novels.append({
  "ID": novel["novel_id"],
  "Name": novel["novel_name"],
  "Popularity": novel["novel_allpopu"],
  "Collection": novel["novel_allcoll"],
  "Timestamp": fetch_time
})

with open('syxd.json', "w", encoding="utf-8") as file:
      json.dump(novels, file, ensure_ascii=False, indent=4)

novels = []
url = 'https://gongzicp.com/webapi/home/recommendList?identifier=zyyc&tid=75&swap=2&style_id=7'
headers = {"User-Agent": "Mozilla/5.0"}
fetch_time = get_china_time()
response = requests.get(url, headers=headers)
if response.status_code == 200:
    text = response.text
    data = json.loads(text)
for novel in data['data']:
  # print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
      # print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
  novels.append({
  "ID": novel["novel_id"],
  "Name": novel["novel_name"],
  "Popularity": novel["novel_allpopu"],
  "Collection": novel["novel_allcoll"],
  "Timestamp": fetch_time
})

with open('sygd.json', "w", encoding="utf-8") as file:
      json.dump(novels, file, ensure_ascii=False, indent=4)


novels = []
url = 'https://gongzicp.com/webapi/home/recommendList?identifier=zyyc&tid=75&swap=3&style_id=7'
headers = {"User-Agent": "Mozilla/5.0"}
fetch_time = get_china_time()
response = requests.get(url, headers=headers)
if response.status_code == 200:
    text = response.text
    data = json.loads(text)
for novel in data['data']:
  # print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
      # print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
  novels.append({
  "ID": novel["novel_id"],
  "Name": novel["novel_name"],
  "Popularity": novel["novel_allpopu"],
  "Collection": novel["novel_allcoll"],
  "Timestamp": fetch_time
})

with open('syhx.json', "w", encoding="utf-8") as file:
      json.dump(novels, file, ensure_ascii=False, indent=4)


novels = []
url = 'https://gongzicp.com/webapi/home/recommendList?identifier=zyyc&tid=75&swap=4&style_id=7'
headers = {"User-Agent": "Mozilla/5.0"}
fetch_time = get_china_time()
response = requests.get(url, headers=headers)
if response.status_code == 200:
    text = response.text
    data = json.loads(text)
    # print(data)
    # print(data['data']['list'][0]['object_list'])
    # print(data['data']['list'][0].keys())
for novel in data['data']:
  # print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
      # print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
  novels.append({
  "ID": novel["novel_id"],
  "Name": novel["novel_name"],
  "Popularity": novel["novel_allpopu"],
  "Collection": novel["novel_allcoll"],
  "Timestamp": fetch_time
})

with open('syxy.json', "w", encoding="utf-8") as file:
      json.dump(novels, file, ensure_ascii=False, indent=4)


novels = []
url = 'https://gongzicp.com/webapi/home/recommendList?identifier=zyyc&tid=75&swap=5&style_id=7'
headers = {"User-Agent": "Mozilla/5.0"}
fetch_time = get_china_time()
response = requests.get(url, headers=headers)
if response.status_code == 200:
    text = response.text
    data = json.loads(text)
for novel in data['data']:
  # print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
      # print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'],fetch_time)
  novels.append({
  "ID": novel["novel_id"],
  "Name": novel["novel_name"],
  "Popularity": novel["novel_allpopu"],
  "Collection": novel["novel_allcoll"],
  "Timestamp": fetch_time
})

with open('syjk.json', "w", encoding="utf-8") as file:
      json.dump(novels, file, ensure_ascii=False, indent=4)

