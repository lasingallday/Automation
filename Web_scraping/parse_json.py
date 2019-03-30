import json

metadata = '/Users/you/Documents/practice_web_scraping.json'
data = json.loads(open(metadata).read())

for i in data:
    print i['district'].encode("utf-8"),i['state'].encode("utf-8")
