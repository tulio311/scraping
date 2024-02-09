# Ticker scraper

This is a code that gets the PE ratios and the Cap of the s&p 500 tickers from the yahoo finance web page. It manages the error of not being able to find a ticker web page and create a list of the found information. The information is in the `datos.csv` file. the `tickers.csv` file has the list of tickers in order to use them for this web scraping.

We calculate also the normal maximum likelihood estimation given by the PE ratios obtained from the web scraping. The parameters are calculated in `parameters.py` and the density is plotted in `normal.py`. This density turned out to be extremely wide and it provides not very useful information. 
