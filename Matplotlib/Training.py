import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1, '', ms=20, mec='', mfc='',ls ='-',c='y',lw='8',)
plt.plot(y2, '', ms=20, mec='', mfc='',ls ='-',c='b',lw='8',)
plt.show()