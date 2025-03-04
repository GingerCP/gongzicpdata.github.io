import requests
import json
from datetime import datetime, timedelta

# Convert UTC time to China Standard Time (CST)
def get_china_time():
    return (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

fetch_time = get_china_time()

novels = []
for page in range(0,1):
  url = 'https://www.gongzicp.com/webapi/home/recommend?page_id=0&tid=0&page=2'
  headers = {"User-Agent": "Mozilla/5.0"}

  response = requests.get(url, headers=headers)
  if response.status_code == 200:
      text = response.text
      data = json.loads(text)
      data = data['data']['list'][2]['object_list'][0]['list']

      # print(data)
      # print(data['data'])
  # Print the HTML content in a formatted way
  for novel in data:
    novels.append({
        "ID": novel["novel_id"],
        "Name": novel["novel_name"],
        "Popularity": novel["novel_allpopu"],
        "Collection": novel["novel_allcoll"],
        "Timestamp": fetch_time  # Store fetch time
    })
    print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'])
    with open('renqijiazuo.json', "w", encoding="utf-8") as file:
          json.dump(novels, file, ensure_ascii=False, indent=4)
