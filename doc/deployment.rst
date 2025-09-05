========================
Procédures de déploiement
========================

Ce document détaille les procédures complètes de déploiement de l'application OC Lettings Site, incluant le pipeline CI/CD, la containerisation Docker et le déploiement sur différentes plateformes.

Vue d'ensemble du déploiement
==============================

Architecture de déploiement
---------------------------

.. code-block:: text

    GitHub Repository
           │
           ├──[push]──> GitHub Actions CI/CD
           │                    │
           │                    ├── Tests & Linting
           │                    ├── Build Docker Image
           │                    ├── Push to Docker Hub
           │                    └── Deploy to Render
           │
           └──[webhook]──> Render Auto-Deploy

Flux de déploiement
-------------------

1. **Développement** : Code sur branche feature
2. **Tests** : Pipeline CI sur chaque push
3. **Build** : Construction image Docker (master/main)
4. **Registry** : Push vers Docker Hub
5. **Déploiement** : Déclenchement automatique sur Render
6. **Monitoring** : Suivi avec Sentry

Pipeline CI/CD avec GitHub Actions
===================================

Configuration du workflow
-------------------------

Le pipeline est défini dans ``.github/workflows/ci-cd.yml`` :

**Déclencheurs** :

- Push sur branches : master, main, develop
- Pull requests vers : master, main

**Jobs du pipeline** :

1. **test** : Tests et linting
2. **docker** : Build et push Docker (master/main uniquement)
3. **deploy** : Déploiement production (master/main uniquement)

Configuration des secrets GitHub
---------------------------------

Dans Settings > Secrets and variables > Actions :

.. list-table:: Secrets requis
   :header-rows: 1
   :widths: 30 70

   * - Secret
     - Description
   * - DOCKER_USERNAME
     - Nom d'utilisateur Docker Hub
   * - DOCKER_TOKEN
     - Token d'accès Docker Hub
   * - RENDER_SERVICE_ID
     - ID du service Render
   * - RENDER_API_KEY
     - Clé API Render

**Créer un token Docker Hub** :

1. Aller sur https://hub.docker.com/settings/security
2. Cliquer sur "New Access Token"
3. Donner un nom descriptif
4. Copier le token généré

Étapes du pipeline
------------------

**1. Tests et Linting** :

.. code-block:: yaml

    - name: Run Flake8
      run: flake8 --exclude=venv,migrations
    
    - name: Run tests with coverage
      run: pytest --cov=. --cov-report=term-missing --cov-fail-under=80

**2. Build Docker** :

.. code-block:: yaml

    - name: Build and push Docker image
      uses: docker/build-push-action@v5
      with:
        tags: ${{ secrets.DOCKER_USERNAME }}/oc-lettings-site:latest

**3. Déploiement** :

.. code-block:: yaml

    - name: Deploy to hosting service
      uses: JorgeLNJunior/render-deploy@v1.4.5
      with:
        service_id: ${{ secrets.RENDER_SERVICE_ID }}
        api_key: ${{ secrets.RENDER_API_KEY }}

Containerisation avec Docker
=============================

Dockerfile
----------

Structure du Dockerfile multi-stage :

.. code-block:: dockerfile

    # Stage 1: Builder
    FROM python:3.11-slim as builder
    
    WORKDIR /app
    
    # Installer les dépendances système
    RUN apt-get update && apt-get install -y \
        gcc \
        && rm -rf /var/lib/apt/lists/*
    
    # Copier et installer les dépendances Python
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Stage 2: Runtime
    FROM python:3.11-slim
    
    WORKDIR /app
    
    # Copier les dépendances installées
    COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
    
    # Copier l'application
    COPY . .
    
    # Collecter les fichiers statiques
    RUN python manage.py collectstatic --noinput
    
    # Exposer le port
    EXPOSE 8000
    
    # Commande de démarrage
    CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]

Docker Compose
--------------

Configuration pour le développement local :

.. code-block:: yaml

    version: '3.8'
    
    services:
      web:
        build: .
        ports:
          - "8000:8000"
        environment:
          - DEBUG=True
          - SECRET_KEY=dev-secret-key
          - ALLOWED_HOSTS=localhost,127.0.0.1
        volumes:
          - .:/app
          - static_volume:/app/staticfiles
        command: python manage.py runserver 0.0.0.0:8000
    
    volumes:
      static_volume:

Commandes Docker
----------------

**Build local** :

.. code-block:: bash

    docker build -t oc-lettings-site .

**Run local** :

.. code-block:: bash

    docker run -p 8000:8000 \
      -e SECRET_KEY=your-secret-key \
      -e DEBUG=False \
      -e ALLOWED_HOSTS=localhost \
      oc-lettings-site

**Docker Compose** :

.. code-block:: bash

    # Développement
    docker-compose up
    
    # Production
    docker-compose -f docker-compose.prod.yml up -d

**Push vers Docker Hub** :

.. code-block:: bash

    docker tag oc-lettings-site username/oc-lettings-site:latest
    docker push username/oc-lettings-site:latest

Configuration de l'environnement
=================================

Variables d'environnement
-------------------------

Créer un fichier ``.env`` basé sur ``.env.example`` :

.. code-block:: bash

    # Django settings
    SECRET_KEY=your-secret-key-here
    DEBUG=False
    ALLOWED_HOSTS=your-domain.com,www.your-domain.com
    
    # Database (optionnel pour PostgreSQL)
    DATABASE_URL=postgresql://user:password@host:5432/dbname
    
    # Sentry monitoring (optionnel)
    SENTRY_DSN=https://xxx@yyy.ingest.sentry.io/zzz
    
    # Static files
    STATIC_ROOT=/app/staticfiles
    STATIC_URL=/static/

**Générer une SECRET_KEY sécurisée** :

.. code-block:: python

    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())

Settings de production
----------------------

Modifications dans ``settings.py`` :

.. code-block:: python

    import os
    from decouple import config
    
    # Security
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', default=False, cast=bool)
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
    
    # HTTPS
    if not DEBUG:
        SECURE_SSL_REDIRECT = True
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True
        SECURE_BROWSER_XSS_FILTER = True
        SECURE_CONTENT_TYPE_NOSNIFF = True
        X_FRAME_OPTIONS = 'DENY'

Déploiement sur Render
======================

Configuration initiale
----------------------

1. **Créer un compte** sur https://render.com
2. **Connecter GitHub** : Dashboard > New > Web Service
3. **Sélectionner le repository**
4. **Configurer le service** :

   - **Name** : oc-lettings-site
   - **Region** : Frankfurt (EU) ou Oregon (US)
   - **Branch** : master
   - **Runtime** : Docker
   - **Instance Type** : Free ou Starter

Configuration des variables
----------------------------

Dans Render Dashboard > Environment :

.. code-block:: text

    SECRET_KEY = [generated-secret-key]
    DEBUG = False
    ALLOWED_HOSTS = oc-lettings-site.onrender.com
    SENTRY_DSN = [your-sentry-dsn]
    PYTHON_VERSION = 3.11

render.yaml
-----------

Configuration Infrastructure as Code :

.. code-block:: yaml

    services:
      - type: web
        name: oc-lettings-site
        runtime: docker
        repo: https://github.com/username/Python-OC-Lettings-FR
        branch: master
        healthCheckPath: /
        envVars:
          - key: SECRET_KEY
            generateValue: true
          - key: ALLOWED_HOSTS
            value: oc-lettings-site.onrender.com
          - key: DEBUG
            value: false
        autoDeploy: true

Déploiement manuel
------------------

.. code-block:: bash

    # Via Render CLI
    render deploy --service-id srv-xxx
    
    # Via webhook
    curl -X POST https://api.render.com/deploy/srv-xxx?key=your-api-key

Déploiement sur d'autres plateformes
=====================================

Heroku
------

**Procfile** :

.. code-block:: text

    web: gunicorn oc_lettings_site.wsgi:application

**Déploiement** :

.. code-block:: bash

    heroku create oc-lettings-site
    heroku config:set SECRET_KEY=xxx
    git push heroku master

AWS Elastic Beanstalk
----------------------

**.ebextensions/django.config** :

.. code-block:: yaml

    option_settings:
      aws:elasticbeanstalk:container:python:
        WSGIPath: oc_lettings_site.wsgi:application

**Déploiement** :

.. code-block:: bash

    eb init -p python-3.11 oc-lettings-site
    eb create oc-lettings-env
    eb deploy

DigitalOcean App Platform
--------------------------

**app.yaml** :

.. code-block:: yaml

    name: oc-lettings-site
    services:
    - name: web
      dockerfile_path: Dockerfile
      source_dir: /
      http_port: 8000

Monitoring avec Sentry
======================

Configuration Sentry
--------------------

1. **Créer un projet** sur https://sentry.io
2. **Choisir Django** comme plateforme
3. **Copier le DSN**

**Integration dans settings.py** :

.. code-block:: python

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
    
    if not DEBUG and config('SENTRY_DSN', default=''):
        sentry_sdk.init(
            dsn=config('SENTRY_DSN'),
            integrations=[DjangoIntegration()],
            traces_sample_rate=0.1,
            send_default_pii=False,
            environment='production'
        )

Test de Sentry
--------------

.. code-block:: python

    # views.py
    def trigger_error(request):
        """Vue de test pour Sentry"""
        division_by_zero = 1 / 0
        return None

Alertes et notifications
-------------------------

Dans Sentry Dashboard :

1. Alerts > Create Alert Rule
2. Configurer les conditions
3. Ajouter les destinations (email, Slack, etc.)

Rollback et récupération
=========================

Stratégie de rollback
----------------------

**1. Via Git** :

.. code-block:: bash

    # Identifier le commit stable
    git log --oneline
    
    # Rollback
    git revert HEAD
    git push origin master

**2. Via Docker** :

.. code-block:: bash

    # Utiliser une version précédente
    docker pull username/oc-lettings-site:v1.0.0
    docker run username/oc-lettings-site:v1.0.0

**3. Via Render** :

- Dashboard > Settings > Rollback
- Sélectionner un déploiement précédent

Backup et restauration
-----------------------

**Backup de la base de données** :

.. code-block:: bash

    # Backup
    python manage.py dumpdata > backup_$(date +%Y%m%d).json
    
    # Upload vers S3 ou autre
    aws s3 cp backup_*.json s3://bucket-name/backups/

**Restauration** :

.. code-block:: bash

    # Télécharger le backup
    aws s3 cp s3://bucket-name/backups/backup_20240101.json .
    
    # Restaurer
    python manage.py flush --noinput
    python manage.py loaddata backup_20240101.json

Checklist de déploiement
=========================

Avant le déploiement
--------------------

- [ ] Tests passent localement
- [ ] Coverage > 80%
- [ ] Linting sans erreurs
- [ ] Variables d'environnement configurées
- [ ] SECRET_KEY unique générée
- [ ] DEBUG=False en production
- [ ] ALLOWED_HOSTS configuré
- [ ] Base de données migrée

Pendant le déploiement
-----------------------

- [ ] Pipeline CI/CD vert
- [ ] Image Docker construite
- [ ] Image pushée vers registry
- [ ] Déploiement déclenché
- [ ] Health check passé

Après le déploiement
--------------------

- [ ] Site accessible
- [ ] Toutes les pages fonctionnent
- [ ] Admin accessible
- [ ] Sentry connecté
- [ ] Logs vérifiés
- [ ] Performance acceptable
- [ ] SSL/HTTPS actif
- [ ] Monitoring configuré

Commandes utiles
================

Déploiement rapide
------------------

.. code-block:: bash

    # Script de déploiement complet
    #!/bin/bash
    
    # Tests
    pytest
    flake8
    
    # Git
    git add .
    git commit -m "Deploy: $(date +%Y-%m-%d)"
    git push origin master
    
    # Attendre le déploiement
    echo "Deployment triggered, check GitHub Actions..."

Vérification de santé
---------------------

.. code-block:: bash

    # Check local
    curl http://localhost:8000/
    
    # Check production
    curl https://oc-lettings-site.onrender.com/
    
    # Check avec timing
    curl -w "@curl-format.txt" -o /dev/null -s https://oc-lettings-site.onrender.com/

Logs et debugging
-----------------

.. code-block:: bash

    # Logs Docker local
    docker logs container_id
    
    # Logs Render
    render logs --service srv-xxx --tail
    
    # Logs avec filtrage
    docker logs container_id 2>&1 | grep ERROR

Optimisations de production
============================

Performance
-----------

1. **Caching** : Configurer Redis/Memcached
2. **CDN** : Utiliser CloudFlare pour les assets
3. **Compression** : Activer gzip dans nginx
4. **Database pooling** : Utiliser pgbouncer pour PostgreSQL

Sécurité
--------

1. **WAF** : Web Application Firewall
2. **Rate limiting** : Limiter les requêtes
3. **Backup automatique** : Scripts cron
4. **Audit logs** : Traçabilité complète
5. **Secrets rotation** : Renouvellement régulier