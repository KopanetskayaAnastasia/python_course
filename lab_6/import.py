import json

with open("workers.json", 'r', encoding='UTF-8') as f:
 data = json.load(f)


print(data)

