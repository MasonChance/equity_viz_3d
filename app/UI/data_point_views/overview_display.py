'''This file contains class definition and methods for parsing, storing, and rendering the results of calls to the "OVERVIEW" endpoint of the AlphaVantage API
'''

# Class instance should accept JSON as an argument
    # instance should be a PYTHON object. 
    # instance should have a method used for adding the result to the data base utilizing the corresponding database model in <dir: db_core_classes>

import json

class Overview:
    def __init__(self, model):
        """Initialization accepts a JSON object from the OVERVIEW endpoint of the AlphaVantage API and assigns corresponding key-value pairs to the instance

        Args:
            model (JSON:object): must be JSON from the OVERVIEW endpoint of the AlphaVantage API see local file <./app/tests/demo_assets/overview.json>

        Yields:
            <object: Overview>: Instance of Overview Class
        """
        model = json.loads(model)
        self.symbol = model['Symbol']
        self.asset_type = model['AssetType']
        self.name = model['Name']
        self.desc = model['Description']
        self.cik = model['CIK']
        self.exch = model['Exchange']
        self.currency = model['Currency']
        self.country = model['Country']
        self.sector = model['Sector']
        self.industry = model['Industry']
        self.address = model['Address']
        self.fisc_yr_end = model['FiscalYearEnd']
        self.latest_qtr = model['LatestQuarter']
        self.market_cap = model['MarketCapitalization']
        self.ebitda = model['EBITDA']
        self.p_e_ratio = model['PERatio']
        self.peg_ratio = model['PEGRatio']
        self.book_val = model['BookValue']
        self.div_per_share = model['DividendPerShare']
        self.div_yield = model['DividendYield']
        self.eps = model['EPS']
        self.rev_per_share_ttm = model['RevenuePerShareTTM']
        self.profit_margin = model['ProfitMargin']
        self.op_margin_ttm = model['OperatingMarginTTM']
        self.roa_ttm = model['ReturnOnAssetsTTM']
        self.roe_ttm = model['ReturnOnEquityTTM']
        self.rev_ttm = model['RevenueTTM']
        self.gross_ttm = model['GrossProfitTTM']
        self.dilute_eps_ttm = model['DilutedEPSTTM']
        self.qtl_earn_growth_yoy = model['QuarterlyEarningsGrowthYOY']
        self.qtl_rev_growth_yoy = model['QuarterlyRevenueGrowthYOY']
        self.target_price = model['AnalystTargetPrice']
        self.trail_pe = model['TrailingPE']
        self.forward_pe = model['ForwardPE']
        self.price_sales_ttm = model['PriceToSalesRatioTTM']
        self.price_book = model['PriceToBookRatio']
        self.ev_revenue = model['EVToRevenue']
        self.ev_ebitda = model['EVToEBITDA']
        self.beta = model['Beta']
        self._52wk_hi = model['52WeekHigh']
        self._52wk_low = model['52WeekLow']
        self._50d_moving_avg = model['50DayMovingAverage']
        self._200d_moving_avg = model['200DayMovingAverage']
        self.shares_out = model['SharesOutstanding']
        self.div_date =  model['DividendDate']
        self.ex_div_date = model['ExDividendDate']
