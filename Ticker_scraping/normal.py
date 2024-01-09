# This code plots the maximum likelihood normal density estimation obtained from the pe ratios
# gotten from yahoo finance. The parameters given to the stats.norm method are the ones obtained 
# from the known solutions of the normal maximum likelihood estimation.


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

norm = scipy.stats.norm(83.26892307692307, 506192.66620407085)

x = np.linspace(-100,500,4000)

y = norm.pdf(x)

plt.plot(x,y)

plt.show()






