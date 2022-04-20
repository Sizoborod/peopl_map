import sys
import csv
import json

s = 'people.csv'
print(s)
ss = { "type": "FeatureCollection",
    "features": []}
with open(s, encoding="utf8") as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))[1:]
    for i in reader:
        coord = list(map(float, i[5].split(', ')))
        print(coord)
        p = {"type": "Feature", "id": int(i[0]),
             "geometry": {"type": "Point", "coordinates": coord},
             "properties": {"balloonContentHeader": f"{i[1]}", "balloonContentBody": f"{i[2]} \n {i[3]}", "balloonContentFooter": f"{i[6]}", "clusterCaption": f"{i[1]}", "hintContent": f"{i[1]}"}}
        print(p)
        ss['features'].append(p)
print(ss)

with open('static/js/data.json', 'w', encoding="utf-8") as cat_file:
    json.dump(ss, cat_file)

