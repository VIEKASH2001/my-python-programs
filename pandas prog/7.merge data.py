import pandas as pd

df1=pd.DataFrame({
    'city':['mumbai','delhi','banglore'],
    'temperature':[32,45,30],
    })

df2=pd.DataFrame({
    'city':['mumbai','delhi','banglore'],
    'humidity':[42,53,31],
    })


#inorder to concatinate without fixing the index, by using city names
df3=pd.merge(df1,df2,on='city')#the column on which the merge is to be performed is city
#print(df3)

#now if we have one city different in each df
df1=pd.DataFrame({
    'city':['mumbai','delhi','banglore','chennai'],
    'temperature':[32,45,30,67],
    })

df2=pd.DataFrame({
    'city':['mumbai','delhi','banglore','kolkota'],
    'humidity':[42,53,31,76]
    })
df3=pd.merge(df1,df2,on='city')
#print(df3)#in this case only the common cities are displayed
#this follows intersection operation, only the data common to both the sets is displayed


#now inorder to perform a union:

df3=pd.merge(df1,df2,on='city',how="outer")#by default how=inner,intersection
#print(df3)

#to get the common element of two sets and the remaining element of left set (df1):

df3=pd.merge(df1,df2,on='city',how="left")#same way right can also be put
#print(df3)

#to know the information about the data that from which set it came from:

df3=pd.merge(df1,df2,on='city',how="outer",indicator=True)
#print(df3)


#to add sufixes to the column names
df1=pd.DataFrame({
    'city':['mumbai','delhi','banglore'],
    'temperature':[32,45,30],
    'humidity':[42,53,31]
    })

df2=pd.DataFrame({
    'city':['mumbai','delhi','banglore'],
    'humidity':[42,53,31],
    'temperature':[32,45,30]
    })

df3=pd.merge(df1,df2,on='city',suffixes=('_left','_right'))
print(df3)


