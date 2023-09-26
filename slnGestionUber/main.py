
# main:

##########################################

import uvicorn

##########################################

def webapi_gestionuber():
	uvicorn.run(
				"application.WebAPIGestionUber:app",
				host="127.0.0.1",
				port=8060,
				reload=True
			)

##########################################

if __name__ == '__main__':
	webapi_gestionuber()

##########################################
"""
https://www.freecodecamp.org/espanol/news/subir-a-github-lo-suficientemente-simple-para-poetas/
git clone https://github.com/CarlosSuaza/GestionUber.git
git branch
git init
git add .
git commit -m "USBGD202302 - Actualizacion 20230920"
git remote add origin https://github.com/nombreDeUsuario/repositorio.git
git remote -v
	main    https://github.com/CarlosSuaza/GestionUber.git (fetch)
	main    https://github.com/CarlosSuaza/GestionUber.git (push)
	origin  https://github.com/CarlosSuaza/GestionUber (fetch)
	origin  https://github.com/CarlosSuaza/GestionUber (push)
git push origin master
"""