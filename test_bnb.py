from binance_chain.client import Client, KlineInterval
client = Client()

# time = client.get_time()
# print(time)

# # get account
# account = client.get_account('tbnb1a75pnew52vw7242k4w2fd6pp67e30h4392yk5k')
# print(account['address'], account['account_number'], account['public_key'])
# for b in range(len(account['balances'])):
# 	print(account['balances'][b])

# # get markets
# markets = client.get_markets()
# print(len(markets))
# for m in range(len(markets)):
# 	print(markets[m])

# fees = client.get_fees()
# print(len(markets))

# trades = client.get_trades()
# for t in range(len(trades['trade'])):
# 	print(trades['trade'][t])


transactions = client.get_transactions(address='tbnb193t8pkhm2sxw5uy5ypesygda8rzsk25ge3e9y7')
#print(transactions)
for t in range(len(transactions['tx'])):
	print(transactions['tx'][t])