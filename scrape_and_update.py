import requests
import json
import pandas as pd

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
                "Collection": novel.get("novel_allcoll", "N/A")
            })

        # Save data to JSON
        with open("output_data.json", "w", encoding="utf-8") as file:
            json.dump(novels, file, ensure_ascii=False, indent=4)

        print("✅ Data successfully saved to output_data.json")
    else:
        print("❌ Failed to fetch data. Status Code:", response.status_code)

if __name__ == "__main__":
    fetch_data()
