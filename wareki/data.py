import csv
from datetime import date, timedelta
import pprint

gengo = []
koyomi = []


with open('data/gengo.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        gengo.append(row)

with open('data/koyomi.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        koyomi.append(row)

pprint.pprint(koyomi)
for row in koyomi:
    x = row[0].replace('/', '-')
    d = date.fromisoformat(x)
    row.append(d)


def find_close_date(target, data):
    flat_list = [sublist[6] for sublist in data]
    target = date.fromisoformat(target)

    close = min(flat_list, key=lambda d: abs(target - d))
    print(close)

find_close_date('1786-12-23', koyomi)
