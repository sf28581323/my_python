import matplotlib.pyplot as plt
import numpy as np

left = -10
right = 10
x = np.linspace(left, right, 100)   #使用linspace()產生陣列

f1 = x
f2 = x**2
f3 = x**3
f4 = x**4

plt.subplot(2, 2, 1)    #子圖1
plt.plot(x, f1)
plt.subplot(2, 2, 2)    #子圖2
plt.plot(x, f2)
plt.subplot(2, 2, 3)    #子圖3
plt.plot(x, f3)
plt.subplot(2, 2, 4)    #子圖4
plt.plot(x, f4)
plt.show()
