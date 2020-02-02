import pandas as pd

df=pd.read_csv('city_weather.csv')
#print(df)
#reshaping is done to change the dimensions of the data frame to the desired dimensions
df1=pd.melt(df,id_vars=["day"])
#print(df1)

#to display a particular variable alone:
#just simply use conditions
df1=pd.melt(df,id_vars=["day"])
#print(df1[df1["variable"]=="chicago"])

#to change the name of the columns from variable and value to something else:
df1=pd.melt(df,id_vars=["day"],var_name="city",value_name="temperature")
#print(df1)
