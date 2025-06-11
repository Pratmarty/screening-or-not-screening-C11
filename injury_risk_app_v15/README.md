
# 🩺 Application de Prédiction du Risque de Blessure Sportive

Cette application permet aux athlètes et aux professionnels du sport de :
- Saisir des données physiologiques et de performance
- Estimer le **risque de blessure** (faible, modéré, élevé)
- Identifier la **localisation probable** de la blessure
- Comprendre les **facteurs de risque**

## 🚀 Lancement local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Fichiers inclus

- `app.py` : l'application principale
- `requirements.txt` : dépendances Python
- `README.md` : documentation

## 📦 Déploiement

Déployez directement via [Streamlit Cloud](https://streamlit.io/cloud) en important ce dépôt GitHub.

## 📚 Basé sur la littérature

Les règles heuristiques sont basées sur :
- Données de performance (force, sprint, saut)
- Questionnaire de bien-être
- Études récentes sur les blessures non-contact (PDF fournis)

## ✨ Auteurs & Sources

Développé à partir d'articles scientifiques et retours terrain (rugby, basket, kinésithérapie sportive).
