import sys
import urllib2
import json
from collections import OrderedDict

def get_stock_info(symbol, data):
    stock_info = OrderedDict()

    stock_info["symbol"] = symbol
    stock_info["currency"] = data['financialCurrency']
    stock_info["currentPrice"] = data['currentPrice']['fmt'] if 'fmt' in data['currentPrice'] else "NA"
    stock_info["totalRevenue"] = data['totalRevenue']['fmt'] if 'fmt' in data['totalRevenue'] else "NA"
    stock_info["ebitda"] = data['ebitda']['fmt'] if 'fmt' in data['ebitda'] else "NA"
    stock_info["cashPerShare"] = data['totalCashPerShare']['fmt'] if 'fmt' in data['totalCashPerShare'] else "NA"
    stock_info["debtToEquity"] = data['debtToEquity']['fmt'] if 'fmt' in data['debtToEquity'] else "NA"
    stock_info["revenuePerShare"] = data['revenuePerShare']['fmt'] if 'fmt' in data['revenuePerShare'] else "NA"
    stock_info["grossProfits"] = data['grossProfits']['fmt'] if 'fmt' in data['grossProfits'] else "NA"
    stock_info["grossMargins"] = data['grossMargins']['fmt'] if 'fmt' in data['grossMargins'] else "NA"
    stock_info["operatingMargins"] = data['operatingMargins']['fmt'] if 'fmt' in data['operatingMargins'] else "NA"
    stock_info["profitMargins"] = data['profitMargins']['fmt'] if 'fmt' in data['profitMargins'] else "NA"
    stock_info["ebitdaMargins"] = data['ebitdaMargins']['fmt'] if 'fmt' in data['ebitdaMargins'] else "NA"
    
    return stock_info

def main():
    if len (sys.argv) != 3 :
        print "Usage: python stock_quote.py <SYMBOL> <EXCHANGE>"
        sys.exit(1)

    symbol = sys.argv[1]
    exchange = sys.argv[2]
    url = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/{0}.{1}?&modules=financialData".format(symbol, exchange)
    response = urllib2.urlopen(url)
    html = response.read()
    d = json.loads(html)

    data = d['quoteSummary']['result'][0]['financialData']
    stock_info = get_stock_info(symbol, data)

    print(json.dumps(stock_info, indent=4))

if __name__ == "__main__":
    main()
