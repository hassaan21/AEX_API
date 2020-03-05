#Hassaan Haq
#ID: 49262514

import json
import urllib.parse
import urllib.request

BASE_IEX_STOCK_URL = 'https://api.iextrading.com/1.0'

def create_url(stock_name: str) -> str:
    '''takes in base url and adds symbol
        to complete the build of the url'''

    complete_url = BASE_IEX_STOCK_URL + '/stock/{symbol}/chart/'.format(symbol = stock_name)
    return complete_url

def retrieve_api_data(url: str, number_of_days: int) -> dict:
    '''contacts the url and retrieves api info'''

    range_options = ['1m', '3m', '6m', '1y', '2y', '5y']
    
    if number_of_days == 1:
        option = '1d'
        current_url = url + '1d'
        response = urllib.request.urlopen(current_url)
        json_text = response.read().decode(encoding = 'utf-8')
        result = json.loads(json_text)
    else:
        for option in range_options:
            
            current_url = ''
            current_url = url + option
        
            response = urllib.request.urlopen(current_url)
            json_text = response.read().decode(encoding = 'utf-8')
            result = json.loads(json_text)
            if len(result) >= number_of_days:
                break

    return result[len(result) - number_of_days:]


def get_company_info(symbol) -> str:
    '''takes in base url and adds
        company to get company info'''

    company_info_url = BASE_IEX_STOCK_URL + '/stock/{symbol}/company/'.format(symbol=symbol)
    response = urllib.request.urlopen(company_info_url)
    json_text = response.read().decode(encoding = 'utf-8')
    result = json.loads(json_text)

    return result

def get_shares_outstanding(symbol) -> int:
    '''gets shares outstanding'''
    url = BASE_IEX_STOCK_URL + '/stock/{symbol}/stats'.format(symbol=symbol)
    response = urllib.request.urlopen(url)
    json_text = response.read().decode(encoding = 'utf-8')
    result = json.loads(json_text)
    print(result['sharesOutstanding'])



