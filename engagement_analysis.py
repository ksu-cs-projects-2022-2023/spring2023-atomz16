import json
from collections import Counter
import datetime

data = []
with open('kstate_comments.json', "r") as infile:
    data = json.load(infile)

dates = []
for comment in data:
    datetime_obj = datetime.datetime.utcfromtimestamp(comment['created_utc'])
    formatted_time = datetime_obj.strftime('%m-%d')
    dates.append(formatted_time)

counter = Counter(dates)

counts = 0
for element, count in counter.most_common():
    counts += 1
    print(str(element) + " " + str(count))

print(counts)