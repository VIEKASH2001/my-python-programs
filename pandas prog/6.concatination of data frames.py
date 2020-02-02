import pandas as pd

india=pd.DataFrame({
    'city':['mumbai','delhi','banglore'],
    'temperature':[32,45,30],
    "humidity":[80,60,78]
    })

us=pd.DataFrame({
    'city':['newyork','chicago','orlando'],
    'temperature':[21,14,35],
    "humidity":[68,65,75]
    })

#to concatinate
df=pd.concat([india,us],ignore_index=True)#we can concatinate more than 2 dataframe also
#print(df)

#to create an additional index to group both the data with the key name we wnt it to have    
df=pd.concat([india,us],keys=["india","us"])
#print(df)

#using this we can retrive the subset of our data set
#print(df.loc["india"])


temp=pd.DataFrame({
    'city':['mumbai','delhi','banglore'],
    'temperature':[32,45,30]
    },index=[0,1,2])#we can accordingly fix the index

windspeed=pd.DataFrame({
    'city':['mumbai','delhi','banglore'],
    'windspeed':[7,12,9]
    },index=[1,0,2])

#now we want to append this data horizontally instead of vertically
df=pd.concat([temp,windspeed],axis=1)
#print(df)#have a look at the index and the city order to how they have changed

#appending series with data framw, to add columns to the data
s=pd.Series(["humid","dry","Rain"], name="event")
df=pd.concat([temp,s],axis=1)
print(df)
