import pandas as pd
import numpy as np

df=pd.read_csv('weather.csv')


#5 methods


#1.fillna method:

new=df.fillna(0)
#print(new)

#if you want it column wise:
new=df.fillna({
    'temperature':0,
    'windspeed':0,
    'event':'no event'
    })
#print(new)

new=df.fillna(method='ffill')#ffill=forward fill
#this fills the gaps with data poin forward
#print(new)
#we can also use backward fill: 'bfill'

new=df.fillna(method='bfill',axis='columns')#fills with the nearby columns
#print(new)

new=df.fillna(method='bfill',limit=1)#fills the forward value only to the lmitted blank space
#print(new)





#2.guessing the Nan values:

new=df.interpolate()#guesses using linear intrpolation
#print(new)

#if you want more accuracy with the data which is interpolated then we can fix methods='time'
#for this to be done the day has to be a time stamp data type
df=pd.read_csv('weather.csv',parse_dates=["day"])
#for this to be done the column on which the method is applied is made as the index
df.set_index('day',inplace=True)

new=df.interpolate(method="time")#interpolates by analyzing the dates
#print(new)





#3.dropna method:


new=df.dropna()#the rows with Nan values are dropped
#print(new)


#to selectively drop rows
new=df.dropna(how="all")#the rows with all the columns having Nan values are dropped
#print(new)


#to display if we have atleast 1,2,...or n Nan values and drop the rest
new=df.dropna(thresh=1)#to display if we have atleast 1 Nan values and drop the rest
#print(new)





#4.inserting missing dates:



date=pd.date_range("01-01-2017","01-11-2017")
idx=pd.DatetimeIndex(date)
df=df.reindex(idx)
#print(df)



#5.replace function:
#done when there are no blank spaces but sometimes the blank data is automatically filled by websites as
#-99999 or anything else , these are called spacial values
#so to handle such data we use replace function



df=pd.read_csv('weather_replace func-1.csv')
#print(df)

new=df.replace(-99999,np.NaN)#replaces -99999 with NaN
#print(new)


#if in case there are 2 spacial values -99999,0 then:
new=df.replace((-99999,'0'),np.NaN)#here '0' as 0 is a string in that csv file
#print(new)


#to specifically replace:
new=df.replace({
    'temperature':-99999,
    'windspeed':-99999,
    'event':'0'},np.NaN)
#print(new)

#to replace specifically with some other data other than NaN:
new=df.replace({-99999:np.NaN,'0':'sunny'})
#print(new)


#if incase the data is given with units:
#to remove the units
df=pd.read_csv('weather_replace func-2.csv')
#we use Regex: used to recogonize patterns
new=df.replace('[A-Za-z]','',regex=True)#replaces the data with alphabets in it with a blank spaces
#print(new)

#but by doing the above the event column is also removed
#so now use dictionary and remove specifically
new=df.replace({
    'temperature':'[A-Za-z]',
    'windspeed':'[A-Za-z]'
    },'',regex=True)
#print(new)



#to replace a list of values with another list of values:
#first lets create a data frame
df=pd.DataFrame({
    'score':['exceptional','average','good'],
    'student':['rob','maya','tom']
    })
#print(df)


#if we wish to have numbers in score columns instead of comments in strings
#we have to internally map these comments to numbers
new=df.replace(['average','good','exceptional'],[2,3,4])
#print(new)















