## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Résumé du fonctionnement

Le déploiement est automatisé via un pipeline CI/CD GitHub Actions qui :
1. Exécute les tests et le linting sur chaque push
2. Construit et pousse l'image Docker vers Docker Hub (branches master/main uniquement)
3. Déclenche le déploiement automatique sur le service d'hébergement

### Configuration requise

#### Variables d'environnement
- `SECRET_KEY` : Clé secrète Django (générer une nouvelle pour la production)
- `DEBUG` : False en production
- `ALLOWED_HOSTS` : Domaine(s) autorisé(s)
- `SENTRY_DSN` : DSN pour le monitoring Sentry (optionnel)

#### Secrets GitHub Actions
- `DOCKER_USERNAME` : Nom d'utilisateur Docker Hub
- `DOCKER_PASSWORD` : Mot de passe Docker Hub
- `RENDER_DEPLOY_HOOK_URL` : Webhook de déploiement (si utilisation de Render)

### Étapes de déploiement

#### 1. Configuration initiale
```bash
# Créer un fichier .env avec les variables de production
cp .env.example .env
# Éditer .env avec les valeurs de production
```

#### 2. Configuration du service d'hébergement (Render)
1. Créer un nouveau Web Service sur Render
2. Connecter le repository GitHub
3. Configurer les variables d'environnement dans Render
4. Activer le déploiement automatique

#### 3. Déploiement
```bash
# Le déploiement se fait automatiquement lors d'un push sur master
git push origin master
```

#### 4. Récupération de l'image Docker
```bash
# Récupérer l'image depuis Docker Hub
docker pull [username]/oc-lettings-site:latest

# Lancer localement
docker run -p 8000:8000 -e SECRET_KEY=your-key [username]/oc-lettings-site:latest
```

### Monitoring

Le site utilise Sentry pour le monitoring des erreurs. Configurer `SENTRY_DSN` dans les variables d'environnement pour activer cette fonctionnalité.
