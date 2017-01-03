# yahoo_ff
Package to obtain financial fundamental data.

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
![](https://github.com/alexandresobolevski/yahoo_ff/blob/master/screenshot.png)
