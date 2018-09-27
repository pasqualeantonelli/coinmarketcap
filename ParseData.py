import requests
import json

url = 'http://finance.yahoo.com/quote/AAPL?p=AAPL'
#wikiURL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
#wikiResponse = requests.get(wikiURL)

response = requests.get(url)
# This will hold the names of all of the companies.
#data = {"Company": []}
data = {}


#print(wikiResponse.text.split("contains 505 stock")[1].split("0000915912")[0])
Indicators = { 'Previous Close':[],
               'Open':[],
               'Bid':[],
               'Ask':[],
               "Day&#x27;s Range":[],
               '52 Week Range':[],
               'Volume':[],
               'Avg. Volumes':[],
               'Market Cap':[],
               'Beta':[],
               'PE Ratio (TTM)':[],
               'EPS (TTM)':[],
               'Earnings Date':[],
               'Dividend &amp; Yield':[],
               'Ex-Divided Date':[],
               '1y Target Est':[] }
print(response)
print(response.status_code)

htmlText = response.text
for indicator in Indicators:
    print(indicator)
    splitList = htmlText.split(indicator)
    afterFirstSplit = splitList[0].split("\">")[0]
    afterSecondSplit = afterFirstSplit.split("</td>")
    dataValue = afterSecondSplit[0]
    Indicators[indicator].append(dataValue)

print(Indicators)
