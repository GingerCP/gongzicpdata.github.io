import json
import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo  # Python 3.9+ required

# File where JSON data is stored
# JSON_FILE = "chunaitaojin.json"

# Function to load existing JSON data
def load_json(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Function to save JSON data
def save_json(data,filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Function to get the last Friday and this Thursday
def get_last_friday_and_this_thursday():
    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    today_weekday = now.weekday()  # Monday=0, ..., Sunday=6

    # Find last Friday (weekday=4)
    last_friday = now - timedelta(days=(today_weekday - 4) % 7 ) 

    # Find this Thursday (weekday=3)
    this_thursday = last_friday + timedelta(days=6) 

    return last_friday.strftime("%Y-%m-%d 00:00:00"), this_thursday.strftime("%Y-%m-%d 23:59:59")

def remove_duplicates(data):
    unique_data = {}
    for entry in data:
        unique_data[entry["ID"]] = entry  # Overwrites duplicate IDs, keeping the latest
    return list(unique_data.values())

def get_weekday_from_timestamp(timestamp_str):
    # Convert string timestamp to a datetime object (assuming UTC time)
    dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    # Convert to China Standard Time (CST, UTC+8)
    dt_cst = dt.replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("Asia/Shanghai"))

    # Get the weekday name (e.g., Monday, Tuesday)
    weekday_name = dt_cst.strftime("%A")  # Full name
    weekday_number = dt_cst.weekday()  # Monday=0, ..., Sunday=6

    return weekday_name, weekday_number

# Function to add new data while keeping only last Friday to this Thursday’s data
def update_json(new_entries, filename_hishtory):
    # print(len(new_entries))
    if load_json(filename_hishtory) == []:
      save_json(new_entries, filename_hishtory)
      print(f"✅ Updated  with {len(new_entries)} new records. Total records: {len(new_entries)}")
      return
    data = load_json(filename_hishtory)
    data = remove_duplicates(data)
    # print(len(data))
    # print('*********************')
    # for entry in data:
    #   print(entry["Name"])
    # Get current time in CST (China Standard Time)
    current_time = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S")

    # Append new entries with their own timestamps if missing
    for entry in new_entries:
        # print(entry["Name"])
        if "Timestamp" not in entry:
            entry["Timestamp"] = current_time
        data.append(entry)

    # Get the valid time range
    last_friday, this_thursday = get_last_friday_and_this_thursday()
    # print(last_friday, this_thursday)

    # Convert the time strings to datetime objects
    last_friday_dt = datetime.strptime(last_friday, "%Y-%m-%d %H:%M:%S")
    this_thursday_dt = datetime.strptime(this_thursday, "%Y-%m-%d %H:%M:%S")
    data = [
        entry for entry in data if last_friday_dt <= datetime.strptime(entry["Timestamp"], "%Y-%m-%d %H:%M:%S") <= this_thursday_dt
    ]

    # print(len(data))
    data = remove_duplicates(data)
    # print('**********all data************')
    # print(len(data))
    for entry in data:
        print(entry["Name"], entry["Timestamp"])
    # Save updated JSON file
    save_json(data, filename_hishtory)
    print(f"✅ Updated  with {len(new_entries)} new records. Total records: {len(data)}")

# Example: New data to add
new_data =  load_json('bobao.json')
# Run the update function
update_json(new_data, 'bobao_weekly.json')

new_data =  load_json('bidu.json')
# Run the update function
update_json(new_data, 'bidu_weekly.json')
