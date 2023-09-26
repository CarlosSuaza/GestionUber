
# GeografiaBroker: 

##########################################

import pymongo
import json

##########################################

from core.domain.geografia.GeografiaModel import ModeloGeografia
from pymongo import MongoClient

##########################################

class BrokerGeografia:
	
	def ingresar_geografia(self, geografia: ModeloGeografia | None = None):
		URL = "mongodb+srv://dbaUsername:dbaPassword@cluster0.cl9qw2d.mongodb.net/dbaUber?retryWrites=true&w=majority"
		client = pymongo.MongoClient(URL)
		db = client["dbaUber"]
		col = db["Geografia"]

		data = json.dumps(geografia)
		resultado = col.insert_one(data)
		geografia.Resultado = resultado.inserted_id

		client.close()
		return geografia

	def modificar_geografia(self, geografia: ModeloGeografia | None = None):
		URL = "mongodb+srv://dbaUsername:dbaPassword@cluster0.cl9qw2d.mongodb.net/dbaUber?retryWrites=true&w=majority"
		client = pymongo.MongoClient(URL)
		db = client["dbaUber"]
		col = db["Geografia"]

		client.close()
		return geografia

	def retirar_geografia(self, geografia: ModeloGeografia | None = None):
		URL = "mongodb+srv://dbaUsername:dbaPassword@cluster0.cl9qw2d.mongodb.net/dbaUber?retryWrites=true&w=majority"
		client = pymongo.MongoClient(URL)
		db = client["dbaUber"]
		col = db["Geografia"]

		client.close()
		return geografia

	def consultar_geografia(self, geografia: ModeloGeografia | None = None):
		URL = "mongodb+srv://dbaUsername:dbaPassword@cluster0.cl9qw2d.mongodb.net/dbaUber?retryWrites=true&w=majority"
		client = pymongo.MongoClient(URL)
		db = client["dbaUber"]
		col = db["Geografia"]
		
		resultado = col.find()
		#geografia = json.loads(json_str)
		for x in resultado:
			print(x)

		client.close()
		return geografia

	def consultarid_geografia(self, geografia: ModeloGeografia | None = None):
		URL = "mongodb+srv://dbaUsername:dbaPassword@cluster0.cl9qw2d.mongodb.net/dbaUber?retryWrites=true&w=majority"
		client = pymongo.MongoClient(URL)
		db = client["dbaUber"]
		col = db["Geografia"]

		client.close()
		return geografia


##########################################