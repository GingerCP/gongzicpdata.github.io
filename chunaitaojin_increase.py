import requests
import json
from datetime import datetime, timedelta

# data_old =json.loads('chunaitaojin.json')
with open('chunaitaojin.json', 'r', encoding='utf-8') as f:
    data_old = json.load(f) 
increased_data = []
headers = {"User-Agent": "Mozilla/5.0"}
for novel in data_old:
  url = 'https://www.gongzicp.com/webapi/novel/novelInfo?id='+str(novel['ID'])
  old_popularity = novel['Popularity']
  old_collection = novel['Collection']
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
      text = response.text
      data = json.loads(text)
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
      text = response.text
      data = json.loads(text)
      # print(data)
      novel = data['data']
  # Print the HTML content in a formatted way
  # for novel in data['data']:
  increased_data.append({
      "ID": novel["novel_id"],
      "Name": novel["novel_name"],
      "Popularity": novel["novel_allpopu"] ,
      "Collection": novel["novel_allcoll"] ,
      "DeltaPopularity": novel["novel_allpopu"] - old_popularity,
      "DeltaCollection": novel["novel_allcoll"] - old_collection,
      "Timestamp": fetch_time  # Store fetch time
  })
  print(novel['novel_name'], novel['novel_id'], novel['novel_allpopu'], novel['novel_allpopu'])
  with open('chunaitaojin_increase.json', "w", encoding="utf-8") as file:
      json.dump(novels, file, ensure_ascii=False, indent=4)
