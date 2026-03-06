from bot.client import BinanceFutureClient
import logging

def execute_order(symbol:str,side:str,order_type:str,quantity:float,price:float=None):
    client = BinanceFutureClient()
    try:
        logging.info(f'Order Initiated for {symbol}')
        response = client.place_order(symbol,side,order_type,quantity,price)
        return response
    except Exception as e:
        raise e
