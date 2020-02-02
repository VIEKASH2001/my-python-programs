import pandas as pd

#1.from CSV
df1=pd.read_csv('nyc_weather.csv')

#2.from EXCEL
df2=pd.read_excel("weather_data.xlsx")#to put one particular sheet in the excel file: df2=pd.read_excel("weather_data.xlsx","sheet1")
print(df2)
#3.creating data frame using python dictionary
wether_data={#python dictionary
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,34,26],
    'windspeed': [3,4,7],
    'event': ['Rain','sunny','snow']
    }
df3=pd.DataFrame(wether_data)#convert this to a pandas dataframe

#4.creating data frame using python tuples/lists: without column names
weather_data = [
('1/1/2017', 32, 6, 'Rain'),
('1/2/2017', 35, 7, 'Sunny'),
('1/3/2017', 28, 2, 'Snow')
]
df4=pd.DataFrame(wether_data,columns=["day","temperature","windspeed","event"])
print(df4)

#5. creating data frame using python tuples/lists: with column names
weather_data = [
{'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
{'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
{'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'}
]
df5=pd.DataFrame(wether_data)
