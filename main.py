import ccxt
import time

exchange = ccxt.mexc({
    'apiKey': 'mx0vglpNoJnXhChZdP',
    'secret': '1a9845f7b79341cda73c9496c4b653f9',
})

symbol = 'BTC/USDT'
amount = 0.001
take_profit = 1.7
stop_loss = 0.9

def get_price():
    return exchange.fetch_ticker(symbol)['last']

def trade():
    entry = get_price()
    print(f"Entrata a: {entry}")
    exchange.create_market_buy_order(symbol, amount)
    print("Acquisto fatto!")

    while True:
        price = get_price()
        if price >= entry * take_profit:
            print("Take profit raggiunto!")
            exchange.create_market_sell_order(symbol, amount)
            break
        elif price <= entry * stop_loss:
            print("Stop loss attivato.")
            exchange.create_market_sell_order(symbol, amount)
            break
        time.sleep(5)

while True:
    trade()
    time.sleep(60)
