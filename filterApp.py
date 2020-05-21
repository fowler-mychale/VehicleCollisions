import pandas as pd
import numpy as np
import time
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/Mike_F/Desktop/US_Accidents_Dec19.csv')

df.drop(['TMC','Description','Country','Timezone','Airport_Code','Number','Weather_Timestamp','Traffic_Calming','Traffic_Signal','Turning_Loop','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','ID','Wind_Speed(mph)','Precipitation(in)','Visibility(mi)','Wind_Chill(F)','End_Lat','End_Lng'], axis = 1, inplace = True)

df[['Start_Date', 'Start(time)']] = df['Start_Time'].str.split(' ', n=1, expand=True)

df['Start_Date'] =  pd.to_datetime(df['Start_Time'])

df[['End_Date', 'End(time)']] = df['End_Time'].str.split(' ', n=1, expand=True)

df['End_Date'] = pd.to_datetime(df['End_Time'])

#the difference in response time
df['Difference'] = (df['End_Date'] - df['Start_Date']).astype(str).str[-15:-13]

#Convert columns to datetime
df['Start_year'] = df['Start_Date'].dt.year
df['Start_month'] = df['Start_Date'].dt.month
df['Start_day'] = df['Start_Date'].dt.day

#drop tables < 2017
#df.drop(df[df['Start_year'] < 2017].index, inplace = True)

#Segment data by City
df.drop(df[(df['City'] != 'Los Angeles') & (df['City'] != 'Boston') & (df['City'] != 'New York') & (df['City'] != 'Chicago')].index, inplace = True)

#drop more unused columns
df.drop(['Start_Time','End_Time','Start_Date','End_Date'], axis=1,inplace=True)

# City Graph 
fig1, ax = plt.subplots(ncols=3,figsize=(15,4))
sns.barplot(x='City',y='Severity', data=df,ax=ax[0],hue='Astronomical_Twilight').set_title("Graph (Astronomical_Twilight) ")
sns.barplot(x='City',y='Severity', data=df, ax=ax[1],hue='Civil_Twilight').set_title("Graph (Civil_Twilight)")
sns.barplot(x='City',y='Severity', data=df,ax=ax[2],hue='Nautical_Twilight').set_title("Graph (Nautical_Twilight)")

#Weather graph
fig2, axs = plt.subplots(ncols=3,figsize=(15,4))
sns.lineplot(x='Start_month', y='Temperature(F)', data=df, ax=axs[0],hue='City',ci=None).set_title("Graph (Temperature(F))")
sns.lineplot(x='Start_month', y='Humidity(%)', data=df, ax=axs[1],hue='City',ci=None).set_title("Graph (Humidity(%))")
sns.lineplot(x='Start_month', y='Pressure(in)', data=df, ax=axs[2],hue='City',ci=None).set_title("Graph (Pressure(in))")

fig1.savefig('City_info', dpi=200)
plt.close(fig1)

fig2.savefig('weather_info', dpi=200)
plt.close(fig2)

plt.show()
pd.DataFrame.to_csv(df,"" + time.strftime('%Y-%m-%d') + ".csv",',')

#https://www.kaggle.com/sobhanmoosavi/us-accidents