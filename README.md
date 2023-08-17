[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
# Mini-Projet Calculatrice

Ce projet a été implémenté dans le but de s'entrainer au test unitaire à l'aide Pytest et UnitTest. Le code source
contient un mini-projet calculatrice qui permet d'effectuer 4 opérations différentes (addition, soustraction,
multiplication et division). Vous pourrez ainsi développer l'ensemble des scénarios nécessaires afin de tester
l'ensemble du code source. À noter que des propositions de corrections sont mises à disposition dans différentes branches
du répertoire.

## Pré-requis

* Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)
* Installer git : [Téléchargement Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

## Installation

### 1. Télécharger le projet sur votre répertoire local :
```
git clone https://github.com/OpenClassrooms-Student-Center/4425126-testing-python.git
cd 4425126-testing-python
```
### 2. Mettre en place un environnement virtuel :
* Créer l'environnement virtuel:
`python -m venv venv`
`pip3 install virtualenv`

* Activer l'environnement virtuel :
    * Windows : `venv\Scripts\activate.bat`
    * Unix/MacOS : `source venv/bin/activate`


### 3. Installer les dépendances du projet
```
pip install -r requirements.txt
```

## Démarrage
* Lancer le projet Flask:

Windows/Linux
```
$env:FLASK_APP = "server.py"
flask run
```

Mac
```
export FLASK_APP=server.py
flask run
```


## Corrections
1. Proposition de correction pour les tests unitaires avec UnitTest :
```

4. Executez les tests unitairs:
```
git checkout QA
pytest
```


