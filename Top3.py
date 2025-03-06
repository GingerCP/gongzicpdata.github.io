import requests
import json
from datetime import datetime, timedelta
# Convert UTC time to China Standard Time (CST)
def get_china_time():
    return (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
headers = {"User-Agent": "Mozilla/5.0"}
novel_rank = []

def find_novel_list_by_identifier(identifier, tid, style_id, recpage = 0, swap = 0):
  url = 'https://gongzicp.com/webapi/home/recommendList?identifier='+identifier + f'&tid={tid}&swap={swap}&style_id={style_id}'
  print(url)
  print(identifier)
  if identifier =='cxrz':
    url = f'https://www.gongzicp.com/webapi/home/recommendList?identifier=cxrz&tid=0&rec_page={recpage}&style_id=2'
  fetch_time = get_china_time()
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
      text = response.text
      data_all = json.loads(text)
      print(data_all['data'])
      print(names[identifiers.index(identifier)])
      novels = []
      for novel in data_all['data']:
        # print(novel)
        print(novel["novel_id"], novel['novel_name'], novel['novel_allpopu'])
        novels.append({
        "ID": novel["novel_id"],
        "Name": novel["novel_name"],
        "Popularity": novel["novel_allpopu"],
        "Collection": novel["novel_allcoll"],
        "Timestamp": fetch_time
    })
  return novels
# identifiers = ['bzqtyc','xsjxyc', 'ybzsyc', 'yccqs', 'ycgd' ,'ycxdds','ychx','ycxy', 'ycjk','qgrzyc','bzxbyc','ycxdzh','ycxdqc']
# names = ['本周强推','新书精选','鱼宝赞赏','长篇热读','纯爱古代','纯爱都市','纯爱幻想','纯爱悬疑','纯爱架空','勤更热追','本周寻宝','纯爱综合','纯爱青春']
identifiers = ['bzlj', 'cxrz', 'qltj']
names = ['本周力荐','畅销热追','人气飙升']
for identifier in identifiers:
  if identifier =='yctj':
    tid = 75
    style_id = 7
    novels = find_novel_list_by_identifier(identifier, tid, style_id)
  elif identifier == 'cxrz':
    tid = 0
    style_id = 2
    novels = []
    for recpage in range(1,4):
      novels = novels + find_novel_list_by_identifier(identifier, tid, style_id, recpage = recpage)

  elif identifier == 'zyyc':
    tid = 75
    style_id = 7
    for swap in range(1,6):
      print(swap)
      novels = find_novel_list_by_identifier(identifier, tid = tid, style_id = style_id, swap =swap)
      continue
  else:
    tid = 0
    style_id = 1
    novels = find_novel_list_by_identifier(identifier, tid, style_id)
  with open( identifier + '.json', "w", encoding="utf-8") as file:
      json.dump(novels, file, ensure_ascii=False, indent=4)
