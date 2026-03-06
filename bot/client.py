import os
import time
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv

load_dotenv()

class BinanceFutureClient:
    def __init__(self):
        api=os.getenv('API')
        sec=os.getenv('SEC')

        self.client = Client(api,sec,testnet=True)
        self.client.FUTURES_URL='https://testnet.binancefuture.com/fapi'
        self.client.timestamp_offset = self.client.get_server_time()['serverTime'] - int(time.time()*1000)

    def place_order(self,symbol,side,order_type,quantity,price=None):
        try:
            param = {
                'symbol':symbol.upper(),
                'side':side.upper(),
                'type':order_type.upper(),
                'quantity':quantity
            }

            if order_type.upper() =='LIMIT':
                param['price']=str(price)
                param['timeInForce'] = 'GTC'
            logging.info(f'Sending Request: {param}')
            response = self.client.futures_create_order(**param)
            logging.info(f'Response Received: {response}')
            return response
        except BinanceAPIException as e:
            logging.error(f'API Error: {e.message}')
            raise e
        except Exception as e:
            logging.error(f'Unexpected Error: {e}')
            raise e
        