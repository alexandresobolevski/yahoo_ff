# yahoo_ff
Package to obtain financial fundamental data from yahoo.com/finance webiste. Returns the balance sheet, income statement, cashflow, key statistics, price and other infos.

## Requirements
```
pip install -r requirements.txt
```

## Installation
```
$ pip install yahoo_ff

```

## Using

### A single stock
```
from yahoo_ff.yahoo_ff import yahoo_ff
aapl = yahoo_ff('aapl')
```
will create an object from which several Pandas DataFrames of interest can be extracted
```
quarterlySECreports = aapl.qr()
annualSECreports = aapl.ar()
keyStatsOfTheDay = aapl.ks()
infoAboutCompany = aapl.inf()
priceOfTheDay = aapl.pr()
```

this is an example for apple's last 3 years of financial data (70 rows)
![](https://github.com/alexandresobolevski/yahoo_ff/blob/master/screenshot.png)
