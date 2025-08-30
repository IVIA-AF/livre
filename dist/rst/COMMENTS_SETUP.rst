
Système de Commentaires - Guide de Configuration
================================================

Ce guide explique comment configurer et utiliser le système de
commentaires intégré dans votre projet livre IVIA-AF.

🎯 Vue d’ensemble
----------------

Le système de commentaires permet aux lecteurs de : - Poser des
questions sur le contenu - Partager leurs expériences - Suggérer des
améliorations - Discuter avec d’autres apprenants

🚀 Configuration du Système
--------------------------

1. Créer un compte Disqus
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Allez sur `disqus.com <https://disqus.com>`__
2. Créez un compte ou connectez-vous
3. Cliquez sur “Get Started” pour créer un nouveau site
4. Choisissez “I want to install Disqus on my site”
5. Remplissez les informations :

   -  **Website Name**: ``ivia-af-livre`` (ou votre nom préféré)
   -  **Website URL**: L’URL de votre site déployé
   -  **Category**: Education
   -  **Language**: French

2. Obtenir votre Disqus Shortname
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Après la création, vous recevrez un “shortname” (ex: ``ivia-af-livre``).

3. Mettre à jour la Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dans le fichier ``static/custom_template.html``, remplacez :

.. raw:: latex

   \diilbookstyleinputcell

.. code:: javascript

   s.src = 'https://ivia-af-livre.disqus.com/embed.js';

Par votre shortname :

.. raw:: latex

   \diilbookstyleinputcell

.. code:: javascript

   s.src = 'https://VOTRE_SHORTNAME.disqus.com/embed.js';

4. Personnaliser l’Apparence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modifiez le fichier ``static/custom.css`` pour ajuster : - Couleurs -
Espacement - Typographie - Responsive design

📝 Utilisation
-------------

Pour les Lecteurs
~~~~~~~~~~~~~~~~~

1. **Lire le contenu** d’une leçon
2. **Faire défiler** jusqu’à la section “Commentaires et Discussions”
3. **Cliquer** sur la zone de commentaires
4. **Se connecter** avec Disqus (ou créer un compte)
5. **Écrire** et **publier** un commentaire

Pour les Modérateurs
~~~~~~~~~~~~~~~~~~~~

1. **Accéder** au `panneau d’administration
   Disqus <https://disqus.com/admin/>`__
2. **Modérer** les commentaires selon vos règles
3. **Configurer** les filtres anti-spam
4. **Gérer** les utilisateurs si nécessaire

🔧 Personnalisation Avancée
--------------------------

Ajouter des Commentaires à de Nouvelles Leçons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Créer** votre fichier ``.md``
2. **Ajouter** à la fin :

.. raw:: latex

   \diilbookstyleinputcell

.. code:: markdown

   ---

   ## Commentaires et Discussions

   Partagez vos questions, commentaires et expériences avec la communauté IVIA-AF ! Utilisez la section de commentaires ci-dessous pour :

   - Poser des questions sur les concepts présentés
   - Partager vos expériences avec l'apprentissage automatique
   - Suggérer des améliorations ou corrections
   - Discuter avec d'autres apprenants

   *Les commentaires sont modérés pour maintenir un environnement d'apprentissage respectueux et constructif.*

Intégration avec d2lbook
~~~~~~~~~~~~~~~~~~~~~~~~

Le système est conçu pour s’intégrer parfaitement avec d2lbook : -
**Template personnalisé** : ``static/custom_template.html`` - **Styles
CSS** : ``static/custom.css`` - **Commentaires automatiques** sur toutes
les pages

🌐 Déploiement
-------------

Vercel (Recommandé)
~~~~~~~~~~~~~~~~~~~

1. **Pousser** vos changements vers GitHub
2. **Vercel** se reconstruira automatiquement
3. **Vérifier** que les commentaires apparaissent

Autres Plateformes
~~~~~~~~~~~~~~~~~~

Le système fonctionne sur toute plateforme statique : - GitHub Pages -
Netlify - Surge - etc.

📊 Analytics et Modération
-------------------------

Disqus Analytics
~~~~~~~~~~~~~~~~

-  **Vues** des commentaires
-  **Engagement** des utilisateurs
-  **Tendances** de discussion
-  **Démographie** des utilisateurs

Modération
~~~~~~~~~~

-  **Filtrage automatique** du spam
-  **Modération manuelle** des commentaires
-  **Règles personnalisables**
-  **Bannissement** d’utilisateurs si nécessaire

🚨 Dépannage
-----------

Les Commentaires n’Apparaissent Pas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Vérifier** que Disqus est activé
2. **Contrôler** la console du navigateur pour les erreurs
3. **S’assurer** que le shortname est correct
4. **Vérifier** que le site est accessible publiquement

Problèmes de Performance
~~~~~~~~~~~~~~~~~~~~~~~~

1. **Charger** Disqus de manière asynchrone (déjà configuré)
2. **Utiliser** un CDN pour les ressources statiques
3. **Optimiser** les images et le contenu

🔒 Sécurité et Confidentialité
-----------------------------

Données Collectées
~~~~~~~~~~~~~~~~~~

Disqus collecte : - **Informations de base** (nom, email) -
**Commentaires** et interactions - **Données de navigation** (cookies)

Conformité RGPD
~~~~~~~~~~~~~~~

-  **Consentement** explicite requis
-  **Droit à l’oubli** disponible
-  **Transparence** sur l’utilisation des données

📞 Support
---------

Ressources Utiles
~~~~~~~~~~~~~~~~~

-  `Documentation Disqus <https://help.disqus.com/>`__
-  `Forum d’entraide <https://disqus.com/support/>`__
-  `Contact IVIA-AF <mailto:contact@ivia.africa>`__

Problèmes Techniques
~~~~~~~~~~~~~~~~~~~~

1. **Vérifier** la documentation officielle
2. **Consulter** les forums Disqus
3. **Contacter** l’équipe IVIA-AF

--------------

*Dernière mise à jour : $(date)* *Version : 1.0.0*
