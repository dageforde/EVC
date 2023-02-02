import pandas as pd
import requests

'''Pull data from API'''
r = requests.get('https://k4clzaf58d.execute-api.us-east-1.amazonaws.com/default/handle_users')
# print(r.status_code)
data = r.json()
df = pd.DataFrame.from_records(data['data'])
# print(df.head(1))
# print(df.columns)

'''Read data from CSV'''
df_csv = pd.read_csv('./data/vendor_x_data.csv')
# print(df_csv.head())
# print(df_csv.columns)

'''Standardize column names. I'm following the naming conventions of the data from the CSV since the column names match the target schema.'''
df_csv.columns = map(str.lower, df_csv.columns)
df.columns = df_csv.columns

'''concatenate dataframes'''
frames = [df,df_csv]
joined_df = pd.concat(frames, ignore_index=True)

'''Given more time, this is where I would write a function to clean the joined dataframe.
This function would look at missing data and based on the volume of missing values, would follow conditions for filling or imputing the missing values.
With more time, I would do some more exploratory data analysis to find individual columns with data cleaning issues and take measures to enforce consistency across the dataframe.
'''

'''Write data to csv'''
joined_df.to_csv('./data/all_vendors.csv', index=False)

'''Write data to sql'''
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://cdag527_gmail_com:8274@68.183.51.176:5432/sqlpad")
joined_df.to_sql('all_vendors', con=engine, schema="s_69cd1f4046f393adf2a7697f8ae5a8f9", if_exists='append', index=False)