import requests 
import json
import hashlib
import time
import random
import requests
import json
from urllib.parse import urlparse, parse_qs, urlencode
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs, urlencode
from request_key import generate_request_key

key = "fss≤Â˜ı≥fhggh*&^%^ÇÏÍÎÍADΩ≈Ç≈√"
imei = ""
version = "android_020701"
token = ""

def send_gongzicp_request(url, imei, version, extra_data, token):
    timestamp = str(int(time.time()))
    nonce = str(random.randint(10 ** 15, 10 ** 16 - 1))
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    request_key = generate_request_key(query_params, timestamp, nonce, imei, version, extra_data)
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Host": parsed_url.netloc,
        "User-Agent": "chang pei yue du/2.7.1 (Android 12; SM-A5260; Samsung)",
        "client": "android",
        "imei": imei,
        "nonce": nonce,
        "referer": "https://www.gongzicp.com",
        "requestKey": request_key,
        "timestamp": timestamp,
        "token": token,
        "version": version
    }

    response = requests.get(url, headers=headers)
    return response.status_code, response.text