import typer

def validate_order_input(symbol: str ,side: str ,order_type:str,quantity: float,price: float):
    if not symbol or len(symbol)<5:
        raise ValueError("Invalid symbol!")
    if side.upper() not in ['BUY','SELL']:
        raise ValueError('Invalid side!')
    if order_type.upper() not in ['MARKET','LIMIT']:
        raise ValueError('Invalid Type')
    if quantity<=0:
        raise ValueError('Quantity must be grater than 0.')
    if order_type.upper()=='LIMIT' and (price is None or price<=0):
        raise ValueError('Price is required and must be greater than 0 for LIMIT orders')
    return True