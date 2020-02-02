
import pandas as pd

#df=pd.read_csv('weather_by_cities.csv')
df=pd.read_csv('1.csv')
g=df.groupby('Hostel')#this creates 3 different data frames grouped by their 3 city names

#to get the grouped data
#for city,city_df in g:
#    print(city)
#    print(city_df)

#to get a single group
print(g.get_group('Aquamarine A Third'))  

#to do operations in group format:
#print(g.max())#to get the maximum value for each city
#print(g.mean())#to get mean value for each data set
#print(g.describe())

