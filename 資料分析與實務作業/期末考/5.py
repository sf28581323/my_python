import csv
import matplotlib.pyplot as plt
import numpy as np

fn = 'input.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)

banana = [18.1, 19.5, 21, 17.4, 16.9, 18, 16.3]

seq = [listReport[0][0], listReport[1][0], listReport[2][0], listReport[3][0],
       listReport[4][0], listReport[5][0], listReport[6][0]]

plt.plot(seq, banana, label = 'banana')
plt.legend(loc='upper right')
plt.title("Market Average Price")
plt.xlabel("date")
plt.ylabel("NT$")
plt.tick_params(axis='both',labelsize=12)
plt.show()
