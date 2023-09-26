
# WebAPIGestionUber:

##########################################

from fastapi import FastAPI 

from core.domain.geografia.GeografiaModel import ModeloGeografia
from core.broker.geografia.GeografiaBroker import BrokerGeografia

app: FastAPI = FastAPI(
						title='Web API Gestion Uber',
						description='USBGS - 202302'
						)

##########################################

@app.post(
		"/ingresargeografia",
		response_model=ModeloGeografia,
		summary="Ingresar Geografia",
		description="API para Ingresar Geografia",
		tags=["Geografia"]
		)
async def ingresar_geografia(geografia: ModeloGeografia | None = None):
	brokergeografia = BrokerGeografia()
	return brokergeografia.ingresar_geografia(geografia)

@app.post(
		"/modificargeografia",
		response_model=ModeloGeografia,
		summary="Modificar Geografia",
		description="API para Modificar Geografia",
		tags=["Geografia"]
		)
async def modificar_geografia(geografia: ModeloGeografia | None = None):
	brokergeografia = BrokerGeografia()
	return brokergeografia.modificar_geografia(geografia)

@app.post(
		"/retirargeografia",
		response_model=ModeloGeografia,
		summary="Retirar Geografia",
		description="API para Retirar Geografia",
		tags=["Geografia"]
		)
async def retirar_geografia(geografia: ModeloGeografia | None = None):
	brokergeografia = BrokerGeografia()
	return brokergeografia.retirar_geografia(geografia)

@app.post(
		"/consultargeografia",
		response_model=ModeloGeografia,
		summary="Consultar Geografia",
		description="API para Consultar Geografia",
		tags=["Geografia"]
		)
async def consultar_geografia(geografia: ModeloGeografia | None = None):
	brokergeografia = BrokerGeografia()
	return brokergeografia.consultar_geografia(geografia)

@app.post(
		"/consultaridgeografia",
		response_model=ModeloGeografia,
		summary="Consultar Id Geografia",
		description="API para Consultar Id Geografia",
		tags=["Geografia"]
		)
async def consultarid_geografia(geografia: ModeloGeografia | None = None):
	brokergeografia = BrokerGeografia()
	return brokergeografia.consultarid_geografia(geografia)

##########################################