import csv

fn = 'csvReport.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)

revenue1 = int(listReport[1][5])+int(listReport[2][5])+int(listReport[5][5])+int(listReport[7][5])+int(listReport[8][5])
revenue2 = int(listReport[3][5])+int(listReport[4][5])+int(listReport[6][5])+int(listReport[9][5])+int(listReport[10][5])

print('Total Revenue of 2015 =',revenue1)
print('Total Revenue of 2016 =',revenue2)
