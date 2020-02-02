import pandas as pd
df=pd.read_csv('weather1.csv')
#print(df)

#pivoting helps in transforming the structure of the table:
#index: the data that you want to be displayed as index
#columns: the data that you want as your title names
#humidity: the data that you want as the values in the data set 
df1=df.pivot(index="date",columns="city",values="humidity")
#print(df1)




#pivot tables:summarizes and aggregates the tabular data
df=pd.read_csv('weather2.csv')
df2=df.pivot_table(index="city",columns="date")
#print(df2)#gives mean value after aggregating data for each day


#by default it does mean
#but we can change the operation too
df2=df.pivot_table(index="city",columns="date",aggfunc="sum")#to sum them up
#print(df2)
#"count","diff"....are rest of the aggfunc...google it

#to get mean value of the whole row displayed
df2=df.pivot_table(index="city",columns="date",margins=True)
#print(df2)





df=pd.read_csv('weather3.csv')
df['date']=pd.to_datetime(df['date'])#to convert it to time stamp format

#grouper function:aggregates on the basis of dates
df1=df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')#M for months(its frequency is used for aggregation) and dtae is considered to do thid
print(df1)
