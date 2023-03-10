
from urllib.parse import urlparse

import pgeocode


def getNetworkGroupedByOperators(list):
	playload = {}
	for row in list:
		op = row.operator.name
		net = row.network
		if op not in playload:
			playload[op] = {"2G": net.twoG, "3G" : net.threeG, "4G" : net.fourG}
		else:
			playload[op]["2G"] = playload[op]["2G"] if playload[op]["2G"] else net.twoG
			playload[op]["3G"] = playload[op]["3G"] if playload[op]["3G"] else net.threeG
			playload[op]["4G"] = playload[op]["4G"] if playload[op]["4G"] else net.fourG

	return playload

def getCityFromPostCode(postCode):
	nomi = pgeocode.Nominatim('fr')
	city = nomi.query_postal_code(postCode)
	return city[5]