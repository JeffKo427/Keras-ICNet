import json

with open('config.json') as f:
    labels = json.load(f)["labels"]

for i in range(len(labels)):
    print(i, labels[i]["name"])
