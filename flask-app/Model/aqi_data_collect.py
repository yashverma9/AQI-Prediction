import pandas as pd
import numpy as np



df = pd.read_csv("data/blr_pm25.csv", usecols = ['date', 'pm25'])



cnt = 0
for i in range(df.shape[0]):
    if df["pm25"][i] == " ":
        cnt += 1        


#Data cleaning
def remove_space(x):
    if x == " ":
        x = np.NaN
    else:
        x =  x.strip()
    return x
df['pm25'] = df['pm25'].apply(remove_space)
df['pm25'] = df['pm25'].astype(float)


#Getting dates in datetime format
df['date'] = df['date'].astype('datetime64[ns]')


sorted_df = df.sort_values(by = "date")
sorted_df.reset_index(drop = True, inplace = True)



#Stores all dates whose data is not there
non_date = list(pd.date_range(start = '2013-12-31', end = '2021-05-15' ).difference(sorted_df["date"]))
for i in range(len(non_date)):
    non_date[i] = (non_date[i].to_pydatetime().date())


for i in non_date:
    if(i):
        sorted_df.loc[len(sorted_df)] = [i, np.NaN]



sorted_df['date'] = pd.to_datetime(sorted_df['date']).dt.date


sorted_df = sorted_df.sort_values(by = "date")
sorted_df.reset_index(drop = True, inplace = True)


#Renaming column to PM2.5
sorted_df.rename(columns = {'pm25':'PM2.5'}, inplace = True)


year_range = [2015, 2016, 2017, 2018, 2019, 2020]
for year in year_range:
    startdate = pd.to_datetime(str(year)+"-1-1").date()
    enddate = pd.to_datetime(str(year+1)+"-1-1").date()
    sorted_df[(sorted_df["date"]<enddate) & (sorted_df["date"] >= startdate)].to_csv("data/AQI/aqi"+str(year)+".csv", index = False)
    with open("data/AQI/aqi"+str(year)+".csv", 'r+') as f:
        f.seek(0,2)                    
        size=f.tell()               
        f.truncate(size-1)