============
Installation
============

Prérequis
=========

* Python 3.11 ou supérieur
* Git
* Docker (optionnel)
* Compte GitHub avec accès au repository

Installation locale
===================

1. Cloner le repository
-----------------------

.. code-block:: bash

    git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
    cd Python-OC-Lettings-FR

2. Créer l'environnement virtuel
---------------------------------

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate

3. Installer les dépendances
-----------------------------

.. code-block:: bash

    pip install -r requirements.txt

4. Configuration des variables d'environnement
-----------------------------------------------

Copier le fichier ``.env.example`` vers ``.env`` et configurer les variables :

.. code-block:: bash

    cp .env.example .env

Éditer le fichier ``.env`` avec vos valeurs :

* ``SECRET_KEY`` : Clé secrète Django (générer une nouvelle pour la production)
* ``DEBUG`` : True pour le développement, False pour la production
* ``ALLOWED_HOSTS`` : Liste des domaines autorisés
* ``SENTRY_DSN`` : DSN Sentry pour le monitoring (optionnel)

5. Appliquer les migrations
----------------------------

.. code-block:: bash

    python manage.py migrate

6. Créer un superutilisateur (optionnel)
-----------------------------------------

.. code-block:: bash

    python manage.py createsuperuser

Installation avec Docker
========================

1. Construire l'image
---------------------

.. code-block:: bash

    docker-compose build

2. Lancer l'application
------------------------

.. code-block:: bash

    docker-compose up

L'application sera accessible sur http://localhost:8000