import requests
from bs4 import BeautifulSoup
import json

# ✅ 替换为你的腾讯文档 URL
DOCUMENT_URL = "https://docs.qq.com/sheet/DWVhxTEJqU1FWbWtS"

# ✅ 发送 HTTP 请求获取 HTML 页面
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(DOCUMENT_URL, headers=headers)

# ✅ 解析 HTML
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # ✅ 查找表格（可能需要调整选择器）
    table = soup.find("table")  # 这里的 `table` 可能需要手动检查
    if table:
        rows = table.find_all("tr")

        data = []
        for row in rows:
            cells = row.find_all(["th", "td"])  # 兼容表头和数据
            row_data = [cell.get_text(strip=True) for cell in cells]
            data.append(row_data)

        # ✅ 存入 JSON 文件
        with open("tencent_doc_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("✅ 数据已成功保存到 tencent_doc_data.json！")
    else:
        print("❌ 没有找到表格，请检查 HTML 结构")
else:
    print(f"❌ 请求失败，状态码: {response.status_code}")
