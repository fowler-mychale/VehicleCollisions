import pandas as pd
import numpy as np
import time
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/Mike_F/Desktop/2020-05-20.csv')



fig, ax = plt.subplots(ncols=3,figsize=(15,4))
sns.barplot(x='City',y='Difference', data=df,ax=ax[0],hue='Astronomical_Twilight').set_title("Time_Diff (Astronomical_Twilight) ")
sns.barplot(x='City',y='Difference', data=df, ax=ax[1],hue='Civil_Twilight').set_title("Time_Diff (Civil_Twilight)")
sns.barplot(x='City',y='Difference', data=df,ax=ax[2],hue='Nautical_Twilight').set_title("Time_Diff (Nautical_Twilight)")


fig2, axs = plt.subplots(ncols=3,figsize=(15,4))
sns.lineplot(x='Difference', y='Temperature(F)', data=df, ax=axs[0],hue='City',ci=None).set_title("Time_Diff (Temperature(F))")
sns.lineplot(x='Difference', y='Humidity(%)', data=df, ax=axs[1],hue='City',ci=None).set_title("Time_Diff (Humidity(%))")
sns.lineplot(x='Difference', y='Pressure(in)', data=df, ax=axs[2],hue='City',ci=None).set_title("Time_DIff (Pressure(in))")


fig.savefig('Time_Difference')
plt.close(fig)


fig2.savefig('Time_Difference (by climate)')
plt.close(fig2)
plt.show()