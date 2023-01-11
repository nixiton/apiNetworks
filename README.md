# Étapes de mise en service du projet

## Pré-requis
	-	git
	- 	docker
	- 	docker-compose

## Cloner la branche dev du projet

## Dans un terminal (invite de commande), aller dans le dossier "deploy/"
	- Lancer docker

## Build et mise en service des containers docker

	```docker-compose build```
	```docker-compose up```

## Initialiser la base donnée
Dans docker accéder au terminal du container "stats" puis executer la commande
	```python manage.py init_db```

## Accéder à l'API
	Dans un navigateur à l'adresse "127.0.0.1:8000/networkApi/?q = [l'adresse à rechercher]"



