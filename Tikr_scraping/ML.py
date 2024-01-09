import numpy as np
import pandas as pd

Arr = pd.read_csv("datos.csv")
Arr.columns = ["Ticker","PE","Cap"]


pes = Arr.PE
n = len(pes)
var = 0

#print(pes[0])

mu = 0
cont = 0
for i in range(n):
	if not pd.isnull(pes[i]):
		cont += 1
		float(pes[i])
		mu += float(pes[i]) 
		#print(mu)
mu /= cont

for i in range(n):
	if not pd.isnull(pes[i]):
		
		var += (float(pes[i]) - mu)**2
		print(var)

var /= cont


print(mu,var)










