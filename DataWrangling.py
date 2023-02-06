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

'''This is where I would write a function to clean the joined dataframe.
This function would look at missing data and based on the volume of missing values, would follow conditions for filling or imputing the missing values.
With more time, I would do some more exploratory data analysis to find individual columns with data cleaning issues and take measures to enforce consistency across the dataframe.
'''

'''Write data to csv'''
joined_df.to_csv('./data/all_vendors.csv', index=False)

'''Create DB connection. Create schema. Create table. Load dataframe to table.
Note: The the DB is not accepting this schema.'''
from sqlalchemy import create_engine
import psycopg2
import sys
username = sys.argv[0]
host = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
port = sys.argv[4]

conn = psycopg2.connect(dbname='sqlpad',
                        user='cdag527_gmail_com', password='8274',
                        host='68.183.51.176')
cur = conn.cursor()
create_schema_query = """CREATE SCHEMA IF NOT EXISTS s_69cd1f4046f393adf2a7697f8ae5a8f9 AUTHORIZATION cdag527_gmail_com;"""
create_table_query = """
                     CREATE TABLE IF NOT EXISTS s_69cd1f4046f393adf2a7697f8ae5a8f9.all_vendors (vendor_id varchar(1024),
                                                                                                status varchar(1024),
                                                                                                tracking_source varchar(1024),
                                                                                                tracking_id varchar(1024),
                                                                                                date_of_birth date,
                                                                                                email_address varchar(1024),
                                                                                                citizenship_confirmed bool,
                                                                                                salutation varchar(1024),
                                                                                                first_name varchar(1024),
                                                                                                middle_name varchar(1024),
                                                                                                last_name varchar(1024),
                                                                                                name_suffix varchar(1024),
                                                                                                home_address varchar(1024),
                                                                                                home_unit int,
                                                                                                home_city varchar(1024),
                                                                                                home_country varchar(1024),
                                                                                                home_zip_code varchar(1024),
                                                                                                mailing_address varchar(1024),
                                                                                                mailing_unit int,
                                                                                                mailing_city varchar(1024),
                                                                                                mailing_country varchar(1024),
                                                                                                mailing_state varchar(1024),
                                                                                                mailing_zip_code varchar(1024),
                                                                                                party varchar(1024),
                                                                                                race varchar(1024),
                                                                                                phone varchar(1024),
                                                                                                phone_type varchar(1024),
                                                                                                opt_in_to_vendor_email bool,
                                                                                                opt_in_to_vendor_sms bool,
                                                                                                opt_in_to_partner_email bool,
                                                                                                opt_in_to_partner_smsrobocall bool,
                                                                                                volunteer_for_vendor bool,
                                                                                                volunteer_for_partner bool,
                                                                                                pre_registered bool,
                                                                                                registration_date timestamp,
                                                                                                finish_with_state bool,
                                                                                                built_via_api bool,
                                                                                                submitted_via_state_api bool,
                                                                                                registration_source varchar(1024),
                                                                                                shift_id int,
                                                                                                shift_type int,
                                                                                                office varchar(1024),
                                                                                                vendor_a_shift_id int,
                                                                                                salutation_standardized varchar(1024),
                                                                                                has_mailing_address_standardized bool,
                                                                                                has_state_license_standardized bool,
                                                                                                has_ssn_standardized bool,
                                                                                                predicted_gender varchar(1024),
                                                                                                org varchar(1024),
                                                                                                evc_id varchar(1024),
                                                                                                program_state varchar(1024),
                                                                                                partner_id int,
                                                                                                field_start timestamp,
                                                                                                field_end timestamp);;
                                                                                                """
cur.execute(create_schema_query, create_table_query)

engine = create_engine("postgresql+psycopg2://"+username+":"+password+"@"+host+':'+port+'/'+database)
joined_df.to_sql('all_vendors', con=engine, schema="s_69cd1f4046f393adf2a7697f8ae5a8f9", if_exists='append', index=False)