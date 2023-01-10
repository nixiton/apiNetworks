
from urllib.parse import urlparse

import logging

from .models import *

from .tasks import *

import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

"""
def saveToDB(filePath):
	try:
		json_data = open(filePath)  
		dictio = json.load(json_data)
		for society in dictio:
			sector = get_or_create_sector(society['sector'])
			soc = get_or_create_society(society['name'], sector, society['siren'])
			for result in society['results']:
				res = Result()
				res.ca = result['ca']
				res.margin = result['margin']
				res.loss = result['loss']
				res.ebitda = result['ebitda']
				res.year = result['year']
				res.society = soc
				res.save()
			#print(society)
		return {"error" : False, "value": "Saved to DB"}
	except Exception as e:
		return {"error" : True, "value": str(e)}
"""