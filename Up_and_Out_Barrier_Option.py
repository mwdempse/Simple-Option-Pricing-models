class UpandOutBarrierOption:
    
    def __init__(self,strike,barrier_level):
        self.strike = strike
        self.barrier_level = barrier_level
        self.barrier_trigger = False
        
    def check_barrier(self, stock_price):
        if stock_price > self.barrier_level:
            self.barrier_trigger = True
    
    def get_payoff(self, stock_price):
        if not self.barrier_trigger:
            if stock_price> self.strike:
                return stock_price - self.strike
            else:
                return 0
        else:
            return 0