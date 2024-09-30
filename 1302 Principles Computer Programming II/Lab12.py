# Small lab using the pandas library for data storage and manipulation

import pandas as pd

revenue = pd.Series([1000, 900, 1100, 400, 2000], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print(revenue)

expenses = pd.Series([900, 900, 900, 900, 900], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print(expenses)

print(revenue['Wed'])
print(expenses['Tue':'Thu'])

net_profit = revenue - expenses
print(net_profit)
print((net_profit['Mon'] + net_profit['Tue'] + net_profit['Wed'] + net_profit['Thu'] + net_profit['Fri']) / 5)
