# IVIA-AF: Initiative pour la Vulgarisation de l'Intelligence Artificielle en Afrique Francophone

## 🚀 Déploiement sur Vercel avec Analytics Simple

Ce projet est maintenant configuré pour être déployé sur Vercel avec un système d'analytics simple pour suivre les consultations du livre.

### Installation rapide

```bash
# Installation des dépendances
pip install -r requirements.txt

# Build local
d2lbook build html

# Déploiement sur Vercel
vercel
```

### Analytics et Statistiques

Le système d'analytics simple vous permet de :
- 📊 Suivre les pages visitées
- 🌍 Voir d'où viennent les visiteurs (référents)
- 🔗 Tracker les clics sur les liens externes
- 📈 Utiliser Vercel Analytics intégré

Les données sont disponibles dans le dashboard Vercel ou via Google Analytics.

### Configuration requise

- pip install git+https://github.com/d2l-ai/d2l-book
- conda install pandoc librsvg
- sudo apt-get install texlive-full

d2lbook build html

<!-- Let’s clear and build again. -->

d2lbook build pdf

rm -rf \_build && d2lbook build pdf

rm -rf \_build && d2lbook build html && d2lbook build pdf

rm -rf \_build && d2lbook build html && d2lbook build pdf && d2lbook deploy html pdf

rm -rf dist && d2lbook build html && d2lbook build pdf && d2lbook deploy html pdf

d2lbook deploy html pdf

## convert latex to md
```bash 
pandoc -s ch1.tex -o ch1.md
```

## Notebook to .md

```bash 
jupyter nbconvert --to markdown prise_en_main_python.ipynb --output-dir './'
```

```bash
•	é → \'e
•	à → \a`
•	è → \e`
•	ç → \c{c}
```


<!-- find dist/html -name "*.html" -exec sed -i '' '/<script src="_static\/sphinx_materialdesign_theme.js/a\
    <!-- Vercel Analytics -->\
    <script defer src="https://va.vercel-scripts.com/v1/script.js"></script>\
    <script src="_static/analytics.js"></script>' {} \; -->