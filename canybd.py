import requests
import json
from datetime import datetime, timedelta
# Convert UTC time to China Standard Time (CST)
def get_china_time():
    return (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
headers = {"User-Agent": "Mozilla/5.0"}    
novel_rank = []
identifiers = ['xsjxyc', 'ybzsyc', 'yccqs', 'ycgd' ,'ycxdds','ychx','ycxy', 'ycjk','qgrzyc','bzxbyc','ycxdzh','ycxdqc']
names = ['新书精选','鱼宝赞赏','长篇热读','纯爱古代','纯爱都市','纯爱幻想','纯爱悬疑','纯爱架空','勤更热追','本周寻宝','纯爱综合','纯爱青春']
for identifier in identifiers:
  if identifier in ['ycxdzh', 'ycxdds','ycxdqc']:
    tid = 1
  else:
    tid = 75
    
  url = 'https://gongzicp.com/webapi/home/recommendList?identifier='+identifier + f'&tid={tid}&swap=0&style_id=7'
  fetch_time = get_china_time()
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
      text = response.text
      data_all = json.loads(text)
      # print(data_all['data'])
      print(names[identifiers.index(identifier)])
      novels = []
      for novel in data_all['data']:
        # print(novel)
        # print(novel["novel_id"], novel['novel_name'], novel['novel_allpopu'])
        novels.append({
        "ID": novel["novel_id"],
        "Name": novel["novel_name"],
        "Popularity": novel["novel_allpopu"],
        "Collection": novel["novel_allcoll"],
        "Timestamp": fetch_time
    })
      novel = min(novels, key=lambda x: x["Popularity"])
      print(novel)
      print("🔥 最热小说:", novel['Name'], novel['ID'],novel['Collection'])
      novel_rank.append({'rank_name': names[identifiers.index(identifier)],
                          "ID": novel["ID"],
                          "Name": novel["Name"],
                          "Popularity": novel["Popularity"],
                          "Collection": novel["Collection"],
                          "Timestamp": novel['Timestamp']})
with open('canybd.json', "w", encoding="utf-8") as file:
      json.dump(novel_rank, file, ensure_ascii=False, indent=4)
