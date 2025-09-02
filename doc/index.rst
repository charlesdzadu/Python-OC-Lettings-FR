.. OC Lettings Site documentation master file

==============================
OC Lettings Site Documentation
==============================

Bienvenue dans la documentation technique du site OC Lettings !

Description du projet
=====================

OC Lettings Site est une application web Django permettant de gérer des locations de vacances et des profils d'utilisateurs. Le site offre une interface moderne pour consulter les propriétés disponibles et les profils des utilisateurs.

.. toctree::
   :maxdepth: 2
   :caption: Sommaire:

   installation
   quickstart
   technologies
   database
   api
   usage
   deployment

Vue d'ensemble
==============

Le site est composé de trois applications principales :

* **oc_lettings_site** : Application principale contenant la page d'accueil
* **lettings** : Gestion des locations avec adresses
* **profiles** : Gestion des profils utilisateurs

Fonctionnalités principales
============================

* Consultation des locations disponibles
* Affichage détaillé de chaque location avec adresse complète
* Consultation des profils utilisateurs
* Interface d'administration Django
* Pages d'erreur personnalisées (404, 500)
* Logging et monitoring avec Sentry
* Tests automatisés avec couverture > 80%

Architecture technique
======================

L'application suit une architecture Django modulaire avec :

* Séparation des applications par domaine fonctionnel
* Configuration par variables d'environnement
* Déploiement containerisé avec Docker
* Pipeline CI/CD automatisé avec GitHub Actions
* Hébergement sur Render (ou autre service cloud)

Indices et tables
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`