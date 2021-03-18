## 2. The Familiarity Principle ##

from numpy import arange

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')
fig, ax = plt.subplots()
ax.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'])
# plt.ylabel('Countries')
# plt.xlabel('Total Deaths')
# plt.title('Top 20 Countries Total Death Toll')
plt.show()

## 4. The OO Interface ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')
fig, ax = plt.subplots()
ax.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'])
plt.show()

## 5. Mobile-Friendly Proportions ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')
fig, ax = plt.subplots(figsize=(4.5,6))
ax.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'])
plt.show()

## 7. Erasing Non-Data Ink ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
         top20_deathtoll['Total_Deaths'])
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(top=False, bottom=False, left=False, right=False)
plt.show()

## 8. Erasing Redundant Data-Ink ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

# Initial Code

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
       top20_deathtoll['Total_Deaths'], height=0.45)

for location in ['left', 'right', 'top', 'bottom']:
   ax.spines[location].set_visible(False)
ax.tick_params(bottom=False, left=False)
ax.set_xticks([0, 150000, 300000])
plt.show()

## 9. The Direction of Reading ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

# Initial Code

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#b00b1e')

for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)
ax.tick_params(bottom=False, left=False, top=False, right=False)
ax.set_xticks([0, 150000, 300000])
ax.xaxis.tick_top()
ax.tick_params(axis='x', colors='grey')
plt.show()

## 10. Title and Subtitle ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#b00b1e')
for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)
ax.set_xticks([0, 150000, 300000])
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')
ax.text(x=-80000, y=23.5, s='The Death Toll Worldwide Is 1.5M+', size=17, weight='bold')
ax.text(x=-80000, y=22.5, s='Top 20 countries by death toll (December 2020)', size=12)
plt.show()

## 11. Final Touches ##

import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#b00b1e')
for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)
ax.set_xticklabels(['0', '150,000', '300,000'])
ax.set_xticks([0, 150000, 300000])
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')
ax.text(x=-80000, y=23.5,
        s='The Death Toll Worldwide Is 1.5M+',
        weight='bold', size=17)
ax.text(x=-80000, y=22.5,
        s='Top 20 countries by death toll (December 2020)',
        size=12)
ax.set_yticklabels([])
for num, country in zip(range(0,21), top20_deathtoll['Country_Other']):
    ax.text(x=-80000, y=num-0.15, s=country)

ax.axvline(x=150000, ymin=0.045, c='grey', alpha=0.5)

plt.show()
    