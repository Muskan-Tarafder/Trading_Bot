import typer
from bot.client import BinanceFutureClient
from bot.logging_config import setup_log
from bot.validators import validate_order_input
from bot.orders import execute_order
app=typer.Typer()
setup_log()

@app.command()
def trade(symbol: str = typer.Option(...,"--symbol",help="Trading pair, e.g., BTCUSDT"),
          side: str =typer.Option(...,"--side",help="BUY or SELL"),
          order_type:str = typer.Option("MARKET","--order-type",help="MARKET or LIMIT"),
          quantity: float = typer.Option(...,"--quantity",help = "Amount to trade"), 
          price: float = typer.Option(None,"--price",help="Required for LIMIT orders")):
    
    try:
        validate_order_input(symbol,side,order_type,quantity,price)
        res = execute_order(symbol,side,order_type,quantity,price)
        typer.secho('Success!!')
        typer.echo(f"Order id: {res.get('orderId')}")
        typer.echo(f"Status: {res.get('status')}")
        typer.echo(f"Price: {res.get('avgPrice',price)}")
    except Exception as e:
        typer.secho(f'Order Failed: {e}')

if __name__=='__main__':
    print('hello')
    app()