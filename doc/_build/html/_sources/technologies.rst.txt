====================
Technologies utilisées
====================

Ce document présente l'ensemble des technologies et outils utilisés dans le projet OC Lettings Site.

Stack technique principale
==========================

Framework Backend
-----------------

**Django 4.2.16**
  Framework web Python de haut niveau qui encourage le développement rapide et une conception propre et pragmatique.

  - Architecture MVT (Model-View-Template)
  - ORM intégré pour la gestion de base de données
  - Système d'administration automatique
  - Gestion de la sécurité (CSRF, XSS, SQL Injection)
  - Système de routage d'URL flexible

**Python 3.11+**
  Langage de programmation principal du projet.

  - Typage dynamique
  - Gestion automatique de la mémoire
  - Large écosystème de bibliothèques
  - Support des environnements virtuels

Base de données
================

**SQLite3**
  Base de données relationnelle légère utilisée pour le développement et les tests.

  - Aucune configuration serveur requise
  - Base de données stockée dans un fichier unique
  - Support complet des transactions ACID
  - Parfait pour le développement et les petites applications

**Django ORM**
  Couche d'abstraction de base de données.

  - Migrations automatiques
  - Requêtes Python plutôt que SQL brut
  - Support de multiples backends de base de données
  - Protection contre les injections SQL

Serveur Web
===========

**Gunicorn 21.2.0**
  Serveur HTTP WSGI Python pour les déploiements en production.

  - Serveur multi-worker
  - Compatible avec Django
  - Gestion des processus robuste
  - Haute performance

**Whitenoise 6.5.0**
  Middleware pour servir les fichiers statiques directement depuis Django.

  - Compression automatique des fichiers statiques
  - En-têtes de cache optimaux
  - Intégration transparente avec Django
  - Idéal pour les déploiements sur PaaS

Outils de développement
========================

Tests et qualité du code
-------------------------

**Pytest 4.8.0**
  Framework de test Python moderne et puissant.

  - Syntaxe simple et expressive
  - Support des fixtures avancées
  - Tests paramétrés
  - Plugins extensibles

**Pytest-django 4.8.0**
  Plugin pytest pour tester les applications Django.

  - Intégration complète avec Django
  - Base de données de test automatique
  - Fixtures Django spécifiques
  - Client de test HTTP

**Pytest-cov 4.1.0**
  Plugin pour mesurer la couverture de code.

  - Rapports détaillés de couverture
  - Intégration avec pytest
  - Support des seuils minimums
  - Formats de sortie multiples

**Flake8 3.7.0**
  Outil de vérification de style et de qualité du code Python.

  - Vérification PEP 8
  - Détection des erreurs de syntaxe
  - Analyse de la complexité du code
  - Extensible via plugins

Configuration et environnement
-------------------------------

**Python-decouple 3.8**
  Bibliothèque pour séparer les paramètres de configuration du code.

  - Variables d'environnement
  - Fichiers .env
  - Typage des valeurs de configuration
  - Valeurs par défaut

Monitoring et debugging
========================

**Sentry-sdk 2.35.2**
  Plateforme de monitoring d'erreurs en temps réel.

  - Capture automatique des exceptions
  - Contexte détaillé des erreurs
  - Monitoring de performance
  - Alertes configurables
  - Intégration Django native

Documentation
=============

**Sphinx**
  Générateur de documentation Python.

  - Format reStructuredText
  - Génération HTML/PDF
  - Documentation du code automatique
  - Thèmes personnalisables

**sphinx-rtd-theme 2.0.0**
  Thème Read the Docs pour Sphinx.

  - Design responsive
  - Navigation intuitive
  - Recherche intégrée
  - Compatible mobile

Containerisation et déploiement
================================

**Docker**
  Plateforme de containerisation.

  - Environnements isolés
  - Reproductibilité garantie
  - Déploiement simplifié
  - Multi-stage builds

**Docker Compose**
  Outil pour définir et exécuter des applications Docker multi-conteneurs.

  - Configuration YAML simple
  - Orchestration locale
  - Réseaux automatiques
  - Volumes persistants

CI/CD et versioning
====================

**Git**
  Système de contrôle de version distribué.

  - Historique complet
  - Branches et merges
  - Collaboration d'équipe
  - Intégration GitHub

**GitHub Actions**
  Plateforme CI/CD intégrée à GitHub.

  - Workflows automatisés
  - Tests sur chaque push
  - Build et push Docker automatique
  - Déploiement continu
  - Matrices de tests

Hébergement
===========

**Render**
  Plateforme d'hébergement cloud moderne.

  - Déploiement automatique depuis GitHub
  - SSL/TLS gratuit
  - Scaling automatique
  - Variables d'environnement sécurisées
  - Logs en temps réel

Architecture et patterns
=========================

Patterns utilisés
-----------------

**MVT (Model-View-Template)**
  Pattern architectural de Django.

  - **Models** : Définition des données et logique métier
  - **Views** : Logique de traitement des requêtes
  - **Templates** : Présentation et rendu HTML

**DRY (Don't Repeat Yourself)**
  Principe de développement évitant la duplication de code.

**KISS (Keep It Simple, Stupid)**
  Principe favorisant la simplicité dans la conception.

Structure modulaire
-------------------

L'application est divisée en applications Django distinctes :

- **oc_lettings_site** : Application principale et configuration
- **lettings** : Gestion des locations
- **profiles** : Gestion des profils utilisateurs

Sécurité
========

Mesures de sécurité implémentées
---------------------------------

- Protection CSRF sur tous les formulaires
- Échappement automatique dans les templates
- Validation des données d'entrée
- Hashage sécurisé des mots de passe
- Variables sensibles dans les variables d'environnement
- Headers de sécurité via middleware
- SSL/TLS en production

Versions et compatibilité
==========================

Compatibilité testée
--------------------

- Python : 3.11, 3.12
- Systèmes d'exploitation : Linux, macOS, Windows
- Navigateurs : Chrome, Firefox, Safari, Edge (versions récentes)
- Docker : 20.10+
- Node.js : Non requis (pas de frontend JavaScript)

Dépendances et mises à jour
============================

Gestion des dépendances
-----------------------

Les dépendances sont gérées via :

- ``requirements.txt`` : Liste fixe des dépendances avec versions
- ``pip`` : Gestionnaire de paquets Python
- Mises à jour régulières pour la sécurité
- Tests de compatibilité avant mise à jour majeure

Pour mettre à jour les dépendances :

.. code-block:: bash

    pip install --upgrade -r requirements.txt