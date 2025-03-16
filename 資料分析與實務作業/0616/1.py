import matplotlib.pyplot as plt

Benz = [3367, 4120, 5539, 6020, 6620]
BMW  = [4000, 3590, 4423, 4900, 4590]
Lexus = [5200, 4930, 5350, 6200, 6930]

seq = [2018, 2019, 2020, 2021, 2022]
plt.xticks(seq)
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout(pad=7)
plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()
