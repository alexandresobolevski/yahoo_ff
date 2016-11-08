import urllib2
import time
import numpy as np

from constants import BASE_URL

powers = {'%': 10 ** (-2), 'M': 10 ** 6, 'B': 10 ** 9, 'T': 10 ** 12}

def getUnixTime (dateTime):
    return int(time.mktime(dateTime.timetuple()))

def parse_powers(x):
    power = x[-1]
    if (power in powers.keys()):
        return float(x[:-1]) * powers[power]
    else :
        return x

def float_or_none(x):
    x = x.replace(',','')
    try:
        # if negative value (1000)
        if x[0]=='(' and x[-1]==')':
            return -float(x[1:-2])
        else:
            return float(x)
    except: return None

def scrape_report(source_code, information):
    return  parse_table(find_section(source_code, information))

def get_annual_is_url(stock):
    return BASE_URL + '/q/is?s=' + stock + '&annual'

def get_quarterly_is_url(stock):
    return BASE_URL + '/q/is?s=' + stock

def get_annual_bs_url(stock):
    return BASE_URL + '/q/bs?s=' + stock + '&annual'

def get_quarterly_bs_url(stock):
    return BASE_URL + '/q/bs?s=' + stock

def get_annual_cf_url(stock):
    return BASE_URL + '/q/cf?s=' + stock + '&annual'

def get_quarterly_cf_url(stock):
    return BASE_URL + '/q/cf?s=' + stock

def get_stockinfo_url(stock):
    return BASE_URL + '/q/pr?s=' + stock + '+Profile'

def get_keystats_url(stock):
    return BASE_URL + '/q/ks?s=' + stock

def get_source_code(url):
    return urllib2.urlopen(url).read()

def parse_table(source_code):
    source_code = source_code.split('</td></tr>')[0]
    source_code = source_code.replace('<strong>', '')
    source_code = source_code.replace('</strong>', '')
    source_code = source_code.replace('\n', '')
    source_code = source_code.replace('&nbsp;', '')
    source_code = source_code.replace('<td align="right">','')
    source_code = source_code.replace(' ', '')
    source_code = source_code.split('</td>')
    source_code = filter(None, source_code)
    return [float_or_none(x.replace(',', '')) for x in source_code]

def find_section(source_code, section_name):
    try:
        return source_code.split(section_name)[1]
    except:
        print 'failed acquiring ' + section_name

def scrape_company_infos(source_code, field):
    return [source_code.split(field+':')[1].split('</td>')[1].replace('</a>','').split('>')[-1]]

def scrape_key_stats(source_code, field):
    try:
        return [parse_powers(source_code.split(field)[1].split('</td></tr>')[0].replace('</span>', '').split('>')[-1])]
    except:
        return [np.nan]

def get_current_price(source_code):
    return {'Price': [float_or_none(source_code.split('time_rtq_ticker')[1].split('span')[1].split('>')[1].split('<')[0])]}
