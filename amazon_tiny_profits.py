import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import datetime as dt 

filename = '/Users/jiali/Documents/Python_CodingDojo/Amazon-tiny-profits/MM25.xlsx'
df = pd.read_excel(filename)

#convert object to int
#reference:https://stackoverflow.com/questions/32464280/converting-currency-with-to-numbers-in-python-pandas
df['Revenue (US $M)'] = df['Revenue (US $M)'].replace({'\\$':'', ',':''}, regex=True).astype(int)
df['Net Income (US $M)'] = df['Net Income (US $M)'].replace({'\\$':'', ',':''}, regex=True).astype(int)

#reference:https://matplotlib.org/stable/tutorials/intermediate/gridspec.html
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10,8), gridspec_kw={'height_ratios': [3,1]})
fig.suptitle('2020/W25: Amazon’s tiny profits')

#subplot1
axes[0].plot(df['Quarter'], df['Revenue (US $M)'], marker='.', markersize=6, linewidth=1.5, label='Revenue (US $M)')
axes[0].plot(df['Quarter'], df['Net Income (US $M)'], marker='.', markersize=6, linewidth=1.5, label='Net Income (US $M)')
axes[0].set_xlim(left=dt.date(2005,3,31), right=dt.datetime(2020,3,31))
axes[0].set_ylim(bottom=-500, top=90000)
axes[0].grid()
axes[0].legend()
#subplot2
axes[1].plot(df['Quarter'], df['Net Income (US $M)'], marker='.', markersize=6, linewidth=1.5, c='C1', label='Net Income (US $M)')
axes[1].set_xlim(left=dt.date(2005,3,31), right=dt.datetime(2020,3,31))
axes[1].set_ylim(bottom=-1000)
axes[1].grid()
axes[1].legend()

plt.show()


# #matlab-style
# plt.figure(figsize=(10,8))
# plt.suptitle('2020/W25: Amazon’s tiny profits')

# #subplot1
# plt.subplot(2,1,1)
# plt.plot(df['Quarter'], df['Revenue (US $M)'], marker='.', markersize=6, linewidth=1.5, label='Revenue (US $M)')
# plt.plot(df['Quarter'], df['Net Income (US $M)'], marker='.', markersize=6, linewidth=1.5, label='Net Income (US $M)')
# plt.xlim(left=dt.date(2005,3,31), right=dt.datetime(2020,3,31))
# plt.ylim(bottom=-500, top=90000)
# plt.grid()
# plt.legend()

# #subplot2
# plt.subplot(2,1,2)
# plt.plot(df['Quarter'], df['Net Income (US $M)'], marker='.', markersize=6, linewidth=1.5, c='C1', label='Net Income (US $M)')
# plt.xlim(left=dt.date(2005,3,31), right=dt.datetime(2020,3,31))
# plt.ylim(bottom=-1000)
# plt.grid()
# plt.legend()

# plt.show()