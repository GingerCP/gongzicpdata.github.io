import json

FILENAME = "query_results.json"

# ✅ Load existing JSON data
try:
    with open(FILENAME, "r", encoding="utf-8") as f:
        query_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    query_data = {}

# ✅ Simulate new data from the frontend (this part should be modified)
new_data = {
    "input-1": "12345",
    "output-1": "📖 Example Book | 📂 100 收藏 | 🔥 5000 热度"
}

# ✅ Merge new data into existing data
query_data.update(new_data)

# ✅ Save updated JSON
with open(FILENAME, "w", encoding="utf-8") as f:
    json.dump(query_data, f, ensure_ascii=False, indent=4)

print("✅ query_results.json 已更新!")
