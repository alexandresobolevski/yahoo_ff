import time
import json
import datetime
import pandas as pd

from yahoo_ff.tools.constants import *
from yahoo_ff.tools.scrapingTools import *

today = getUnixTime(pd.to_datetime('today'))

class yahoo_ff:
    '''
    ra(): annual reports
    rq(): quarterly reports
    ks(): key stats
    inf(): company infos
    pr(): today's price
    '''

    sleep = 0.5 # being a good citizen and not overusing the API

    def __init__(self, ticker):
            self.flag = 0
            self.ticker = ticker
            self.__wait()
            self.__construct_is_annual()
            self.__wait()
            self.__construct_is_quarterly()
            self.__wait()
            self.__construct_bs_annual()
            self.__wait()
            self.__construct_bs_quarterly()
            self.__wait()
            self.__construct_cf_annual()
            self.__wait()
            self.__construct_cf_quarterly()
            self.__wait()
            self.__construct_company_info()
            self.__wait()
            self.__construct_key_stats()
            print('flag is ' + str(self.flag))

    def __construct_is_annual(self):
        '''
        populate self.ra
        '''
        try:
            html = get_source_code(get_annual_is_url(self.ticker)).split('Get Income Statement for:')[1]
            self.is_annual = self.__get_endofperiod(html)
            for field in is_fields:
                self.is_annual[field] = scrape_report(html, field)
            print('Annual income statement for ' + str(self.ticker) + ' successfuly obtained')
        except Exception as e:
            self.flag = 1
            print('failed construct_is_annual for ' + self.ticker + '; ' + str(e))

    def __construct_is_quarterly(self):
        '''
        populate self.rq
        '''
        try:
            html = get_source_code(get_quarterly_is_url(self.ticker)).split('Get Income Statement for:')[1]
            self.is_quarterly = self.__get_endofperiod(html)
            for field in is_fields:
                self.is_quarterly[field] = scrape_report(html, field)
            print('Quarterly income statement for ' + str(self.ticker) + ' successfuly obtained')
        except Exception as e:
            self.flag = 1
            print('failed construct_is_quarterly for ' + self.ticker + '; ' + str(e))

    def __construct_bs_annual(self):
        '''
        populate self.bs_annual
        '''
        try:
            html = get_source_code(get_annual_bs_url(self.ticker)).split('Get Balance Sheet for:')[1]
            self.bs_annual = self.__get_endofperiod(html)
            for field in bs_fields:
                self.bs_annual[field] = scrape_report(html, field)
            print('Annual balance sheet for ' + str(self.ticker) + ' successfuly obtained')
        except Exception as e:
            self.flag = 1
            print('failed construct_bs_annual for ' + self.ticker + '; ' + str(e))

    def __construct_bs_quarterly(self):
        '''
        populate self.bs_quarterly
        '''
        try:
            html = get_source_code(get_quarterly_bs_url(self.ticker)).split('Get Balance Sheet for:')[1]
            self.bs_quarterly = self.__get_endofperiod(html)
            for field in bs_fields:
                self.bs_quarterly[field] = scrape_report(html, field)
            print('Quarterly balance sheet for ' + str(self.ticker) + ' successfuly obtained')
        except Exception as e:
            self.flag = 1
            print('failed construct_bs_quarterly for ' + self.ticker + '; ' + str(e))

    def __construct_cf_annual(self):
        '''
        populate self.cf_annual
        '''
        try:
            html = get_source_code(get_annual_cf_url(self.ticker)).split('Get Cash Flow for:')[1]
            self.cf_annual = self.__get_endofperiod(html)
            for field in cf_fields:
                self.cf_annual[field] = scrape_report(html, field)
            print('Annual Cash Flows for ' + str(self.ticker) + ' successfuly obtained')
        except Exception as e:
            self.flag = 1
            print('failed construct_cf_annual for ' + self.ticker + '; ' + str(e))

    def __construct_cf_quarterly(self):
        '''
        populate self.cf_quarterly
        '''
        try:
            html = get_source_code(get_quarterly_cf_url(self.ticker)).split('Get Cash Flow for:')[1]
            self.cf_quarterly = self.__get_endofperiod(html)
            for field in cf_fields:
                self.cf_quarterly[field] = scrape_report(html, field)
            print('Quarterly Cash Flows for ' + str(self.ticker) + ' successfuly obtained')
        except Exception as e:
            self.flag = 1
            print('failed construct_cf_quarterly for ' + self.ticker + '; ' + str(e))

    def __construct_company_info(self):
        '''
        get basic information on the stock (sector, industry, nb of employees
        '''
        self.company_infos = {}
        try:
            html = get_source_code(get_stockinfo_url(self.ticker))
            for field in inf_fields:
                self.company_infos[field] = scrape_company_infos(html, field)
            print('Company Info for ' + str(self.ticker) + ' successfuly obtained')

        except Exception as e:
            self.flag = 1
            print('failed construct_stockinfo for ' + self.ticker + '; ' + str(e))

    def __construct_key_stats(self):
        '''
        get key stats
        '''
        self.key_stats = {}
        try:
            html = get_source_code(get_keystats_url(self.ticker))
            for field in ks_fields:
                self.key_stats[field] = scrape_key_stats(html, field)
            print('Key Stats for ' + str(self.ticker) + ' successfuly obtained')

        except Exception as e:
            self.flag = 1
            print('failed construct_keystats for ' + self.ticker + '; ' + str(e))

    def __construct_price(self):
        '''
        get price
        '''
        try:
            html = get_source_code(get_keystats_url(self.ticker))
            self.current_price = get_current_price(html)
            print('Price for ' + str(self.ticker) + ' successfuly obtained')

        except Exception as e:
            self.flag = 1
            print('failed construct_price for ' + self.ticker + '; ' + str(e))

    def __get_endofperiod(self, html):
        '''
        scrape the html source code for the ending periods of each column
        '''
        source_code = html

        end_periods = source_code.split('Period Ending')[1]
        end_periods = end_periods.split('</TR>')[0]
        # take out unwanted html formatting
        end_periods = end_periods.replace(
            '<TD class="yfnc_modtitle1" align="right"><b>', '')
        end_periods = end_periods.replace('<th scope="col" style="border-top:2px solid '
                                          '#000;text-align:right; font-weight:bold">', '')
        end_periods = end_periods.replace('</span></small></td>', '')
        end_periods = end_periods.replace('</span></small></TD>', '')
        end_periods = end_periods.replace('</b>', '')
        end_periods = end_periods.split('</th>')
        # if '</th>' is not used to split periods
        if len(end_periods) == 1:
            end_periods = end_periods[0].split('</TD>')

        dates = [pd.to_datetime(x[-date_string_length:]) for x in end_periods if x is not '']
        dates = [getUnixTime(date) for date in dates]
        return {'Date': dates}

    def ar(self):
        '''
        package all annual info from is,
        blanacesheet and cf into a pandas
        dataframe
        '''
        isa = pd.DataFrame(self.is_annual)
        bsa = pd.DataFrame(self.bs_annual)
        csa = pd.DataFrame(self.cf_annual)
        df = pd.merge(isa, bsa, on='Date')
        df_packaged = pd.merge(df, csa, on='Date')
        df_packaged.set_index('Date', inplace=True)
        df_packaged = df_packaged
        return df_packaged

    def qr(self):
        '''
        package all quarterly info from is,
        blanacesheet and cf into a pandas
        dataframe
        '''
        isa = pd.DataFrame(self.is_quarterly)
        bsa = pd.DataFrame(self.bs_quarterly)
        csa = pd.DataFrame(self.cf_quarterly)
        df = pd.merge(isa, bsa, on='Date')
        df_packaged = pd.merge(df, csa, on='Date')
        df_packaged.set_index('Date', inplace=True)
        df_packaged = df_packaged
        return df_packaged

    def inf(self):
        '''
        package company company_infos as a pandas dataframe
        '''
        df = pd.DataFrame(self.company_infos)
        df['Date'] = today
        df = df.set_index(['Date'])
        return df

    def ks(self):
        '''
        package company key statistics as a pandas dataframe
        '''
        df = pd.DataFrame(self.key_stats)
        df['Date'] = today
        df = df.set_index(['Date'])
        return df

    def pr(self):
        '''
        price of the stock atm
        '''
        df = pd.DataFrame(self.current_price)
        df['Date'] = today
        df = df.set_index(['Date'])
        return df

    def __wait(self):
        time.sleep(yahoo_ff.sleep)
