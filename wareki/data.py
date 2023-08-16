import csv
from datetime import date, timedelta
import pprint
import pkg_resources

gengo = []
koyomi = []
dates = {}
dates_list = []

gengo_path = pkg_resources.resource_filename("wareki", "data/gengo.csv")
koyomi_path = pkg_resources.resource_filename("wareki", "data/koyomi.csv")

with open(gengo_path) as f:
    reader = csv.reader(f)
    for row in reader:
        gengo.append(row)

with open(koyomi_path) as f:
    reader = csv.reader(f)
    for row in reader:
        koyomi.append(row)

for row in koyomi:
    x = row[0].replace('/', '-')
    d = date.fromisoformat(x)
    dates_list.append(d)
    row.append(d)
    dates[d.strftime('%Y-%m-%d')] = row

def print_koyomi():
    pprint.pprint(koyomi)

def print_gengo():
    pprint.pprint(gengo)

def get_koyomi_date(target_date):
    date = None
    if isinstance(target_date, str):
        date = dates[target_date]
    else:
        target = target_date.strftime('%Y-%m-%d')
        date = dates[target]
    return date

def find_close_date(target):
    target = date.fromisoformat(target)
    close = min(dates_list, key=lambda d: abs(target - d))
    x = dates_list.index(close)
    if target < close:
        x -= 1
        close = dates_list[x]

    return get_koyomi_date(close)

#find_close_date('1786-12-23', koyomi)
