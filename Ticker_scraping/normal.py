import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

norm = scipy.stats.norm(83.26892307692307, 506192.66620407085)

x = np.linspace(-100,500,4000)

y = norm.pdf(x)

plt.plot(x,y)

plt.show()






