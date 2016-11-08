import numpy as np

BASE_URL = 'https://ca.finance.yahoo.com/'
date_string_length = 12

FIELDS = {'INFO': {}, 'KEY_STATS': {}, 'REPORTS': {'is': [], 'bs': [], 'cf': []}}
try:
    from params import PARAMS
    FIELDS['INFO'] = PARAMS['INFO']
    FIELDS['KEY_STATS'] = PARAMS['KEY_STATS']
    FIELDS['REPORTS']['is'] = dict(filter(lambda x: x[1]['report'] == 'is', np.array(PARAMS['REPORTS'].items()))).keys()
    FIELDS['REPORTS']['cf'] = dict(filter(lambda x: x[1]['report'] == 'cf', np.array(PARAMS['REPORTS'].items()))).keys()
    FIELDS['REPORTS']['bs'] = dict(filter(lambda x: x[1]['report'] == 'bs', np.array(PARAMS['REPORTS'].items()))).keys()
except ImportError:
    # default PARAMS
    FIELDS = {
        'INFO': [
            'Sector',
            'Industry',
            'Full Time Employees'
        ],
        'KEY_STATS': [
            'Market Cap (intraday)',
            'Trailing P/E (ttm, intraday)',
            'Forward P/E',
            'PEG Ratio (5 yr expected)',
            'Price/Sales (ttm)',
            'Price/Book (mrq)',
            'Enterprise Value/Revenue (ttm)',
            'Enterprise Value/EBITDA (ttm)',
            'Fiscal Year Ends',
            'Most Recent Quarter (mrq)',
            'Profitability',
            'Profit Margin (ttm)',
            'Operating Margin (ttm)',
            'Return on Assets (ttm)',
            'Return on Equity (ttm)',
            'Revenue (ttm)',
            'Revenue Per Share (ttm)',
            'Qtrly Revenue Growth (yoy)',
            'Gross Profit (ttm)',
            'EBITDA (ttm)',
            'Net Income Avl to Common (ttm)',
            'Diluted EPS (ttm)',
            'Qtrly Earnings Growth (yoy)',
            'Total Cash (mrq)',
            'Total Cash Per Share (mrq)',
            'Total Desbt (mrq)',
            'Total Debt/Equity (mrq)',
            'Current Ratio (mrq)',
            'Book Value Per Share (mrq)',
            'Operating Cash Flow (ttm)',
            'Levered Free Cash Flow (ttm)',
            'Float',
            'Held by Insiders',
            'Held by Institutions',
            'Shares Short',
            'Short Ratio',
            'Beta'
        ],
        'REPORTS': {
            'is' : [
                'Total Revenue',
                'Cost of Revenue',
                'Gross Profit',
                'Research Development',
                'Selling General and Administrative',
                'Non Recurring',
                'Total Operating Expenses',
                'Total Other Income/Expenses Net',
                'Earnings Before Interest And Taxes',
                'Interest Expense',
                'Income Before Tax',
                'Income Tax Expense',
                'Minority Interest',
                'Net Income From Continuing Ops',
                'Discontinued Operations',
                'Extraordinary Items',
                'Effect Of Accounting Changes',
                'Other Items',
                'Net Income Applicable To Common Shares'
            ],
            'bs': [
                'Cash And Cash Equivalents',
                'Short Term Investments',
                'Net Receivables',
                'Inventory',
                'Other Current Assets',
                'Total Current Assets',
                'Long Term Investments',
                'Property Plant and Equipment',
                'Goodwill',
                'Intangible Assets',
                'Accumulated Amortization',
                'Other Assets',
                'Deferred Long Term Asset Charges',
                'Total Assets',
                'Accounts Payable',
                'Short/Current Long Term Debt',
                'Other Current Liabilities',
                'Total Current Liabilities',
                'Long Term Debt',
                'Other Liabilities',
                'Deferred Long Term Liability Charges',
                'Minority Interest',
                'Negative Goodwill',
                'Total Liabilities',
                'Misc Stocks Options Warrants',
                'Redeemable Preferred Stock',
                'Preferred Stock',
                'Common Stock',
                'Retained Earnings',
                'Treasury Stock',
                'Capital Surplus',
                'Other Stockholder Equity',
                'Total Stockholder Equity',
                'Net Tangible Assets'
            ],
            'cf': [
                'Depreciation',
                'Adjustments To Net Income',
                'Changes In Accounts Receivables',
                'Changes In Liabilities',
                'Changes In Inventories',
                'Changes In Other Operating Activities',
                'Total Cash Flow From Operating Activities',
                'Capital Expenditures',
                'Investments',
                'Other Cash flows from Investing Activities',
                'Total Cash Flows From Investing Activities',
                'Dividends Paid',
                'Sale Purchase of Stock',
                'Net Borrowings',
                'Other Cash Flows from Financing Activities',
                'Effect Of Exchange Rate Changes',
                'Change In Cash and Cash Equivalents'
            ]
        }
    }


inf_fields = FIELDS['INFO'].keys()
ks_fields = FIELDS['KEY_STATS'].keys()
is_fields = FIELDS['REPORTS']['is']
bs_fields = FIELDS['REPORTS']['bs']
cf_fields = FIELDS['REPORTS']['cf']
