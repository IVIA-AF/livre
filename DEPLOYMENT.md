# Guide de déploiement sur Vercel avec Analytics

Ce guide vous explique comment déployer le livre IVIA-AF sur Vercel avec Vercel Analytics intégré.

## Prérequis

1. Un compte Vercel (gratuit)
2. Un repository GitHub avec votre code

## Déploiement

1. Connectez votre repository GitHub à Vercel
2. Vercel détectera automatiquement la configuration `vercel.json`
3. Le build se fera automatiquement avec la commande : `pip install -r requirements.txt && d2lbook build html`

## Analytics

Le projet utilise **Vercel Analytics** intégré, qui est :
- ✅ **Automatique** - Pas de configuration supplémentaire
- ✅ **Gratuit** - Inclus avec Vercel
- ✅ **Privé** - Respecte la vie privée des utilisateurs
- ✅ **Simple** - Données disponibles dans le dashboard Vercel

### Activation

1. Dans votre projet Vercel, allez dans **Settings** → **Analytics**
2. Activez **Vercel Analytics**
3. C'est tout ! Les données commencent à être collectées automatiquement

### Données collectées

- **Pages visitées** - Quelles pages sont les plus populaires
- **Sources de trafic** - D'où viennent vos visiteurs
- **Clics sur liens externes** - Quels liens externes sont cliqués
- **Informations de base** - Navigateur, pays, etc.

## Fonctionnalités Analytics

### Tracking automatique
- **Pages visitées** : Chaque page visitée est enregistrée
- **Sources de trafic** : Sites référents
- **Clics sur liens externes** : Suivi des liens sortants
- **Informations de base** : User agent, timestamp

### Données collectées
- URL de la page visitée
- Site référent (d'où vient le visiteur)
- User agent (navigateur, système d'exploitation)
- Timestamp de la visite

## Structure des fichiers

```
livre/
├── static/
│   ├── analytics.js      # Script client de tracking simple
│   └── custom_template.html # Template HTML avec analytics
├── vercel.json           # Configuration Vercel
├── package.json          # Dépendances Node.js
└── requirements.txt      # Dépendances Python
```

## Commandes utiles

```bash
# Build local
d2lbook build html

# Déploiement local
vercel

# Déploiement en production
vercel --prod
```

## Personnalisation

### Modifier le tracking
Éditez `static/analytics.js` pour ajouter de nouveaux événements à tracker.

### Intégrer un autre service d'analytics
Remplacez le code dans `static/analytics.js` par l'intégration de votre choix.

## Avantages de cette approche

- ✅ **Simple** : Pas de base de données à gérer
- ✅ **Rapide** : Déploiement immédiat
- ✅ **Fiable** : Utilise les services Vercel intégrés
- ✅ **Privé** : Respecte la vie privée des utilisateurs
- ✅ **Gratuit** : Vercel Analytics est inclus gratuitement

## Support

Pour toute question ou problème :
- Email : contact@ivia.africa
- GitHub : https://github.com/IVIA-AF/livre 