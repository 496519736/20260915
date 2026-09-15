# app.py
import os
import requests

def get_user_info(user_id):
    # 故意留一个不安全的代码：硬编码敏感信息
    api_key = "sk-1234567890-SECRET-KEY" 
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"},, timeout=10)
    return response.json()

def unused_function():
    # 故意写一个没有任何测试用例的函数
    return "这段代码没有被测试覆盖"
