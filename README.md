# Étapes de mise en service du projet

## Pré-requis
	-	git
	- 	docker
	- 	docker-compose

## Cloner le projet

## Dans un terminal (invite de commande), aller dans le dossier "deploy/"

## Build et mise en service des containers docker

	`docker-compose build`
	`docker-compose up`

## Accéder au backend
	Dans un navigateur à l'adresse "127.0.0.1:8000/"
### Initialiser la base de donnée 
	Dans un navigateur à l'adresse "127.0.0.1:8000/initDb/"
### Lister les entreprises
	Dans un navigateur à l'adresse "127.0.0.1:8000/list/"
### Voir les détails d'une entreprise
	Dans un navigateur à l'adresse "127.0.0.1:8000/detail/{idEntreprise}"

## Lancer les tests du backend 
Dans docker accéder au terminal du container "stats"
### Tests unitaires
	`python manage.py test`
	Un exemple de rendu est accessible dans Python_tests.png
### Tests de couverture
	`coverage run manage.py test`
	` coverage report`
	Un exemple de rendu est accessible dans test_coverage_report.png

## Accéder au frontend
	Dans un navigateur à l'adresse "127.0.0.1:3000/"


