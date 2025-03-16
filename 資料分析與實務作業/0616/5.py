import matplotlib.pyplot as plt
sorts = ["America", "Australia", "Japan", "Europe", "United Kingdom"]
fee = [10543,2105,1190,3346,980]

plt.pie(fee,labels=sorts,explode=(0,0,0.3,0,0), autopct="%1.2f%%")
plt.show()
