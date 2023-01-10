import pandas
import pyproj
import warnings
import os
import numpy
import io

from pandarallel import pandarallel
import requests

warnings.filterwarnings("ignore", category=FutureWarning)

# Initialization
#pandarallel.initialize()
pandarallel.initialize(progress_bar=True, nb_workers=os.cpu_count())

def get_data_frame():
    data_frame = pandas.read_csv('static/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv',
                                          header=0,
                                          delimiter=';')
    
    data_frame.dropna(subset=['X', 'Y'], inplace=True)
    data_frame.drop_duplicates(inplace=True)
    
    return data_frame

def replace_code_by_operator(data_frame):
	#codes_df = data_frame['Operateur']
	#codes_df.drop_duplicates(inplace=True)
	codes_op_df = get_operator_code_dataframe()
	codes_op_df = codes_op_df.rename(columns = {"MCC-MNC" : "Operateur"})
	codes_op_df = pandas.merge(data_frame,codes_op_df, on = 'Operateur')
	codes_op_df.drop_duplicates(inplace=True)
	codes_op_df.drop(['Operateur'], axis=1, inplace=True)
	codes_op_df = codes_op_df.rename(columns = {"Nom" : "Operateur"})
	return codes_op_df

def get_operator_code_dataframe():
	data_frame = pandas.read_csv('static/mcc_mnc_codes.csv',
                                          header=0,
                                          delimiter=',')
	data_frame.drop_duplicates(inplace=True)
	return data_frame

def lamber93_to_gps(x, y):
	lambert = pyproj.Proj('+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
	wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
	lng, lat = pyproj.transform(lambert, wgs84, x, y)
	return lat, lng


def replace_lambert93_by_gps(df):
	dfXY = df[['X', 'Y']].copy()
	dfXY[['lat', 'lng']] = dfXY.parallel_apply(lambda row : pandas.Series((lamber93_to_gps(row['X'], row['Y']))), axis = 1)
	dfXY.drop(['X', 'Y'],axis=1, inplace=True)
	df = pandas.concat([df, dfXY], axis=1)
	df.drop(['X', 'Y'],axis=1, inplace=True)
	df.to_csv('static/processed_op_gps_df.csv', index=False)
	return df

def get_city_from_gps(csvFile):
	resp = requests.post('https://api-adresse.data.gouv.fr/reverse/csv/', files={'data': csvFile})
	resp.raise_for_status()
	data = resp.text
	return data

def replace_long_lat_by_city(df):
	dfLl = df[['lat', 'lng']]
	dfLl.to_csv('static/dfLl.csv', index=False)
	with open('static/dfLl.csv') as csvFile:
		data = get_city_from_gps(csvFile)
	buffer = io.StringIO(data)
	data_df = pandas.read_csv(buffer, delimiter=',', header=0)
	data_df.dropna(subset=['result_city'], inplace=True)

	df = df.round({'lng': 2, 'lat': 2})
	data_df = data_df[['lng', 'lat', 'result_city']]
	data_df = data_df.round({'lng': 2, 'lat': 2})

	op_city_df = pandas.merge(df,data_df, on = ['lat','lng']).drop(['lat', 'lng'], axis = 1)
	op_city_df.drop_duplicates(inplace=True)
	op_city_df.to_csv('static/op_city_df.csv', index=False)
	return op_city_df

#df = get_data_frame()
#op_df = replace_code_by_operator(df)
#op_gps_df = replace_lambert93_by_gps(op_df)
#op_gps_df = pandas.read_csv('static/processed_op_gps_df.csv',
#                                          header=0,
#                                          delimiter=',')
#op_city_df = replace_long_lat_by_city(op_gps_df)
op_city_df = pandas.read_csv('static/op_city_df.csv',
                                          header=0,
                                          delimiter=',')

print(op_city_df)

