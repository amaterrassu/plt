import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import stat
from PIL import Image
from matplotlib.ticker import FormatStrFormatter

df = pd.read_csv('/Users/georgezagorsky/Desktop/Deworking/data.csv')

# children hist
# total_income hist
# total_income hist 2d, 3d

fig = plt.figure(figsize=(7, 7))

ax = fig.add_subplot(1, 4, 1)
plt.hist(df['children'], density=True, color='red', edgecolor='skyblue', orientation='vertical', lw=1,
         label='histogram', bins=20)
plt.title('histogram children')
plt.xlabel('Values of children')
plt.ylabel('Counter of children')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.minorticks_on()
plt.grid(which='minor', color='#444', ls='--')
plt.grid(which='major', color='#aaa', ls='-.')
plt.legend()
ax.xaxis.set_major_formatter(FormatStrFormatter('x = %2.f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('y = %2.f'))

ax2 = fig.add_subplot(1, 4, 2)
plt.hist(df['total_income'], orientation='horizontal', density=True, edgecolor='skyblue', color='red',
         label='histogram', bins=20, range=(min(df['total_income']), max(df['total_income'])))
plt.title('histogram total income')
plt.xlabel('values of total_income')
plt.ylabel('counter of total_income')
plt.xticks(rotation=90)
plt.yticks(rotation=90)
plt.legend()
plt.minorticks_on()
plt.grid(which='minor', color='#444', ls='--')
plt.grid(which='major', color='#aaa', ls='-.')
ax2.yaxis.set_major_formatter(FormatStrFormatter('y = %.2f'))
ax2.xaxis.set_major_formatter(FormatStrFormatter('x = %.2f'))

ax3 = fig.add_subplot(1, 4, 3)
plt.scatter(df['children'], df['total_income'], s=50, c='green', edgecolors='black', linewidths=1, alpha=0.5,
            label='scatter', marker='s')
plt.title('scatter children_total_income')
plt.xlabel('children')
plt.ylabel('total_income')
plt.xticks(rotation = 90)
plt.yticks(rotation = 90)
plt.legend()
plt.minorticks_on()
plt.grid(which = 'major', color = '#444', ls = '-.')
plt.grid(which='minor', color = '#aaa', ls = '--')
ax3.yaxis.set_major_formatter(FormatStrFormatter('y = %.2f'))
ax3.xaxis.set_major_formatter(FormatStrFormatter('x = %.2f'))


ax4 = fig.add_subplot(1, 4, 4, projection = '3d')
plt.scatter(df['children'], df['total_income'], s=50, c='green', edgecolors='black', linewidths=1, alpha=0.5,
            label='scatter', marker='s')
plt.title('scatter children_total_income')
plt.xlabel('children')
plt.ylabel('total_income')
plt.xticks(rotation = 90)
plt.yticks(rotation = 90)
plt.legend()
plt.minorticks_on()
ax4.set_zlabel('High')
plt.grid(which = 'major', color = '#444', ls = '-.')
plt.grid(which='minor', color = '#aaa', ls = '--')
ax3.yaxis.set_major_formatter(FormatStrFormatter('y = %.2f'))
ax3.xaxis.set_major_formatter(FormatStrFormatter('x = %.2f'))

plt.show()