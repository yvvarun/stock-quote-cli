# stock-quote-cli

> Real time stock data retrieved from yahoo finance.

## Info

Supports all the Exchanges listed on yahoo finance.

Yahoo finance provides stock price and details for stocks using a particular Id and extension. For instance, Hdfc Bank Ltd. listed in NSE(National Stock Exchange India) has symbol as HDFCBANK and extension as NS. Similarly, in BSE the symbol is same but the extension is BO. Please check the Usage section for more detailed usage.

You can get the list of exchanges from the following URL:
```
https://help.yahoo.com/kb/SLN2311.html
```

## Install
```
pip install stock-quote-cli
```
## Usage
```
stock <SYMBOL> <EXCHANGE>
<EXCHANGE> to be provided only if the stock is not listed on NYSE
```

To get stock quote of Google listed in NASDAQ, use the following code snippet:

```
stock GOOGL
```

To get stock quote of Biocon listed in Bombay Stock Exchange, use the following code snippet:

```
stock BIOCON BO
```

You can get the list of exchanges from the following URL:
```
https://help.yahoo.com/kb/SLN2310.html
```


## Data Format
The data returned when the promise is resolved will have the following format:

{  
    "symbol": "GOOGL",  
    "currency": "USD",  
    "currentPrice": "1,217.41",  
    "totalRevenue": "123.9B",  
    "ebitda": "38.21B",  
    "cashPerShare": "146.99",  
    "currentRatio": "4.15",  
    "quickRatio": "4.00",  
    "debtToEquity": "2.46",  
    "revenuePerShare": "178.41",  
    "grossProfits": "65.27B",  
    "grossMargins": "57.41%",  
    "operatingMargins": "24.48%",  
    "profitMargins": "13.16%",  
    "ebitdaMargins": "30.84%"  
}
