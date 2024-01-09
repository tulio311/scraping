from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

import sys


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

# if there are no CLI parameters
if len(sys.argv) <= 1:
    print('Ticker symbol CLI argument missing!')
    sys.exit(2)

# read the ticker from the CLI argument
ticker_symbol = sys.argv[1]

# build the URL of the target page
url = f'https://finance.yahoo.com/quote/{ticker_symbol}'

driver.get(url)



pe_ratio = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="PE_RATIO-value"]').text


stock = {}

# stock price scraping logic omitted for brevity...

# add the scraped data to the dictionary

stock['pe_ratio'] = pe_ratio


print(stock)










# close the browser and free up the resources
driver.quit()
