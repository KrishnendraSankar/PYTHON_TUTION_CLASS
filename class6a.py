#Dictionary Comprehension

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

new_stocks = {}
for k,v in stocks.items():
    new_stocks[k] = v*2

updated_stocks = {k: v*2 for (k,v) in stocks.items()}
print(updated_stocks)
print(new_stocks)

