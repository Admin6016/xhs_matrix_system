import requests
import json

url = "http://redapi.cn/api/external-api/publish"
headers = {
    "X-API-Key": "YOUR_API_KEY",
    "Content-Type": "application/json"
}

data = {
    "account_id": 123,
    "title": "分享一道超好吃的家常菜",
    "content": "今天给大家分享一道简单易做的家常菜，味道超级棒！材料准备：\n1. 鸡蛋 3个\n2. 西红柿 2个\n3. 葱花适量\n\n制作步骤：...\n\n#美食 #家常菜 #简单易做",
    "image_urls": [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg"
    ],
    "topics": ["美食", "家常菜", "简单易做"],
    "scheduled_at": "2024-01-15 18:00:00"
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

if result["code"] == 200:
    task_id = result["data"]["task_id"]
    print(f"发布成功，任务ID: {task_id}")
    print(f"预计发布时间: {data['scheduled_at']}")
else:
    print(f"发布失败: {result['message']}")
