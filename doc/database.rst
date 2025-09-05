==============================
Structure de la base de données
==============================

Ce document décrit la structure complète de la base de données de l'application OC Lettings Site.

Vue d'ensemble
==============

L'application utilise SQLite3 comme système de gestion de base de données avec l'ORM Django pour l'abstraction. La base de données est organisée autour de trois entités principales : les adresses, les locations et les profils d'utilisateurs.

Schéma de la base de données
============================

Diagramme des relations
------------------------

::

    ┌─────────────────┐
    │      User       │
    │   (Django)      │
    └────────┬────────┘
             │ OneToOne
             ▼
    ┌─────────────────┐
    │     Profile     │
    ├─────────────────┤
    │ + user          │
    │ + favorite_city │
    └─────────────────┘

    ┌─────────────────┐
    │     Address     │
    ├─────────────────┤
    │ + number        │
    │ + street        │
    │ + city          │
    │ + state         │
    │ + zip_code      │
    │ + country_iso   │
    └────────┬────────┘
             │ OneToOne
             ▼
    ┌─────────────────┐
    │    Letting      │
    ├─────────────────┤
    │ + title         │
    │ + address       │
    └─────────────────┘

Modèles de données
==================

Model Address
-------------

**Table** : ``lettings_address``

.. list-table:: Structure de la table Address
   :header-rows: 1
   :widths: 20 20 20 40

   * - Champ
     - Type
     - Contraintes
     - Description
   * - id
     - INTEGER
     - PRIMARY KEY, AUTO INCREMENT
     - Identifiant unique
   * - number
     - INTEGER
     - NOT NULL, MAX 9999
     - Numéro de rue
   * - street
     - VARCHAR(64)
     - NOT NULL
     - Nom de la rue
   * - city
     - VARCHAR(64)
     - NOT NULL
     - Ville
   * - state
     - VARCHAR(2)
     - NOT NULL, LENGTH=2
     - Code état (US)
   * - zip_code
     - INTEGER
     - NOT NULL, MAX 99999
     - Code postal
   * - country_iso_code
     - VARCHAR(3)
     - NOT NULL, LENGTH=3
     - Code pays ISO

**Validations** :

- ``number`` : Doit être positif et <= 9999
- ``state`` : Exactement 2 caractères
- ``zip_code`` : Doit être positif et <= 99999
- ``country_iso_code`` : Exactement 3 caractères

Model Letting
-------------

**Table** : ``lettings_letting``

.. list-table:: Structure de la table Letting
   :header-rows: 1
   :widths: 20 20 20 40

   * - Champ
     - Type
     - Contraintes
     - Description
   * - id
     - INTEGER
     - PRIMARY KEY, AUTO INCREMENT
     - Identifiant unique
   * - title
     - VARCHAR(256)
     - NOT NULL
     - Titre de la location
   * - address_id
     - INTEGER
     - FOREIGN KEY, UNIQUE, ON DELETE CASCADE
     - Référence vers Address

**Relations** :

- OneToOne avec ``Address`` (cascade on delete)

Model Profile
-------------

**Table** : ``profiles_profile``

.. list-table:: Structure de la table Profile
   :header-rows: 1
   :widths: 20 20 20 40

   * - Champ
     - Type
     - Contraintes
     - Description
   * - id
     - INTEGER
     - PRIMARY KEY, AUTO INCREMENT
     - Identifiant unique
   * - user_id
     - INTEGER
     - FOREIGN KEY, UNIQUE, ON DELETE CASCADE
     - Référence vers User
   * - favorite_city
     - VARCHAR(64)
     - NULLABLE
     - Ville favorite

**Relations** :

- OneToOne avec ``User`` (modèle Django auth)

Tables Django par défaut
========================

L'application utilise également les tables Django standard :

Tables d'authentification
--------------------------

- ``auth_user`` : Utilisateurs du système
- ``auth_group`` : Groupes d'utilisateurs
- ``auth_permission`` : Permissions
- ``auth_user_groups`` : Association user-group
- ``auth_user_user_permissions`` : Permissions par utilisateur

Tables système
--------------

- ``django_migrations`` : Historique des migrations
- ``django_session`` : Sessions utilisateurs
- ``django_content_type`` : Types de contenu
- ``django_admin_log`` : Logs d'administration

Commandes de gestion de la base de données
===========================================

Accès à la base de données
---------------------------

**Via SQLite3 CLI** :

.. code-block:: bash

    sqlite3 oc-lettings-site.sqlite3
    .tables  # Liste les tables
    .schema lettings_letting  # Structure d'une table
    .quit  # Quitter

**Via Django shell** :

.. code-block:: bash

    python manage.py shell
    
    # Importer les modèles
    from lettings.models import Letting, Address
    from profiles.models import Profile
    
    # Requêtes
    Letting.objects.all()
    Address.objects.filter(city="Paris")
    Profile.objects.get(user__username="admin")

Migrations
----------

**Créer une migration** :

.. code-block:: bash

    python manage.py makemigrations [app_name]

**Appliquer les migrations** :

.. code-block:: bash

    python manage.py migrate

**Voir l'état des migrations** :

.. code-block:: bash

    python manage.py showmigrations

**Annuler une migration** :

.. code-block:: bash

    python manage.py migrate app_name migration_number

Gestion des données
--------------------

**Exporter les données** :

.. code-block:: bash

    python manage.py dumpdata > backup.json
    python manage.py dumpdata lettings.Letting > lettings.json

**Importer les données** :

.. code-block:: bash

    python manage.py loaddata backup.json

**Réinitialiser la base** :

.. code-block:: bash

    rm oc-lettings-site.sqlite3
    python manage.py migrate
    python manage.py createsuperuser

Requêtes ORM courantes
=======================

Exemples pour Letting
----------------------

.. code-block:: python

    from lettings.models import Letting, Address
    
    # Créer une location
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="New York",
        state="NY",
        zip_code=10001,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(
        title="Beautiful Apartment",
        address=address
    )
    
    # Récupérer toutes les locations
    all_lettings = Letting.objects.all()
    
    # Filtrer par ville
    ny_lettings = Letting.objects.filter(address__city="New York")
    
    # Récupérer avec l'adresse (évite les requêtes N+1)
    lettings = Letting.objects.select_related('address').all()

Exemples pour Profile
----------------------

.. code-block:: python

    from profiles.models import Profile
    from django.contrib.auth.models import User
    
    # Créer un profil
    user = User.objects.create_user('john', 'john@example.com', 'password')
    profile = Profile.objects.create(
        user=user,
        favorite_city="Paris"
    )
    
    # Récupérer tous les profils
    all_profiles = Profile.objects.all()
    
    # Filtrer par ville favorite
    paris_lovers = Profile.objects.filter(favorite_city="Paris")
    
    # Récupérer avec l'utilisateur
    profiles = Profile.objects.select_related('user').all()

Optimisation des performances
==============================

Index
-----

Les index sont automatiquement créés sur :

- Les clés primaires (id)
- Les clés étrangères
- Les champs unique

Pour ajouter des index personnalisés :

.. code-block:: python

    class Meta:
        indexes = [
            models.Index(fields=['city']),
        ]

Requêtes optimisées
-------------------

**Éviter les requêtes N+1** :

.. code-block:: python

    # Mauvais
    for letting in Letting.objects.all():
        print(letting.address.city)  # Une requête par letting
    
    # Bon
    for letting in Letting.objects.select_related('address'):
        print(letting.address.city)  # Une seule requête

**Utiliser only() et defer()** :

.. code-block:: python

    # Récupérer seulement certains champs
    Letting.objects.only('title')
    
    # Exclure certains champs
    Profile.objects.defer('favorite_city')

Sauvegarde et restauration
===========================

Sauvegarde complète
-------------------

.. code-block:: bash

    # Sauvegarde JSON
    python manage.py dumpdata --indent 2 > backup_$(date +%Y%m%d).json
    
    # Sauvegarde SQLite
    cp oc-lettings-site.sqlite3 backup_$(date +%Y%m%d).sqlite3

Restauration
------------

.. code-block:: bash

    # Depuis JSON
    python manage.py flush --noinput
    python manage.py loaddata backup_20240101.json
    
    # Depuis SQLite
    cp backup_20240101.sqlite3 oc-lettings-site.sqlite3

Considérations pour la production
==================================

Migration vers PostgreSQL
--------------------------

Pour un déploiement en production, considérer PostgreSQL :

.. code-block:: python

    # settings.py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'oc_lettings',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

Sécurité
--------

- Utiliser des variables d'environnement pour les credentials
- Activer SSL pour les connexions à la base
- Implémenter des sauvegardes régulières
- Limiter les permissions des utilisateurs de base de données
- Utiliser des connexions poolées en production