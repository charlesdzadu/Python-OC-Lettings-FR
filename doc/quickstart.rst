======================
Guide de démarrage rapide
======================

Ce guide vous permet de démarrer rapidement avec l'application OC Lettings Site.

Démarrage en 5 minutes
=======================

1. **Cloner le projet**

.. code-block:: bash

    git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
    cd Python-OC-Lettings-FR

2. **Installer les dépendances**

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    pip install -r requirements.txt

3. **Configurer l'environnement**

.. code-block:: bash

    cp .env.example .env
    # Éditer .env si nécessaire (optionnel pour le développement)

4. **Lancer l'application**

.. code-block:: bash

    python manage.py runserver

5. **Accéder à l'application**

Ouvrir votre navigateur et aller sur http://localhost:8000

Démarrage avec Docker
======================

Pour une installation encore plus rapide avec Docker :

.. code-block:: bash

    docker-compose up

L'application sera accessible sur http://localhost:8000

Commandes essentielles
======================

**Lancer les tests**

.. code-block:: bash

    pytest

**Vérifier la qualité du code**

.. code-block:: bash

    flake8

**Accéder au panel d'administration**

- URL : http://localhost:8000/admin
- Utilisateur : admin
- Mot de passe : Abc1234!

**Créer un superutilisateur**

.. code-block:: bash

    python manage.py createsuperuser

**Appliquer les migrations**

.. code-block:: bash

    python manage.py migrate

**Collecter les fichiers statiques**

.. code-block:: bash

    python manage.py collectstatic

Premiers pas
============

Une fois l'application lancée, vous pouvez :

1. **Parcourir les locations** : Cliquez sur "Lettings" depuis la page d'accueil
2. **Voir les profils** : Cliquez sur "Profiles" depuis la page d'accueil
3. **Administrer le site** : Connectez-vous au panel admin pour gérer les données

Structure des URLs principales
================================

- ``/`` : Page d'accueil
- ``/lettings/`` : Liste des locations
- ``/lettings/<id>/`` : Détail d'une location
- ``/profiles/`` : Liste des profils
- ``/profiles/<username>/`` : Détail d'un profil
- ``/admin/`` : Panel d'administration

Données de test
===============

La base de données SQLite fournie contient déjà des données de test :

- Plusieurs locations avec leurs adresses
- Plusieurs profils d'utilisateurs
- Un compte administrateur préconfiguré

Résolution des problèmes courants
==================================

**Erreur "Port 8000 already in use"**

.. code-block:: bash

    # Utiliser un autre port
    python manage.py runserver 8080

**Problème de permissions sur Windows**

.. code-block:: powershell

    # Autoriser l'exécution de scripts
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

**Base de données corrompue**

.. code-block:: bash

    # Réinitialiser la base de données
    rm oc-lettings-site.sqlite3
    python manage.py migrate
    python manage.py createsuperuser

Prochaines étapes
==================

- Consultez la documentation complète : :doc:`installation`
- Découvrez les fonctionnalités : :doc:`usage`
- Personnalisez votre déploiement : :doc:`deployment`