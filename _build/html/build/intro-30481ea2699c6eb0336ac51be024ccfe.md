# Bienvenue

Bienvenue dans ce livre sur l’**Apprentissage Automatique**, une ressource complète et entièrement accessible en français. Cet ouvrage s’adresse aux chercheurs, étudiants et praticiens francophones, **en particulier à la jeunesse africaine**, qui souhaitent maîtriser les concepts fondamentaux et avancés de l’intelligence artificielle à travers des explications claires et contextualisées.

## À propos de ce livre

Ce livre couvre un large éventail de sujets, allant des bases mathématiques essentielles aux techniques modernes de *deep learning*. Chaque chapitre est conçu de manière progressive et pédagogique, en s’appuyant sur des **exemples concrets et culturellement familiers**, inspirés des réalités africaines (éducation, agriculture, finance mobile, santé, médias, langues locales, etc.), afin de rendre les notions techniques plus intuitives et directement applicables. L’objectif est de réduire les barrières d’entrée à l’IA en reliant les concepts abstraits à des situations du quotidien.

## À propos d’IVIA-AF

Ce livre s’inscrit dans le cadre de l’initiative **IVIA-AF** (*Initiative pour la Vulgarisation de l’Intelligence Artificielle dans l’Afrique francophone*), une organisation engagée à démocratiser l’accès aux connaissances en IA auprès des communautés francophones d’Afrique et de la diaspora. IVIA-AF promeut une approche **inclusive, contextualisée et orientée vers l’autonomisation de la jeunesse**, en encourageant l’apprentissage, la contribution communautaire et l’innovation locale.

```{admonition} En savoir plus
:class: tip

Pour découvrir notre mission complète, nos autres projets, notre équipe et nos initiatives, visitez notre site web principal : **[www.ivia.africa](https://www.ivia.africa/)**
```

```{admonition} Statut du livre
:class: note

Ce livre est en cours de développement. Certains chapitres sont actuellement disponibles (marqués avec des liens cliquables), tandis que d'autres sont en cours de conversion depuis LaTeX vers Markdown et seront ajoutés progressivement.
```

# Table des Matières

Ce livre couvre les concepts fondamentaux de l'apprentissage automatique, depuis les bases mathématiques jusqu'aux techniques avancées de deep learning. Voici la structure complète de l'ouvrage :

## 1. {doc}`content/chapter1`
- 1.1 C'est quoi Apprentissage Automatique
- 1.2 Convention Mathématiques pour le document

## 2. {doc}`content/chapter2`
- 2.1 Langage Python et ses Librairies
  - 2.1.1 Installation de Python et Anaconda
  - 2.1.2 Prise en main de Python
- 2.2 Les Bases Mathématiques pour l'Apprentissage Automatique
  - 2.2.1 Algèbre linéaire et Analyse
    - Exemples de distances
  - 2.2.2 Calcul du gradient (dérivation)
    - Dérivées de fonctions composées
  - 2.2.3 Probabilités
    - Indépendance et conditionnement
    - Variables aléatoires
      - Variable aléatoire discrète
      - Variable aléatoire continue
    - Loi des grands nombres
    - Intervalles de confiance
  - 2.2.4 Estimations paramétriques
    - Estimation par la méthode des moments
    - Estimation par maximum de vraisemblance

## 3. Apprentissage Supervisé
- 3.1 Problèmes de Régression
  - 3.1.1 La Régression Linéaire
    - La régression linéaire affine
    - Descente de gradient
    - La régression linéaire polynomiale
- 3.2 Les Problèmes de Classification
  - 3.2.1 L'algorithme des K plus proches voisins (K-NN)
    - Algorithme
    - Comment choisir la valeur de K ?
    - Les avantages de l'algorithme de K-NN
    - Les limitations de l'algorithme de K-NN
    - Exemple pratique
  - 3.2.2 L'algorithme du Perceptron
    - Algorithme
  - 3.2.3 La Régression Logistique
    - La régression logistique binaire
  - 3.2.4 La fonction Sigmoïde et ses propriétés
    - Estimation du maximum de vraisemblance
    - Cas pratique
  - 3.2.5 Régression logistique multinomiale
  - 3.2.6 La fonction Softmax et ses propriétés
  - 3.2.7 Estimation du maximum de vraisemblance
  - 3.2.8 Naïve Bayes
    - Entraînement du Naïve Bayes (Exemple Pratique)
  - 3.2.9 Machines à Vecteur de Support (Support Vector Machine: SVM en anglais)
  - 3.2.10 Conclusion

## 4. Apprentissage Non-Supervisé
- 4.1 Introduction et Motivations
- 4.2 Algorithmes de Partitionnement
  - 4.2.1 K-moyennes
    - Comment choisir la valeur de K ?
    - K-moyennes: Algorithme
    - K-moyenne: cas pratique
- 4.3 Réduction de dimension
  - 4.3.1 Positionnement multidimensionnel (MDS en Anglais)
  - 4.3.2 Analyse en Composantes Principales (ACP)
    - Cas d = 2
    - Cas général (d ≥ 2)
    - Algorithme de l'Analyse en Composantes Principales
- 4.4 Applications
- 4.5 Conclusion

## 5. Les méthodes du noyau (Kernel methods)
- 5.1 Motivations et Rappels
  - 5.1.1 Motivations
  - 5.1.2 Rappels
    - Espace de Hilbert
    - Quelques propriétés et caractéristiques des espaces de Hilbert
  - 5.1.3 Noyaux et espaces de Hilbert à noyau reproduisant (RKHS)
- 5.2 Le Noyau: définitions et propriétés
  - 5.2.1 Méthodes à noyaux générales
    - Astuce du noyau (Kernel Trick) et théorème du représentant
  - 5.2.2 Ridge regression (Régression de Ridge), Kernel ridge regression
  - 5.2.3 Méthodes à noyaux et optimisation convexe
    - Rappels d'optimisation convexe
- 5.3 Exemples de noyaux
  - 5.3.1 Noyau linéaire
  - 5.3.2 Noyau polynomial
  - 5.3.3 Noyau de Laplace RBF
  - 5.3.4 Noyau Gaussien
  - 5.3.5 Noyau hyperbolique tangent (Noyau Sigmoid)
- 5.4 Travaux pratiques/méthodes à noyau
  - 5.4.1 Tutoriel: première session
  - 5.4.2 Tutoriel: deuxième session

## 6. Apprentissage Profond (Deep Learning)
- 6.1 Introduction, motivation et contexte
- 6.2 Pourquoi les réseaux de neurones ?
- 6.3 Définitions
- 6.4 Réseaux de neurones artificiels
  - 6.4.1 Le Neurone
  - 6.4.2 La fonction d'activation
    - La fonction de seuil (Threshold function)
    - La fonction Sigmoïde (Sigmoid function)
    - La fonction de redressement (Rectifier en Anglais)
    - La fonction tangente hyperbolique (Hyperbolic Tangent (tanh))
  - 6.4.3 Comment fonctionne le réseau de neurone ?
  - 6.4.4 Comment les réseaux de neurones apprennent ?
  - 6.4.5 Descente graduelle (Gradient Descent)
  - 6.4.6 Descente graduelle stochastique (Stochastic Gradient Descent SGD)
  - 6.4.7 Rétropropagation (Backpropagation)
- 6.5 Réseaux de neurones adaptés au traitement de séquences
  - 6.5.1 Introduction
  - 6.5.2 Architecture de Réseaux de Neurones Récurrents (RNR)
  - 6.5.3 Rétro-propagation à travers le temps
  - 6.5.4 Les Challenges dans l'entraînement des RNR
  - 6.5.5 Long Short-Term Memory (LSTM)
- 6.6 Réseaux de neurones en couches convolutionnelles
  - 6.6.1 Architecture du Réseaux de neurones en couches convolutionnelles (CNN)
  - 6.6.2 L'opération de convolution
- 6.7 Travaux pratiques/méthodes à noyau
  - 6.7.1 Tutoriel: première session
  - 6.7.2 Tutoriel: deuxième session

---

## Contribution

Ce projet est une initiative collaborative et open-source. Nous accueillons chaleureusement les contributions de la communauté francophone en intelligence artificielle. Que vous souhaitiez corriger des erreurs, améliorer des explications, ou ajouter de nouveaux contenus, votre participation est précieuse.

- **Repository GitHub :** [github.com/IVIA-AF/livre](https://github.com/IVIA-AF/livre)
- **Contact :** [contact@ivia.africa](mailto:contact@ivia.africa)
- **Site web :** [www.ivia.africa](https://www.ivia.africa/)
- **X (Twitter) :** [@IviaAf](https://x.com/IviaAf)
- **Youtube :** [@IVIA-AF](https://www.youtube.com/@IVIA-AF)
---

*Pour plus d'informations sur IVIA-AF, nos projets et notre équipe, visitez [www.ivia.africa](https://www.ivia.africa/)*
