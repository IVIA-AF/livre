# IVIA-AF: Initiative pour la Vulgarisation de l'Intelligence Artificielle en Afrique Francophone

## 📚 Jupyter Book 2 - Guide d'Apprentissage Automatique

Ce projet utilise **Jupyter Book 2** pour créer un livre interactif sur l'apprentissage automatique, déployé sur Vercel avec intégration GitHub Discussions pour les commentaires.

> **Important**: Jupyter Book 2 est construit sur la chaîne d'outils MyST. Par conséquent :
> - ✅ **`myst build`** est le point d'entrée unifié pour tous les builds
> - ❌ **`jupyter-book build`** est **DÉPRÉCIÉ** et ne doit pas être utilisé
> - Le système de build est maintenant agnostique du backend et plus extensible

## 🚀 Installation et Configuration

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation

```bash
# Cloner le repository
git clone https://github.com/IVIA-AF/livre.git
cd livre

# Installer les dépendances
pip install -r requirements.txt
```

## 🏗️ Construction du Livre

### Build Local

```bash
# Construire le livre HTML
myst build --html

# Les fichiers générés se trouvent dans _build/html/
```

### Nettoyer les Builds Précédents

```bash
# Nettoyer les builds précédents
myst clean

# Puis reconstruire
myst build --html
```

## 🧪 Tester Localement

### Option 1: Serveur HTTP Python (Recommandé)

```bash
# Construire le livre
myst build --html

# Naviguer vers le répertoire de build
cd _build/html

# Démarrer un serveur HTTP local
python -m http.server 8000

# Ouvrir dans votre navigateur
# http://localhost:8000
```

## 📦 Déploiement

### Déploiement sur Vercel

Le projet est configuré pour être déployé automatiquement sur Vercel :

```bash
# Build pour production
myst build --html

# Déployer sur Vercel
vercel
```

Le fichier `vercel.json` configure automatiquement le répertoire de sortie (`_build/html`).

## 💬 Commentaires et Discussions GitHub

Ce livre utilise **Giscus** pour intégrer les commentaires via GitHub Discussions. Chaque chapitre a son propre fil de discussion.

### Configuration GitHub

Avant de déployer, assurez-vous que :

1. ✅ **GitHub Discussions sont activées** dans les paramètres du repository
2. ✅ **La catégorie "Commentaire" existe** dans Discussions (ou mettez à jour le category-id dans `inject_giscus.py`)
3. ✅ **Le repository est public** (ou les utilisateurs ont accès si privé)
4. ✅ **L'application Giscus est autorisée** pour le repository

### Fonctionnalités

- 💬 **Commentaires par chapitre** : Chaque page/chapitre a son propre fil de discussion
- 🔐 **Authentification GitHub** : Les utilisateurs doivent être connectés à GitHub pour commenter
- 🎯 **Intégration workflow** : Les commentaires peuvent être liés à des Issues/PRs pour les améliorations
- 📊 **Réactions et engagement** : Support des réactions, markdown, et fonctionnalités GitHub

## 🔧 Conversion de Contenu

### Conversion LaTeX vers Markdown

Pour convertir des fichiers LaTeX en Markdown MyST :

```bash
# Conversion basique
pandoc -s tex/chapter1.tex -o content/chapter1.md

# Conversion avec support des citations et références croisées
pandoc tex/chapter1.tex \
  -f latex \
  -t commonmark_x+tex_math_dollars \
  --wrap=none \
  --citeproc \
  --metadata=link-citations=true \
  --bibliography=references.bib \
  --filter pandoc-crossref \
  -o content/chapter1.md
```

### Conversion de Notebooks Jupyter

```bash
# Convertir un notebook en Markdown
jupyter nbconvert --to markdown notebook.ipynb --output-dir './'
```

## 📝 Références et Citations

Jupyter Book 2 supporte les références MyST :

- `{numref}` - Affiche "Fig. 1" (recommandé pour les figures)
- `{ref}` - Affiche la légende complète
- `{cite}` - Pour les références bibliographiques

Exemple :
```markdown
Voir la figure {numref}`fig-label` pour plus de détails.
```

## 🛠️ Scripts Utilitaires

### Scripts de Build

- `build.sh` - Build pour Vercel avec injection de commentaires
- `build_production.sh` - Build de production
- `start_dev.sh` - Serveur de développement local
- `deploy.sh` - Build et déploiement sur GitHub

## 📚 Structure du Projet

```
livre/
├── content/           # Contenu du livre (chapitres)
│   ├── chapter1.md
│   ├── chapter2.md
│   └── images/       # Images du livre
├── intro.md          # Introduction
├── myst.yml          # Configuration Jupyter Book 2
├── parts/            # Parties réutilisables (footer, etc.)
├── plugins/          # Plugins MyST personnalisés
├── references.bib    # Bibliographie
└── _build/           # Fichiers générés (ne pas commiter)
```

## 🔍 Dépannage

### Problèmes Courants

1. **Erreur de build** : Nettoyez les builds précédents avec `myst clean`
2. **Commentaires ne s'affichent pas** : Vérifiez que GitHub Discussions sont activées
3. **Images manquantes** : Vérifiez les chemins relatifs dans les fichiers Markdown

## 📖 Ressources

- [Documentation Jupyter Book 2](https://jupyterbook.org/)
- [Guide MyST Markdown](https://mystmd.org/guide)
- [Giscus Documentation](https://giscus.app/)

## 📄 Licence

Voir le fichier `LICENSE` pour plus d'informations.
