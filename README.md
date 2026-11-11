# Portfolio_Project - Naira Awadin

Portfolio développé avec **Python et Streamlit** pour présenter mon parcours, mes projets, mes expériences, etc, dans le cadre du cours Fundamental of Python.

## Fonctionnalités

- Présentation de mon profil et de mon parcours académique
- Présentation de mes projets et mes expériences pro et associatives
- Visualisation de mes compétences techniques
- Formulaire de contact

## Structure du projet

- `app.py` : point d'entrée et navigation des pages
- `data.py` : tout le contenu du site
- `utils.py` : fonctions de filtre et de tri des projets, validation du form de contact et enregistrement des messages
- `app_pages/` : une page par fichier (le dossier ne s'appelle pas `pages`, sinon Streamlit affiche brièvement son propre menu avant ma navigation)
- `assets/` : photo, cv et les differentes images des projets
- `.streamlit/config.toml` : thème (clair et sombre)

## Installation et lancement

### 1. Cloner le Repo

```bash
git clone [lien_du_repo]
cd Portfolio_Project
```

### 2. Créer et activer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate   #Linux/macOS
.venv\Scripts\activate  #windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l'app streamlit

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse suivante : http://localhost:8501

### 5. Quitter l'environnement virtuel

```bash
deactivate
```

## Technlogies utilisées

- Python
- Streamlit
- Pandas

## Liens
 
- Github : https://github.com/NairaAwadin/Portfolio_Project
- Portfolio en ligne : https://naira-awadin-portfolio.streamlit.app/
