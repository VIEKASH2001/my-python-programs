import pandas as pd

#READ CSV


#1.to skip the unimportant rows from top    
df1=pd.read_csv('stock_data.csv',skiprows=1)#as the required data starts from 1st row or can also use pd.read_csv('stock_data.csv',header=1)
#print(df1)

#2.if in case title for each column is missing then to auto generate titles:
df2=pd.read_csv('stock_data.csv',header=None)
#print(df2)

#3.inorder to give names for columns instead of 0,1,2,3,4... i above
df3=pd.read_csv('stock_data.csv',header=None,names=["tickers","eps","revenue","price","people"])
#print(df3)

#4.to read only particular rows
df4=pd.read_csv('stock_data.csv',nrows=3)
#print(df4)

#5.Na values are made into Nan
df5=pd.read_csv('stock_data.csv',na_values=["not available","n.a."])
#print(df5)

#6.to manage unfair data
#revenue cannot be negative
#so we change itto Nan
#do this by selectively give Nan values
df6=pd.read_csv('stock_data.csv',na_values={'eps':["not available","n.a."],
                                            'revenue':["not available","n.a.",-1],
                                            'people':["not available","n.a."]
                                            })
#7.to change data type
df=pd.read_csv('weather.csv')
print(type(df.day[0]))
#this gives string as out put
#but you want the dates to be of type "time stamp"
#so read it differently
df=pd.read_csv('weather.csv',parse_dates=["day"])
print(type(df.day[0]))#now we get the desired type
print(df)#now see the date coumn, the format would have changed

#print(df6)

#WRITE TO CSV



#1.writing into a new csv file
df6.to_csv('new.csv')#creates csv file in which the data of cf6 is written into

#2.in the above we also recive the index, to avoid it:
df6.to_csv('new.csv',index=False)

#3.to specifically write columns
df6.to_csv('new.csv',columns=['tickers','eps'])

#3.to remove header
df6.to_csv('new.csv',header=False)



#READ EXCEL



#1.to convert a oarticular data from one to another
def convert_people_cell(cell):
    if(cell=="n.a."):
       return 'sam walton'
    return cell

df1=pd.read_excel("stock_data.xlsx",converters={'people':convert_people_cell})
print(df1)

#rest all are the same as CSV


#WRITE TO EXCEL



#1.writing into a new excel file
df1.to_excel("new.xlsx",sheet_name="stocks")

#2.to select the location in excel file and write 
df1.to_excel("new.xlsx",sheet_name="stocks",startrow=1,startcol=2)

#3.to write 2 data frames into the same excel file in 2 different sheets:
#the below are the 2 data frames
df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")


#rest all are the same as CSV




