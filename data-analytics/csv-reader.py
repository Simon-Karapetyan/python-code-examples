
import numpy as np
import pandas as pd
import os

# --------- reading data from an csv file
# data = pd.read_csv('csv/data.csv')
# data = pd.read_csv('csv/big-data.csv')


# --------- reading data from an xlsx file
# df = pd.read_excel('data.xlsx')


# --------- reading data from database
# --------- Creating a connection to a SQLite database
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///example.db')
# data = pd.read_sql('SELECT * FROM my_table', engine)


# --------- reading data from API
# import requests
# url = 'https://api.example.com/data'
# response = requests.get(url)
# data = response.json()



# --------- printing data
# print(data) # prints all rows
# print(data.head(1)) # prints first rows
# print(data.shape) # prints shape
# print(data.info()) # prints information
# print(data.describe()) # prints describtion
# print(sorted(data["Level"])[0:8]) # prints sorted by Level



# --------- filtering data
# skills = data.dtypes[data.dtypes == 'object'].index
# print(skills)



# del data["Level"] # deletes column



# --------- transforming data, now we can see counts and frequencies of each category
# new_category = pd.Categorical(data["Variable_category"])
# new_category = new_category.rename_categories(["Financial performance", "Financial position", "Financial ratios"])
# print(new_category.describe())



# --------- converting string values to numbers
# data['Value'] = pd.to_numeric(data['Value'], errors='coerce').fillna(0).astype(int)



# --------- plotting data
# import matplotlib.pyplot as plt
# # print(data.hist(column="Value", bins=50, figsize=(9, 6)))
# print(data["Value"].plot(kind="box", figsize=(9, 6)))
# plt.show()
