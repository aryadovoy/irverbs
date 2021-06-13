import pandas as pd
import requests
import csv


url = 'https://pasttenses.com/irregular-verbs-list/'
d = {}
fields = ['Verb', 'Present Participle', 'Past', 'Past Participle']
for number in range(32):
    r = requests.get(url + str(number))
    df_list = pd.read_html(r.text)          # this parses all the tables in webpages to a list
    df = df_list[0]
    n = 0
    for i in df[fields[0]]:                 # make a dict
        d[i] = []
        d[i].extend([df[fields[1]][n], df[fields[2]][n], df[fields[3]][n]])
        n += 1
with open('db.csv', 'w', newline='') as f:  # write to file
    writer = csv.writer(f)
    writer.writerow(fields)
    for k in d.keys():
        writer.writerow([k, *d.get(k)])
