import requests
import json
import pandas as pd
from datetime import datetime, timedelta

# Convert UTC time to China Standard Time (CST)
def get_china_time():
    return (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")



def fetch_data():
    url = "https://www.gongzicp.com/webapi/novel/novelGetList?page=1&size=10&tid=75&field=4&order=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://www.gongzicp.com/home/indexRanking?rid=2&tid=0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        novels = []

        for novel in data['data']['list']:
            novels.append({
                "ID": novel["novel_id"],
                "Name": novel["novel_name"],
                "Popularity": novel["novel_allpopu"],
                "Collection": pre_novel["novel_allcoll"]
            })

        # Save data to JSON
        with open("output_data.json", "w", encoding="utf-8") as file:
            json.dump(novels, file, ensure_ascii=False, indent=4)

        print("✅ Data successfully saved to output_data.json")
    else:
        print("❌ Failed to fetch data. Status Code:", response.status_code)



def get_recent_updates():
  novels = []
  for page in range(0,1):
    print(page/50)
    url = "https://gongzicp.com/webapi/novel/novelGetList?page="+str(page)+"&size=10&tid=75&field=4&order=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://www.gongzicp.com/home/indexRanking?rid=2&tid=0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.text
        data = json.loads(text)
        # print(data['data']['list'][0])
        # list_novel = data["data"]['recList']['bzlj']['list']
        for novel in data['data']['list']:
            # # print(novel["novel_id"],novel["novel_name"],novel["novel_allpopu"])
            # all_pop.append(novel["novel_allpopu"])
            # IDs.append(novel["novel_id"])
            # names.append(novel["novel_name"])

            url2 ='https://www.gongzicp.com/webapi/novel/novelInfo?id='+ str(novel["novel_id"]) +' HTTP/1.1'
            fetch_time = get_china_time()
            response = requests.get(url2)
            web_content = response.text
            pre_novel = json.loads(web_content)['data']
            novels.append({
                "ID": novel["novel_id"],
                "Name": novel["novel_name"],
                "Popularity": novel["novel_allpopu"],
                "Collection":  pre_novel["novel_allcoll"],
                "Timestamp": fetch_time  # Store fetch time
            })
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
    with open("output_data.json", "w", encoding="utf-8") as file:
        json.dump(novels, file, ensure_ascii=False, indent=4)

      
if __name__ == "__main__":
    get_recent_updates()
