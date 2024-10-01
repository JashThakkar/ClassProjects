# Takes a CSV file and makes it into a matplot graph

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('atlanta_weather.csv')
df = pd.DataFrame(data)

months = df.Month
high = df.High
low = df.Low

plt.figure()
plt.title('Atlanta – Monthly Temperature', fontsize=20)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Temperature (Fahrenheit)', fontsize=16)

plt.plot(months, high, 'b--o', label='High')
plt.plot(months, low, 'g:^', label='Low')
plt.legend(fontsize=20)
plt.annotate('Highest of the year', arrowprops=dict(facecolor='red'), xy=(6, 89), xytext=(5, 76))

plt.show()
