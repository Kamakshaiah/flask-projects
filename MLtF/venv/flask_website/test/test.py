from bokeh.embed import components
import random
import matplotlib.pyplot as plt

x = list(range(10))
y = list(range(10))

random.shuffle(x, random.random)
random.shuffle(y, random.random)

x1 = list(range(10))
y1 = list(range(10))

print(x1)

plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.subplot(2, 1, 2)
plt.plot(x1, y1)
plt.show()

