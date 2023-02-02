import pandas as pd
import requests
import psycopg2

# conn = psycopg2.connect(dbname='sqlpad',
#                         user='cdag527_gmail_com', 
#                         password='8274',
#                         host='68.183.51.176')
# cur = conn.cursor()
# # cur.execute("select * from all_records LIMIT 5;")
# # print(cur.fetchall())

r = requests.get('https://k4clzaf58d.execute-api.us-east-1.amazonaws.com/default/handle_users')
# print(r.status_code)
data = r.json()
df = pd.DataFrame.from_records(data['data'])
# print(df.head(1))
# print(df.columns)

# standardize columns
df_csv = pd.read_csv('./data/vendor_x_data.csv')

# print(df_csv.head())
# print(df_csv.columns)
df_csv.columns = map(str.lower, df_csv.columns)
df.columns = df_csv.columns

# #concatenate dfs
frames = [df,df_csv]
joined_df = pd.concat(frames, ignore_index=True)
# joined_df.astype(dtype= {'vendor_id':'object', 
#                         'status':'object', 
#                         'tracking_source':'object', 
#                         'tracking_id':'object',
#                         'date_of_birth':'datetime64', 
#                         'email_address':'object', 
#                         'citizenship_confirmed':'bool', 
#                         'salutation':'object',
#                         'first_name':'object', 
#                         'middle_name':'object', 
#                         'last_name':'object', 
#                         'name_suffix':'object', 
#                         'home_address':'object',
#                         'home_unit':'int', 
#                         'home_city':'object', 
#                         'home_county':'object', 
#                         'home_state':'object', 
#                         'home_zip_code':'object',
#                         'mailing_address':'object', 
#                         'mailing_unit':'int', 
#                         'mailing_city':'object', 
#                         'mailing_county':'object',
#                         'mailing_state':'object', 
#                         'mailing_zip_code':'object', 
#                         'party':'object', 
#                         'race':'object', 
#                         'phone':'object',
#                         'phone_type':'object',
#                         'opt_in_to_vendor_email':'bool', 
#                         'opt_in_to_vendor_sms':'bool',
#                         'opt_in_to_partner_email':'bool', 
#                         'opt_in_to_partner_smsrobocall':'bool',
#                         'volunteer_for_vendor':'bool',
#                         'volunteer_for_partner':'bool', 
#                         'pre_registered':'bool',
#                         'registration_date':'datetime64',
#                         'finish_with_state':'bool', 
#                         'built_via_api':'bool',
#                         'submitted_via_state_api':'bool', 
#                         'registration_source':'object',
#                         'shift_id':'int',
#                         'shift_type':'int', 
#                         'office':'object', 
#                         'vendor_a_shift_id':'int', 
#                         'salutation_standardized':'object',
#                         'has_mailing_address_standardized':'bool', 
#                         'has_state_license_standardized':'bool',
#                         'has_ssn_standardized':'bool', 
#                         'predicted_gender':'object', 
#                         'org':'object', 
#                         'evc_id':'object',
#                         'program_state':'object', 
#                         'partner_id':'int', 
#                         'field_start':'datetime64', 
#                         'field_end':'datetime64'})
print(joined_df.dtypes)
# # save to csv
# joined_df.to_csv('all_vendors.csv', index=False)


