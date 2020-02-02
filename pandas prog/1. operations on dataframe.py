import pandas as pd



##LIST OF OPERATIONS(only few impotant once are mentioned, rest all google= 'pandas series operations')
##1.creating a dataframe
##2.opening a pre existing csv file
##3.rows and columns
##4.selectively printing rows and columns
##5.data type of columns
##6.MAX and MIN
##7.MEAN
##8.standard deviation
##9.describe: gives all the stats like count,max,min,mean,std....
##10.conditions
###11.to set index(nos: 0,1,2,3..)
##12.to get a particular row on the basis of the new index
##13.filling Nan




#1.create dataframe
wether_data={
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,34,26],
    'windspeed': [3,4,7],
    'event': ['Rain','sunny','snow']
    }
df=pd.DataFrame(wether_data)#convert this to a pandas dataframe
#print(df)

#2.opening a pre existing csv file
df1=pd.read_csv('nyc_weather.csv')

#3.rows and columns
rows,columns=df1.shape
#print(rows,columns)

#4.if we want to print only first n rows do df.head(n)
#print(df1.head(4))

#4.if we want to print only last n rows do df.tail(n)
#print(df1.tail(4))

#4.to print few selective rows
#print(df1[2:5])#prints 2,3,4

#4.to print the name of all the columns
#print(df.columns)

#4.to print a particular column
#print(df.day)# or also df['day'] but ['wind speed'] if spaces are there then we have to use only this type

#4.to print selective columns
#print(df[['event','day','temperature']])

#5.ype of columns
#print(type(df['event']))# it is always SERIES

#6.MAX and MIN
#print(df['temperature'].min())

#7.MEAN
#print(df['temperature'].mean())

#8.standard deviation
#print(df['temperature'].std())

#9.describe
#print((df.describe())


#10.conditionally select data
#print(df[df['temperature']>=32])
#print(df[df['temperature']==df.temperature.max()])

#11.to set index(nos: 0,1,2,3..)
#print(df.index)#prints range

#print(df.set_index('day'))#column day becomes the index instead of 0,1,2,3..

#to permanently change the index
#df.set_index('day',inplace=True)
#print(df)

#12.to get a particular row on the basis of the new index
#print(df.loc['1/1/2017'])

#to reset index
#df.reset_index(inplace=True)
#print(df)

#13.filling Nan
#there is a problem with any given data set if it has a unfilled data points.
#it showa Nan, so here Nan doesnt mean =0 but takes some junk value because of which value of AVG comes wrong
#so in order to make all the Nan spaces as 0 do the following
df1.fillna(0,inplace=True)
print(df1)#here Nan is replaced by 0






























