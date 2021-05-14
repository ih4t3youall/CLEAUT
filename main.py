import requests;

r_eth_price = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
r_sxp_price = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=SXPUSDT')

print(r_eth_price);
print(r_sxp_price);
