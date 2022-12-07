import csv
import json
import pandas as pd

# input_file = csv.DictReader(open("clean.csv"))
df=pd.read_csv("clean.csv")
df = df.rename({'Unnamed: 0.1':'ID','Unnamed: 0': 'Read ID'}, axis=1)

columns=['Read ID', 'Date Time', 'NOx', 'NO2', 'NO', 'PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5', 'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure', 'Location']

# print(df[ columns])

#['ID', 'Read ID', 'Date Time', 'NOx', 'NO2', 'NO', 'SiteID', 'PM10','NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5', 'VPM2.5', 'CO', 'O3', 'SO2','Temperature', 'RH', 'Air Pressure', 'Location', 'geo_point_2d', 'DateStart', 'DateEnd', 'Current', 'Instrument Type']

# print (df)

# df = (
#     df[['ID']]
#     .apply(pd.Series)
#     .merge(df, left_index=True, right_index = True)
# )

# print(df.columns)
df=df.set_index('ID')
df=df.head(10)

df.to_json('nosql.json',orient='index')

# (df.groupby([ 'Read ID', 'Date Time', 'NOx', 'NO2', 'NO', 'PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5', 'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure', 'Location'], as_index=False)
#    .apply(lambda x: dict(zip(x.ID,x.SiteID)))
#    .reset_index()
#    .rename(columns={0:'Tide-Data'})
#    .to_json('./file_name.json', orient='records'))

# result=[]
 


# for row in input_file:
#      result.append(json.dumps(row))
# input_file=json.dumps(input_file)

# result=json.loads(input_file)


# with open('json_data.json', 'w') as outfile:
#     outfile.write(json.decoder(result) )
 
# print(result)

# with open('json_data.json', 'w') as f:
#     json.dump(result, f)