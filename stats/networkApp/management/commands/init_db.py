from django.core.management.base import BaseCommand, CommandError
from networkApp.models import *
import pandas

class Command(BaseCommand):
    help = 'Populates the database with the datas from static/op_city_df.csv.'

    def handle(self, *args, **options):
        try:
        	op_city_df = pandas.read_csv('static/op_city_df.csv',
	                                          header=0,
	                                          delimiter=',')
        	createCities(op_city_df)
        	createOperators(op_city_df)
        	createNetworks(op_city_df)
        	createNetworkOperatorCity(op_city_df)
        except Exception as e:
        	raise 


def createCities(df):
	df_city = df['result_city']
	df_city.drop_duplicates(inplace=True)
	cities = []
	for row in df_city:
		city = City(name = row.encode('utf-8') )
		cities.append(city)
	City.objects.bulk_create(cities, ignore_conflicts = True)

def createOperators(df):
	df_op = df['Operateur']
	df_op.drop_duplicates(inplace=True)
	ops = []
	for row in df_op:
		op = Operator(name = row)
		ops.append(op)
	Operator.objects.bulk_create(ops, ignore_conflicts = True)


def createNetworks(df):
	df_net = df[['2G', '3G', '4G']].copy()
	df_net.drop_duplicates(inplace=True)
	nets = []
	for index, row in df_net.iterrows():
		#print(row)
		net = Network(name =str(row["2G"])+str(row["3G"])+str(row["4G"]) ,twoG = row['2G'], threeG = row['3G'], fourG = row['4G'])
		nets.append(net)
	Network.objects.bulk_create(nets, ignore_conflicts = True)

def createNetworkOperatorCity(df):
	df.drop_duplicates(inplace=True)
	nocs = [] 
	for index, row in df.iterrows():

		city = get_or_create_city(row['result_city'])
		op = get_or_create_operator(row['Operateur'])
		net = get_or_create_network(str(row["2G"])+str(row["3G"])+str(row["4G"]))

		noc = NetworkOperatorCity(city = city, operator = op, network = net)

		nocs.append(noc)
	NetworkOperatorCity.objects.bulk_create(nocs, ignore_conflicts = True)






