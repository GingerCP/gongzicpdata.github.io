import requests 
import json
from datetime import datetime, timedelta

# Convert UTC time to China Standard Time (CST)
def get_china_time():
    return (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
# URL of the webpage
novels = []
fetch_time = get_china_time()
  url = 'https://gongzicp.com/webapi/home/recommend?page_id='+str(page)+'&tid=0&p'
  headers = {"User-Agent": "Mozilla/5.0"}
  fetch_time = get_china_time()
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
      text = response.text
      data = json.loads(text)

  # Print the HTML content in a formatted way
  # print(data['data']['list'][0].keys())
 
  for k in range(len(data['data']['list'])):
    if 'list' in data['data']['list'][k]['object_list'][0].keys():
      print(data['data']['list'][k]['object_id'])
      print(data['data']['list'][k]['object_name'])
      # print('********')
      
      # filename = 'novels_'+str(data['data']['list'][k]['object_id'])+'.json'
      if data['data']['list'][k]['object_id'] == 62:
        for novel in data['data']['list'][k]['object_list'][0]['list']:         
          novels.append({
              "ID": novel["novel_id"],
              "Name": novel["novel_name"],
              "Popularity": novel["novel_allpopu"],
              "Collection": novel["novel_allcoll"],
              "Timestamp": fetch_time 
          })
          print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'])
      with open('bobao.json', "w", encoding="utf-8") as file:
           json.dump(novels, file, ensure_ascii=False, indent=4)


