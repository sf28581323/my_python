import json

fn = 'populations.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)

jsondata1 = [obj for obj in getDatas if obj['Country Name'] != 'World']

for getData in jsondata1:
    if getData['Year'] == '2000':
        countryName = getData['Country Name']
        population = int(float(getData['Numbers']))
        print(countryName,
              '人口數 =',population)
        
jsondata2 = [obj for obj in getDatas if obj['Country Name'] == 'World']

for getData in jsondata2:
    if getData['Year'] == '2000':
        population = int(float(getData['Numbers']))
        print('人口總數 =',population)
