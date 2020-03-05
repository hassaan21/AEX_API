#Hassaan Haq
#ID: 49262514
import API
import Indicators


class true_range:

    '''using first two letters of input,
        figures out which signal strategy to use'''

    def __init__(self, upper_threshold: str, lower_threshold: str) -> None:

        self.upper_threshold = float(upper_threshold[1:])
        self.lower_threshold = float(lower_threshold[1:])

    def buy_or_sell_option(self, value: float, api_element: dict) -> str:
        '''tells the user which stocks to buy/sell'''
        if value == '':
            return ''
        elif float(value) < self.upper_threshold:
            return "BUY"
        elif float(value) > self.lower_threshold:
            return "SELL"
        else:
            return ''

class moving_average:
    '''gets signal to buy/sell for moving
        average indicator using closing prices'''
    def __init__(self):
        self._last_signal = 'no value'

    def buy_or_sell_option(self, value: float, api_element: dict) -> str:
        '''tells the user which stocks to buy/sell'''
        if value == '':
            empty = ''
            return empty
        elif float(api_element['close']) < float(value):
            if self._last_signal == 'BUY' or self._last_signal == 'NONE':
                self._last_signal = 'SELL'
                return 'SELL'
            else:
                self._last_signal = 'SELL'
                return '' 
        elif float(api_element['close']) == float(value):
            self._last_signal = 'NONE'
            empty = ''
            return empty
        elif float(value['close']) > float(value):
            if self._last_signal == 'SELL' or self._last_signal == 'NONE':
                self._last_signal = 'BUY'
                return 'BUY'
            else:
                self._last_signal = 'BUY'
                empty = ''
                return empty
        else:
            empty = ''
            return empty

class moving_average_volume:
    '''gets signal to buy/sell for moving
        average indicator using volume'''
    def __init__(self):
        self._last_signal = 'no value'

    def buy_or_sell_option(self, value: float, api_element: dict) -> str:
        '''tells the user which stocks to buy/sell'''
        if value == '':
            empty = ''
            return empty
        elif float(api_element['volume']) < float(value):
            if self._last_signal == 'BUY' or self._last_signal == 'NONE':
                self._last_signal = 'SELL'
                return 'SELL'
            else:
                self._last_signal = 'SELL'
                return '' 
        elif float(api_element['close']) == float(value):
            self._last_signal = 'NONE'
            empty = ''
            return empty
        elif float(value['close']) > float(value):
            if self._last_signal == 'SELL' or self._last_signal == 'NONE':
                self._last_signal = 'BUY'
                return 'BUY'
            else:
                self._last_signal = 'BUY'
                empty = ''
                return empty
        else:
            empty = ''
            return empty


class directonal_closing_signal:
    """"decides whether to buy or sell a given
        stock depending upon the closing price"""

    def __init__(self, buy_threshold: str, sell_threshold: str) -> None:
        self.buy_threshold = float(buy_threshold)
        self.sell_threshold = float(sell_threshold)

    def buy_or_sell_option(self, indicator_value: float, api_option: dict):
        if indicator_value == '':
            return ''
        elif indicator_value > self.buy_threshold:
            return 'BUY'
        elif indicator_value < self.sell_threshold:
            return 'SELL'
        else:
            return ''



class directonal_vol_signal:
    """"decides whether to buy or sell a given
        stock depending upon the volume"""

    def __init__(self, buy_threshold: str, sell_threshold: str) -> None:
        self.buy_threshold = float(buy_threshold)
        self.sell_threshold = float(sell_threshold)

    def buy_or_sell_option(self, indicator_value: float, api_option: dict):
        if indicator_value == '':
            return ''
        elif indicator_value > self.buy_threshold:
            return 'BUY'
        elif indicator_value < self.sell_threshold:
            return 'SELL'
        else:
            return ''   



    
        
       
        
    
        



        

    

        

