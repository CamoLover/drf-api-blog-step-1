# API Django - Gestion des Concessionnaires et Véhicules

**Fait par Evan Escabasse**

---

## Description du projet

Cette API Django REST Framework permet de gérer des concessionnaires automobiles et leurs véhicules. Elle implémente un système d'authentification JWT et expose des endpoints sécurisés pour consulter les données.

### Fonctionnalités principales

- **Gestion des concessionnaires** (nom visible, siret protégé)
- **Gestion des véhicules** (type, marque, puissance, prix)
- **Authentification JWT** (création utilisateur, tokens)
- **API RESTful** sécurisée
- **Admin Django** configuré
- **Validation des données** (SIRET obligatoire 14 caractères)

---

## Modèles de données

### Concessionnaire
- `nom` : CharField (64 caractères max)
- `siret` : CharField (exactement 14 caractères, **non exposé via API**)

### Véhicule
- `type` : CharField (choix: "moto" ou "auto")
- `marque` : CharField (64 caractères max)
- `chevaux` : IntegerField
- `prix_ht` : FloatField
- `concessionnaire` : ForeignKey vers Concessionnaire

---

## Installation et démarrage

### 1. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 2. Migrations de base de données
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Créer un superutilisateur (optionnel)
```bash
python manage.py createsuperuser
```

### 4. Démarrer le serveur
```bash
python manage.py runserver
```

Le serveur sera accessible sur : `http://localhost:8000`

---

## Routes API disponibles

### **Authentification**

#### **POST** `/api/users/`
**Description :** Créer un nouvel utilisateur
**Auth :** Aucune

**Corps de la requête :**
```json
{
  "username": "nom_utilisateur",
  "password": "mot_de_passe"
}
```

**Réponse (201) :**
```json
{
  "id": 1,
  "username": "nom_utilisateur"
}
```

---

#### **POST** `/api/token/`
**Description :** Obtenir un token JWT d'accès
**Auth :** Aucune

**Corps de la requête :**
```json
{
  "username": "nom_utilisateur", 
  "password": "mot_de_passe"
}
```

**Réponse (200) :**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

#### **POST** `/api/refresh_token/`
**Description :** Rafraîchir le token d'accès
**Auth :** Aucune

**Corps de la requête :**
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Réponse (200) :**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

### **Concessionnaires**

#### **GET** `/api/concessionnaires/`
**Description :** Liste de tous les concessionnaires
**Auth :** Bearer Token requis

**Headers :**
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Réponse (200) :**
```json
[
  {
    "id": 1,
    "nom": "AutoMax Paris"
  },
  {
    "id": 2,
    "nom": "Moto Expert Lyon"
  }
]
```

**Note :** Le champ `siret` n'est **jamais** exposé via l'API.

---

#### **GET** `/api/concessionnaires/{id}/`
**Description :** Détails d'un concessionnaire spécifique
**Auth :** Bearer Token requis

**Paramètres d'URL :**
- `id` : ID du concessionnaire (entier)

**Réponse (200) :**
```json
{
  "id": 1,
  "nom": "AutoMax Paris"
}
```

**Réponse (404) :** Concessionnaire inexistant

---

### **Véhicules**

#### **GET** `/api/concessionnaires/{concessionnaire_id}/vehicules/`
**Description :** Liste des véhicules d'un concessionnaire
**Auth :** Bearer Token requis

**Paramètres d'URL :**
- `concessionnaire_id` : ID du concessionnaire (entier)

**Réponse (200) :**
```json
[
  {
    "id": 1,
    "type": "auto",
    "marque": "BMW",
    "chevaux": 150,
    "prix_ht": 25000.0,
    "concessionnaire": 1
  },
  {
    "id": 2,
    "type": "auto", 
    "marque": "Audi",
    "chevaux": 180,
    "prix_ht": 32000.0,
    "concessionnaire": 1
  }
]
```

---

#### **GET** `/api/concessionnaires/{concessionnaire_id}/vehicules/{vehicule_id}/`
**Description :** Détails d'un véhicule spécifique
**Auth :** Bearer Token requis

**Paramètres d'URL :**
- `concessionnaire_id` : ID du concessionnaire (entier)
- `vehicule_id` : ID du véhicule (entier)

**Réponse (200) :**
```json
{
  "id": 1,
  "type": "auto",
  "marque": "BMW", 
  "chevaux": 150,
  "prix_ht": 25000.0,
  "concessionnaire": 1
}
```

**Réponse (404) :** Concessionnaire ou véhicule inexistant

---

## Sécurité et Authentification

### Token JWT
- **Durée de vie access token :** 60 minutes
- **Durée de vie refresh token :** 7 jours
- **Rotation des tokens :** Activée

### Permissions
- **Endpoints publics :** `/api/users/`, `/api/token/`, `/api/refresh_token/`
- **Endpoints protégés :** Tous les autres (Bearer Token requis)

### Données sensibles
- Le champ **`siret`** des concessionnaires n'est **jamais exposé** via l'API
- Il reste accessible uniquement via l'admin Django

---

## Administration

### Interface d'administration
Accès : `http://localhost:8000/admin/`

**Fonctionnalités :**
- Gestion complète des concessionnaires (avec siret)
- Gestion des véhicules
- Interface optimisée (filtres, recherche)

---

## Tests avec Bruno

Une collection complète de tests Bruno est disponible dans le dossier `bruno_collection/`.

### Import de la collection
1. Ouvrir Bruno
2. "Open Collection" → Sélectionner `bruno_collection/`
3. Exécuter les requêtes dans l'ordre

**Guide complet :** Voir `BRUNO_GUIDE.md`

---

## Données de test

La base SQLite est fournie avec des données de test :

### Utilisateurs existants
- `userA` (mot de passe **admin123**)
- `userB` (mot de passe **test456**)

### Concessionnaires et véhicules
- **AutoMax Paris** avec BMW et Audi
- **Moto Expert Lyon** avec Yamaha

---

## Codes de réponse HTTP

| Code | Description |
|------|-------------|
| 200  | Succès |
| 201  | Créé avec succès |
| 400  | Erreur de validation |
| 401  | Non authentifié |
| 404  | Ressource non trouvée |

---

## Spécifications respectées

- **Modèles** : Concessionnaire + Véhicule avec validation  
- **Serializers** : SIRET exclu, véhicules complets  
- **Endpoints obligatoires** : 4/4 implémentés  
- **Endpoints bonus** : 3/3 implémentés  
- **Sécurité JWT** : Authentification complète  
- **Migrations** : Base de données structurée  

**Projet conforme à 100% aux spécifications techniques.**