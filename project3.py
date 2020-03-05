#Hassaan Haq
#ID: 49262514

import urllib.request 
import json
import API
import signal_strategies
import Indicators

def main() -> None:
    '''calls different functions that run the program'''
    stockName = stock_name()
    daysNum = trade_days()
    combo = combo_input()
    behavior_url = API.create_url(stockName)
    api_json = API.retrieve_api_data(behavior_url, daysNum)
    comp_info = API.get_company_info(stockName)
    print_three_headers(stockName)
    print_table_headers()
    print_data(api_json, combo)


def print_data(api_data, combo):
    x = which_combo(api_data, combo)
    for data in range(len(api_data)):
        print(api_data[data]['date'], '\t', "%.4f" % (api_data[data]['open']), '\t', "%.4f" % (api_data[data]['high']), '\t', "%.4f" % (api_data[data]['low']), '\t', "%.4f" % (api_data[data]['close']), '\t', api_data[data]['volume'], '\t', x[2], '\t', x[0][data], '\t', x[1][data])
    print('Data provided for free by IEX')
    print("View IEX's Terms of Use")
    print('https://iextrading.com/api-exhibit-a/')
    

def print_three_headers(stockName: str) -> str:
    '''prints symbol, company name,
    and shares outstanding'''
    result = API.get_company_info(stockName)
    print(result['symbol'])
    print(result["companyName"])
    API.get_shares_outstanding(stockName)
    


def print_table_headers() -> str:
    '''prints the headers for the table'''
    print('Date\tOpen\tHigh\tLow\tClose\tVolume\tIndicator\tBuy?\tSell?')    


def stock_name() -> str:
    '''prompts user to enter symbol'''
    stock = input()
    return stock 

def trade_days() -> str:
    '''takes in days and converts to one of the time options'''
    
    while True:
        num_days = int(input())
        if num_days not in range(1, 1000):
            continue
        break
    return num_days

def combo_input(): #COME BACK AND FIGURE OUT RETURN VALUE
    
    while True:
        combo = input()
        if combo[0:2] not in ['TR', 'MP', 'MV', 'DP', 'DV']:
            continue
        break
    return combo


def which_combo(api_info: list, indisignal: str) -> None:
    """figures out which signal/indicator function to call depending on input"""
    indisignal = indisignal.split()
    buy = sell = []
    if indisignal[0] == "TR":
        indicator = Indicators.true_range()        
        for item in api_info:
            temp = indicator.calculations(item)
            true_range_signal = signal_strategies.true_range(indisignal[1], indisignal[2])
            buy_or_sell = true_range_signal.buy_or_sell_option(temp, item)
            if buy_or_sell == "":
                buy.append("")
                sell.append("")
            elif buy_or_sell == "BUY":
                buy.append(buy_or_sell)
                sell.append("")
            elif buy_or_sell == "SELL":
                sell.append(buy_or_sell)
                buy.append("")
            
    elif indisignal[0] == "MP":
        indicator = Indicators.moving_average(indisignal[1])
        for item in api_info:
            temp = indicator.calculate(item)
            moving_avg_signal = signal_strategies.moving_average()
            buy_or_sell = moving_avg_signal.buy_or_sell_option(temp, item)
            if buy_or_sell == "":
                buy.append("")
                sell.append("")
            elif buy_or_sell == "BUY":
                buy.append(buy_or_sell)
                sell.append("")
            elif buy_or_sell == "SELL":
                sell.append(buy_or_sell)
                buy.append("")
        
    elif indisignal[0] == "MV":
        indicator = Indicators.moving_average_volume(indisignal[1])
        for item in api_info:
            temp = indicator.calculate(item)
            moving_avg_vol_signal = signal_strategies.moving_average_volume()
            buy_or_sell = moving_avg_vol_signal.buy_or_sell_option(temp, item)
            if buy_or_sell == "":
                buy.append("")
                sell.append("")
            elif buy_or_sell == "BUY":
                buy.append(buy_or_sell)
                sell.append("")
            elif buy_or_sell == "SELL":
                sell.append(buy_or_sell)
                buy.append("")
        
    elif indisignal[0] == "DP":
        indicator = Indicators.directional_closing_indicator(indisignal[1])
        for item in api_info:
            temp = indicator.calculations(item)
            directional_signal = signal_strategies.directional_closing_signal(indisignal[2], indisignal[3])
            buy_or_sell = directional_signal.buy_or_sell_option(temp, item)
            if buy_or_sell == "":
                buy.append("")
                sell.append("")
            elif buy_or_sell == "BUY":
                buy.append(buy_or_sell)
                sell.append("")
            elif buy_or_sell == "SELL":
                sell.append(buy_or_sell)
                buy.append("")
        
    elif indisignal[0] == "DV":
        indicator = Indicators.directional_vol_indicator(indisignal[1])
        for item in api_info:
            temp = indicator.calculations(item)
            directional_vol_signal = signal_strategies.directional_vol_signal(indisignal[2], indisignal[3])
            buy_or_sell = directional_vol_signal.buy_or_sell_option(temp, item)
            if buy_or_sell == "":
                buy.append("")
                sell.append("")
            elif buy_or_sell == "BUY":
                buy.append(buy_or_sell)
                sell.append("")
            elif buy_or_sell == "SELL":
                sell.append(buy_or_sell)
                buy.append("")


    return [buy, sell, indicator]



if __name__ == '__main__':
    main()
    
    
