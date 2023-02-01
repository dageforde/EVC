import pandas as pd
import requests
import psycopg2

conn = psycopg2.connect(dbname='sqlpad',
                        user='cdag527_gmail_com', 
                        password='8274',
                        host='68.183.51.176')
cur = conn.cursor()
# cur.execute("select * from all_records LIMIT 5;")
# print(cur.fetchall())

r = requests.get('https://k4clzaf58d.execute-api.us-east-1.amazonaws.com/default/handle_users')
# print(r.status_code)
data = r.json()
df = pd.DataFrame.from_records(data['data'])
# print(df.head(1))
# print(df.columns)

df_csv = pd.read_csv('./data/vendor_x_data.csv')
# print(df_csv.head())
# print(df_csv.columns)
df_csv.columns = map(str.lower, df_csv.columns)
df.columns = df_csv.columns

