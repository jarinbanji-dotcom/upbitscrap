import threading
import time
from pybit.unified_trading import HTTP



session = HTTP(
    testnet=False,
    api_key="nrk5LoL4OsGXVetTgZ",
    api_secret="F9YtDDwUeAAgTzhAKwAl3h1u7XoqAKAMx6bP"
)
def place_aggressive_spot_buy(symbol):
    st = time.time()

    # Results container
    results = {}

    # ── Fetch both in parallel using threads ──
    def fetch_ticker():
        results['ticker'] = session.get_tickers(category="spot", symbol=symbol)

    def fetch_instr():
        results['instr'] = session.get_instruments_info(category="spot", symbol=symbol)

    #t1 = threading.Thread(target=fetch_ticker)
    #t2 = threading.Thread(target=fetch_instr)

    #t1.start()
    #t2.start()
    #t1.join()
    #t2.join()

    fetch_instr()
    fetch_ticker()

    print(f"Both fetched in: {time.time()-st:.3f}s")  # ~100-150ms instead of ~300-400ms

    # ── Extract data ──
    mark_price = float(results['ticker']['result']['list'][0]['usdIndexPrice'])
    rules = results['instr']['result']['list'][0]

    ratio_x = min(float(rules['riskParameters']['priceLimitRatioX']), 0.05)
    safe_ratio = ratio_x * 0.80
    ...

symbol=["SKRUSDT","SENTUSDT","USDCUSDT","BTCUSDT","ETHUSDT"]
for i in symbol:
    place_aggressive_spot_buy(i)
for i in symbol:
    place_aggressive_spot_buy(i)

