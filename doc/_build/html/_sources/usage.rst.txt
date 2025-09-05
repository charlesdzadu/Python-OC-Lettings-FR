==================
Guide d'utilisation
==================

Ce guide détaille l'utilisation complète de l'application OC Lettings Site, tant pour les utilisateurs finaux que pour les administrateurs.

Navigation dans l'application
=============================

Page d'accueil
--------------

La page d'accueil est le point d'entrée principal de l'application.

**Accès** : http://localhost:8000/

**Fonctionnalités disponibles** :

- **Lettings** : Accès à la liste des locations
- **Profiles** : Accès à la liste des profils utilisateurs  
- **Admin** : Accès au panel d'administration (authentification requise)

Interface utilisateur
---------------------

L'interface est conçue pour être simple et intuitive :

.. code-block:: text

    ┌─────────────────────────────────────┐
    │        Holiday Homes                │
    │                                     │
    │   [Lettings]     [Profiles]        │
    │                                     │
    │   Welcome to Holiday Homes          │
    └─────────────────────────────────────┘

Module Lettings (Locations)
============================

Liste des locations
-------------------

**URL** : http://localhost:8000/lettings/

Cette page affiche toutes les locations disponibles sous forme de liste cliquable.

**Fonctionnalités** :

- Visualisation de toutes les locations
- Clic sur une location pour voir les détails
- Navigation vers la page d'accueil

**Exemple d'affichage** :

.. code-block:: text

    Lettings
    
    • Underground Hygge
    • Soutane, King
    • The Gingerbread House
    • A Dome on a Dome
    • Infinite Cubes

Détail d'une location
----------------------

**URL** : http://localhost:8000/lettings/<id>/

Affiche les informations complètes d'une location spécifique.

**Informations affichées** :

- Titre de la location
- Adresse complète :
  - Numéro et rue
  - Ville
  - État (code à 2 lettres)
  - Code postal
  - Code pays ISO

**Exemple** :

.. code-block:: text

    Underground Hygge
    
    Address:
    123 Main Street
    New York, NY 10001
    USA
    
    [Back to Lettings List]

Navigation dans les locations
------------------------------

1. Depuis la page d'accueil, cliquer sur "Lettings"
2. Parcourir la liste des locations disponibles
3. Cliquer sur une location pour voir ses détails
4. Utiliser "Back" pour revenir à la liste
5. Utiliser "Home" pour revenir à l'accueil

Module Profiles (Profils)
==========================

Liste des profils
-----------------

**URL** : http://localhost:8000/profiles/

Affiche tous les profils d'utilisateurs enregistrés.

**Fonctionnalités** :

- Liste de tous les utilisateurs
- Clic sur un profil pour voir les détails
- Navigation vers la page d'accueil

**Exemple d'affichage** :

.. code-block:: text

    Profiles
    
    • HeadlinesGazer
    • DavWin
    • AirWow
    • 4meRomance

Détail d'un profil
-------------------

**URL** : http://localhost:8000/profiles/<username>/

Affiche les informations du profil utilisateur.

**Informations affichées** :

- Nom d'utilisateur
- Prénom et nom (si renseignés)
- Email
- Ville favorite

**Exemple** :

.. code-block:: text

    Profile: HeadlinesGazer
    
    First name: Jamie
    Last name: Lal
    Email: jssssss33@acee9.live
    Favorite city: Buenos Aires
    
    [Back to Profiles List]

Panel d'administration
======================

Accès à l'administration
-------------------------

**URL** : http://localhost:8000/admin/

**Identifiants par défaut** :

- Username : ``admin``
- Password : ``Abc1234!``

**Première connexion** :

1. Naviguer vers /admin/
2. Entrer les identifiants
3. Cliquer sur "Log in"

Interface d'administration
---------------------------

Le panel d'administration Django offre une interface complète pour gérer les données.

**Sections disponibles** :

.. code-block:: text

    Django administration
    
    AUTHENTICATION AND AUTHORIZATION
    ├── Groups
    └── Users
    
    LETTINGS
    ├── Addresses
    └── Lettings
    
    PROFILES
    └── Profiles

Gestion des locations
---------------------

**Ajouter une location** :

1. Cliquer sur "Lettings" > "Add"
2. Remplir le formulaire :
   - Title : Nom de la location
   - Address : Sélectionner ou créer une adresse
3. Cliquer sur "Save"

**Créer une adresse** :

1. Cliquer sur "Addresses" > "Add"
2. Remplir tous les champs :
   - Number : Numéro de rue (max 9999)
   - Street : Nom de la rue
   - City : Ville
   - State : Code état (2 lettres)
   - Zip code : Code postal (max 99999)
   - Country ISO code : Code pays (3 lettres)
3. Cliquer sur "Save"

**Modifier une location** :

1. Dans la liste, cliquer sur la location
2. Modifier les champs souhaités
3. Cliquer sur "Save"

**Supprimer une location** :

1. Sélectionner la/les location(s)
2. Choisir "Delete selected lettings"
3. Confirmer la suppression

Gestion des profils
-------------------

**Créer un profil** :

1. D'abord créer un utilisateur dans "Users"
2. Puis aller dans "Profiles" > "Add"
3. Sélectionner l'utilisateur
4. Renseigner la ville favorite (optionnel)
5. Cliquer sur "Save"

**Modifier un profil** :

1. Cliquer sur le profil dans la liste
2. Modifier la ville favorite
3. Cliquer sur "Save"

**Gestion des utilisateurs** :

1. Aller dans "Users"
2. Créer/modifier/supprimer des utilisateurs
3. Gérer les permissions et groupes

Fonctionnalités avancées
-------------------------

**Recherche** :

- Utiliser la barre de recherche pour filtrer
- Recherche par titre, username, ville

**Filtres** :

- Filtrer par état (locations)
- Filtrer par ville favorite (profils)
- Filtrer par statut (utilisateurs)

**Actions en masse** :

1. Cocher plusieurs éléments
2. Sélectionner l'action dans le menu
3. Cliquer sur "Go"

**Export de données** :

- Les données peuvent être exportées via le shell Django
- Voir la section "Commandes de gestion"

Commandes de gestion
====================

Accès au shell Django
---------------------

.. code-block:: bash

    python manage.py shell

**Exemples d'utilisation** :

.. code-block:: python

    # Importer les modèles
    from lettings.models import Letting, Address
    from profiles.models import Profile
    from django.contrib.auth.models import User
    
    # Compter les objets
    Letting.objects.count()
    Profile.objects.count()
    
    # Lister les locations
    for letting in Letting.objects.all():
        print(f"{letting.title} - {letting.address.city}")
    
    # Rechercher un profil
    profile = Profile.objects.get(user__username="admin")
    print(profile.favorite_city)

Création de données via le shell
---------------------------------

**Créer une location complète** :

.. code-block:: python

    # Créer une adresse
    address = Address.objects.create(
        number=456,
        street="Python Street",
        city="Django City",
        state="DJ",
        zip_code=12345,
        country_iso_code="USA"
    )
    
    # Créer la location
    letting = Letting.objects.create(
        title="Django Paradise",
        address=address
    )
    
    print(f"Created: {letting.title} at {letting.address}")

**Créer un profil utilisateur** :

.. code-block:: python

    # Créer un utilisateur
    user = User.objects.create_user(
        username='johndoe',
        email='john@example.com',
        password='securepassword123',
        first_name='John',
        last_name='Doe'
    )
    
    # Créer le profil associé
    profile = Profile.objects.create(
        user=user,
        favorite_city='Paris'
    )
    
    print(f"Created profile for {user.username}")

Maintenance et nettoyage
-------------------------

**Nettoyer les sessions expirées** :

.. code-block:: bash

    python manage.py clearsessions

**Vérifier la base de données** :

.. code-block:: bash

    python manage.py dbshell
    .tables
    SELECT COUNT(*) FROM lettings_letting;
    .quit

**Réinitialiser les données de test** :

.. code-block:: bash

    # Sauvegarder d'abord
    python manage.py dumpdata > backup.json
    
    # Réinitialiser
    python manage.py flush
    python manage.py loaddata initial_data.json

Personnalisation
================

Modifier les styles
-------------------

Les fichiers CSS se trouvent dans ``static/`` :

.. code-block:: css

    /* static/style.css */
    body {
        font-family: Arial, sans-serif;
        background: #f0f0f0;
    }

Personnaliser les templates
----------------------------

Modifier les templates dans ``templates/`` :

.. code-block:: html

    <!-- templates/index.html -->
    {% extends "base.html" %}
    {% block content %}
        <h1>Bienvenue sur Holiday Homes</h1>
        <!-- Votre contenu personnalisé -->
    {% endblock %}

Ajouter des fonctionnalités
----------------------------

1. Créer une nouvelle vue dans ``views.py``
2. Ajouter l'URL dans ``urls.py``
3. Créer le template correspondant
4. Ajouter les tests

Bonnes pratiques d'utilisation
===============================

Sécurité
--------

1. **Changer le mot de passe admin** après l'installation
2. **Ne pas utiliser DEBUG=True** en production
3. **Utiliser HTTPS** pour les connexions sécurisées
4. **Limiter les accès admin** aux personnes autorisées
5. **Faire des sauvegardes régulières**

Performance
-----------

1. **Utiliser la pagination** pour les grandes listes
2. **Optimiser les requêtes** avec select_related()
3. **Activer le cache** pour les pages statiques
4. **Minimiser les fichiers statiques**

Maintenance
-----------

1. **Vérifier les logs** régulièrement
2. **Monitorer avec Sentry** les erreurs en production
3. **Mettre à jour** les dépendances de sécurité
4. **Tester** avant chaque déploiement
5. **Documenter** les modifications

Troubleshooting
===============

Problèmes courants
------------------

**Page 404 sur une location existante** :

- Vérifier l'ID dans l'URL
- Confirmer que la location existe en base
- Vérifier les logs d'erreur

**Impossible de se connecter à l'admin** :

.. code-block:: bash

    # Réinitialiser le mot de passe
    python manage.py changepassword admin

**Les styles ne s'affichent pas** :

.. code-block:: bash

    # Collecter les fichiers statiques
    python manage.py collectstatic

**Erreur 500** :

- Vérifier les logs dans la console
- Activer DEBUG temporairement
- Consulter Sentry si configuré

Support et aide
===============

Pour obtenir de l'aide :

1. Consulter la documentation technique
2. Vérifier les logs d'erreur
3. Utiliser le shell Django pour debugger
4. Contacter l'équipe de développement