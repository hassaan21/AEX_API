#Hassaan Haq
#ID: 49262514

import API
import signal_strategies


class true_range:
    '''uses true range
    indicator to get buy/sell signal'''

    def __init__(self) -> None:
        self.indisignal = 0
                
       

    def calculations(self, api_element: dict) -> float:
        upper = api_element['high']
        lower = api_element['low']

        true_range = 0

        if self.indisignal > 0:

            if upper > self.indisignal > lower:
                true_range = (upper - lower)/(self.indisignal)        

            elif self.indisignal > upper:
                true_range = (self.indisignal - lower)/(self.indisignal)


            elif self.indisignal < lower:
                true_range = (upper - self.indisignal)/(self.indisignal)
            

        self.indisignal = api_element['close']

        if true_range == 0:
            return ''
        
        return '{0:.4f}'.format(true_range*100)


class moving_average:
    '''calculates moving average'''

    def __init__(self, value: int) -> None:

        self._value_number = value

        self._infoList = []

    def calculate(self, api_element: dict) -> float:
        self._infoList.append(api_element['close'])

        if len(self._value_number + 1 == self._infoList):
            self._infoList.pop(0)

        if self._value_number == len(self._infoList):

            result = 0


        for element in self_infoList:
            result += element

            return '{0:.4f}'.format(result/self._value_number)
        else:
            empty = ''
            return empty

class moving_average_volume:
    '''EXACT same as moving average class
        except this calculates moving average of
        volume instead of closing prices'''
    def __init__(self, value: int) -> None:

        self._value_number = value

        self._infoList = []

    def calculate(self, api_element: dict) -> float:
        self._infoList.append(api_element['volume'])

        if len(self._value_number + 1 == self._infoList):
            self._infoList.pop(0)

        if self._value_number == len(self._infoList):

            result = 0


        for element in self_infoList:
            result += element

            return '{0:.4f}'.format(result / self._value_number)
        else:
            empty = ''
            return empty

    

class directonal_closing_indicator:
    """"calculates n-day directional indicator
        for a given stock using closing price"""

    def __init__(self, days):
        self.values = []
        self.days = days

    def calculations(self, api_element: dict):
        self.values.append(api_element['close'])
        count = 0
        for i in range(len(self.values)-1):
            if self.values[i] < self.values[i+1]:
                count += 1
            elif self.values[i] > self.values[i+1]:
                count -= 1
        if len(self.values) == self.days + 1:
            self.values.pop(0)

        return count


class directonal_vol_indicator:
    """calcualtes n-day directonal indicator
       for a given stock using volume"""

    def __init__(self, days):
        self.values = []
        self.days = days

    def calculations(self, api_element: dict):
        self.values.append(api_element['volume'])
        count = 0
        for i in range(len(self.values)-1):
            if self.values[i] < self.values[i+1]:
                count += 1
            elif self.values[i] > self.values[i+1]:
                count -= 1
        if len(self.values) == self.days + 1:
            self.values.pop(0)

        return count
        
        
        
