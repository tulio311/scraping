from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

import sys

import pandas as pd


# initialize a web driver instance to control a Chrome window
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

#driver.set_window_size(1920, 1080)

# scraping logic...

L1 = pd.read_csv("tickers.csv")
L = pd.Series(L1['Tickers'])

n = len(L1)


#print(L[0])

stock = []
cont=0


for i in range(n):

	

	ticker_symbol = L[i]
	print(str(i) +" "+ ticker_symbol)
	

	# build the URL of the target page
	url = f'https://finance.yahoo.com/quote/{ticker_symbol}'

	driver.get(url)


	try:
		pe_ratio = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="PE_RATIO-value"]').text
		market_cap = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="MARKET_CAP-value"]').text

		#stock[i][1] = pe_ratio
		#stock[i][2] = market_cap
		L2 = [ticker_symbol, pe_ratio, market_cap]
		stock.append(L2)
		cont += 1
		
	except:
		print(ticker_symbol + " fallo")
	
	
	
	#print(i)
	

# stock price scraping logic omitted for brevity...

# add the scraped data to the dictionary

Arr = pd.DataFrame(stock)
Arr.to_csv('datos.csv', index = False)




print(stock)









# close the browser and free up the resources
driver.quit()
