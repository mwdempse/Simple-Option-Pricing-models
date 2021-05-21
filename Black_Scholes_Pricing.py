import math
from scipy.stats import norm

class EuropeanCall:
    def call_price(self, asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate):
        b = math.exp(-risk_free_rate*time_to_expiration)
        x1 = (math.log(asset_price/(b*strike_price)) + 0.5*(asset_volatility**2)*time_to_expiration)/(asset_volatility*(time_to_expiration*time_to_expiration**0.5))
        z1 = norm.cdf(x1)*asset_price
        x2 = (math.log(asset_price/(b*strike_price)) - 0.5*(asset_volatility**2)*time_to_expiration)/(asset_volatility*(time_to_expiration*time_to_expiration**0.5))
        z2 = norm.cdf(x2)*asset_price
        return z1-z2
    
    def __init__(self, asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate):
        self.asset_price = asset_price
        self.asset_volatility = asset_volatility
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.price = self.call_price(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)
        
class EuropeanPut:
    def call_price(self, asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate):
        b = math.exp(-risk_free_rate*time_to_expiration)
        x1 = (math.log(b*strike_price)/asset_price + 0.5*(asset_volatility**2)*time_to_expiration)/(asset_volatility*(time_to_expiration*time_to_expiration**0.5))
        z1 = norm.cdf(x1)*asset_price
        x2 = (math.log(b*strike_price)/asset_price - 0.5*(asset_volatility**2)*time_to_expiration)/(asset_volatility*(time_to_expiration*time_to_expiration**0.5))
        z2 = norm.cdf(x2)*asset_price
        return z1-z2
    
    def __init__(self, asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate):
        self.asset_price = asset_price
        self.asset_volatility = asset_volatility
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.price = self.call_price(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)
        
    
class European_Call_Payoff:

    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self, stock_price):
        if stock_price > self.strike:
            return stock_price - self.strike
        else:
            return 0

class European_Put_Payoff:

    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self, stock_price):
        if stock_price < self.strike:
            return stock_price - self.strike
        else:
            return 0