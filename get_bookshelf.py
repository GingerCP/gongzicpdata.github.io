import requests
import json

# ✅ 替换为你的 API Key
APP_ID = "your_app_id"
SECRET_KEY = "your_secret_key"
DOCUMENT_ID = "your_doc_id"

def set_edit_permission(password):
    url = f"https://docs.qq.com/openapi/docs/{DOCUMENT_ID}/permissions"
    headers = {
        "Authorization": f"Bearer {SECRET_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "password": password,  # 设置密码
        "editable_ranges": [
            {"startRowIndex": 0, "endRowIndex": 5, "startColIndex": 0, "endColIndex": 2}
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("✅ 编辑权限已设置！")
    else:
        print("❌ 设置失败，错误信息：", response.text)

# 运行函数
set_edit_permission("mypassword123")
