
Pré-requis
==========

Python est le langage de programmation préféré des Data Scientistes. Ils
ont besoin d’un langage facile à utiliser, avec une disponibilité
décente des bibliothèques et une grande communauté. Les projets ayant
des communautés inactives sont généralement moins susceptibles de mettre
à jour leurs plates-formes. Mais alors, pourquoi Python est populaire en
Data Science ?

Python est connu depuis longtemps comme un langage de programmation
simple à maîtriser, du point de vue de la syntaxe. Python possède
également une communauté active et un vaste choix de bibliothèques et de
ressources. Comme résultat, vous disposez d’une plate-forme de
programmation qui est logique d’utiliser avec les technologies
émergentes telles que l’apprentissage automatique (Machine Learning) et
la Data Science.

Langage Python et ses Librairies
--------------------------------

Python est un langage de programmation puissant et facile à apprendre.
Il dispose de structures de données de haut niveau et permet une
approche simple mais efficace de la programmation orientée objet. Parce
que sa syntaxe est élégante, que son typage est dynamique et qu’il est
interprété, Python est un langage idéal pour l’écriture de scripts quand
on fait de l’apprentissage automatique et le développement rapide
d’applications dans de nombreux domaines et sur la plupart des
plate-formes.

Installation de Python et Anaconda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

L’installation de Python peut-être un vrai challenge. Déjà il faut se
décider entre les versions 2.X et 3.X du langage, par la suite, choisir
les librairies nécessaires (ainsi que les versions compatibles) pour
faire de l’apprentissage automatique (Machine Learning); sans oublier
les subtilités liées aux différents Systèmes d’exploitation (Windows,
Linux, Mac…) qui peuvent rendre l’installation encore plus
*"douloureuse"*.

Dans cette partie nous allons installer pas à pas un environnement de
développement Python en utilisant Anaconda[^1]. A l’issue de cette
partie, nous aurons un environnement de développement fonctionnel avec
les librairies (packages) nécessaires pour faire de l’apprentissage
automatique (Machine Learning).

**Qu’est ce que Anaconda ?**

L’installation d’un environnement Python complet peut-être assez
complexe. Déjà, il faut télécharger Python et l’installer, puis
télécharger une à une les librairies (packages) dont on a besoin.
Parfois, le nombre de ces librairies peut-être grand. Par ailleurs, il
faut s’assurer de la compatibilité entre les versions des différents
packages qu’on a à télécharger. *Bref, ce n’est pas amusant*!

Alors Anaconda est une distribution Python. À son installation, Anaconda
installera Python ainsi qu’une multitude de packages dont vous pouvez
consulter la
`liste <https://docs.anaconda.com/anaconda/packages/pkg-docs/#Python-3-7>`__.
Cela nous évite de nous ruer dans les problèmes d’incompatibilités entre
les différents packages. Finalement, Anaconda propose un outil de
gestion de packages appelé Conda. Ce dernier permettra de mettre à jour
et installer facilement les librairies dont on aura besoin pour nos
développements.

**Téléchargement et Installation de Anaconda**

**Note**: Les instructions qui suivent ont été testées sur Linux/Debian.
Le même processus d’installation pourra s’appliquer pour les autres
systèmes d’exploitation.

Pour installer Anaconda sur votre ordinateur, vous allez vous rendre sur
le `site officiel <http://docs.anaconda.com/anaconda/navigator/>`__
depuis lequel l’on va télécharger directement la dernière version
d’Anaconda. Prenez la version du binaire qu’il vous faut :

-  Choisissez le système d’exploitation cible (Linux, Windows, Mac,
   etc…)

-  Sélectionnez la version 3.X (à l’heure de l’écriture de ce document,
   c’est la version 3.8 qui est proposée, surtout pensez à toujours
   installer la version la plus récente de Python), compatible (64 bits
   ou 32 bits) avec l’architecture de votre ordinateur.

Après le téléchargement, si vous êtes sur Windows, alors rien de bien
compliqué double cliquez sur le fichier exécutable et suivez les
instructions classique d’installation d’un logiciel sur Windows.

Si par contre vous êtes sur Linux, alors suivez les instructions qui
suivent:

-  Ouvrez votre terminal et rassurez vous que votre chemin accès est
   celui dans lequel se trouve votre fichier d’installation.

-  Exécutez la commande: $ bash Anaconda3-2020.02-Linux-x86_64.sh,
   rassurez vous du nom du fichier d’installation, il peut changer selon
   la version que vous choisissez.

Après que l’installation se soit déroulée normalement, éditez le fichier
caché **.bashrc** pour ajouter le chemin d’accès à Anaconda. Pour cela
exécutez les commandes suivantes:

-  $ cd ~

-  $ gedit .bashrc

-  Ajoutez cette commande à la dernière ligne du fichier que vous venez
   d’ouvrir

-  export PATH= ~/anaconda3/bin:$PATH

Maintenant que c’est fait, enregistrez le fichier et fermez-le. Puis
exécutez les commandes suivantes

-  $ conda init

-  $ Python

Pour ce qui est de l’installation sur Mac, veuillez suivre la procédure
d’installation dans la `documentation
d’Anaconda <https://docs.anaconda.com/anaconda/install/mac-os/>`__.

Il existe une distribution appelée
`Miniconda <https://docs.conda.io/en/latest/miniconda.html>`__ qui est
un programme d’installation minimal gratuit pour conda. Il s’agit d’une
petite version bootstrap d’Anaconda qui inclut uniquement conda, Python,
les packages dont ils dépendent, et un petit nombre d’autres packages
utiles.

Terminons cette partie en nous familiarisant avec quelques notions de la
programmation Python.

**Première utilisation de Anaconda**

La distribution Anaconda propose deux moyens d’accéder à ses fonctions:
soit de manière graphique avec Anaconda-Navigator, soit en ligne de
commande (depuis Anaconda Prompt sur Windows, ou un terminal pour Linux
ou MacOS). Sous Windows ou MacOs, démarrez Anaconda-Navigator dans le
menu des programmes. Sous Linux, dans un terminal, tapez la commande : $
anaconda-navigator (cette commande est aussi disponible dans le prompt
de Windows). Anaconda-Navigator propose différents services (déjà
installés, ou à installer). Son onglet Home permet de lancer le service
désiré. Les principaux services à utiliser pour développer des
programmes Python sont :

-  Spyder

-  IDE Python

-  Jupyter notebook et jupyter lab : permet de panacher des cellules de
   commandes Python (code) et des cellules de texte (Markdown).

Pour la prise en main de Python nous allons utiliser jupyter lab.

Prise en main de Python
~~~~~~~~~~~~~~~~~~~~~~~

Nous avons préparé un notebook qui nous permettra d’aller de zèro à demi
Héros en Python. Le notebook se trouve
`ici <https://colab.research.google.com/drive/1zILtNrCmPDFyQQ1Ev1H4jeHx7FuyEZ27?usp=sharing>`__.

Python pour les debutants : Notions de bases du python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les nombres avec Python!
''''''''''''''''''''''''

Dans cette partie, nous allons tout apprendre comment utiliser les
nombres sur Python.

Nous allons couvrir les points suivants :

1. Les types de nombres sur Python
2. Arithmetique de base sur les nombres
3. Différences entre Python 2 et 3
4. Assignation d’objets dans Python

Les types de nombres
''''''''''''''''''''

Python a plusieurs “types” de nombres. Nous nous occuperons
principalement des entiers (integers) et des nombres à virgule flottante
(float).

Le type entier (integer) représente des nombres entiers, positifs ou
negatifs. Par exemple: 7 et -1 sont des integers.

Le type flottant (float) de Python est facile à identifier parce que les
nombres sont représentés avec la partie décimal (Attention, ici les
nombre decimaux sont representer avec un point et non la virgule comme
habituellement en langue française), ou alors avec le signe exponentiels
(reprensenter par **e**) pour représenter les puissances de 10. Par
exemple, 2.0 et -2.1 sont des nombres de type flottant. 2e3 ( 2 fois 10
à la puissance 3) est aussi un nombre de type flottant en Python.

Voici un tableau des deux types que nous manipulerons le plus dans ce
cours:

.. _table_nombre:

.. table:: Les types de nomber en Python.

   ======================== ==============================
   Exemples                 Type
   ======================== ==============================
   1, 4, -2, 100            Integers
   1.4, 0.3, -0.5, 2e2, 3e2 Floating-point numbers (float)
   ======================== ==============================


Voyons maintenant, quelques examples d’arithmétique simples que l’on
peux appliquer sur ses elements.

Arithmétique
            

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Addition de 1 et 3 = 4
    1+3




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    4



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Soustraction de 1 dans 3 = 2
    3-1




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    2



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Multiplication de 2 par 2 = 4
    2*2




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    4



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Division de 5 par 2 = 2.5 (remaquez qu'on a la un flottant)
    5/2




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    2.5



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Puissances. 2 a la  puissances 3 = 8
    2**3




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    8



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    #la racine carree peut se calculer  de la même manière = 2.0
    4**0.5




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    2.0



Ordre de priorite
'''''''''''''''''

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Voyons quel ordre de priorite python fais sur les operteurs
    2 + 10 * 10 + 3  # avec ceci nous obtenons un resultats errone = 105




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    105



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Avec des parenthèse nous pouvons garder le contrôle de ces priorités
    (2+10) * (10+3)




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    156



Les variables
'''''''''''''

Maintenant que nous savons comment utiliser python en mode calculette,
nous pouvons créer des variables et leur assigner des valeurs comme des
nombres. Notons que l’utilisation des variables sur python est un tout
petit peu different que ce qui ce passe dans d’autre langage de
programmation. Contrairement a d’autre language, python utilise une
technique de typage faible. Les variables ne sont pas declarees a
l’avance avant l’untilisation.

Il suffit d’un simple signe égal = pour assigner un nom à une variable.
Voyons quelques exemples pour détailler la façon de faire.

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Créons un objet nommé "x" et "y" et nous leur assignons la valeur 5 et .2 respectivement
    x = 5 # ici la variable x est de type integer
    y = .2 # ici la variable y est de type flottant (notons que 0.2 peut aussi s'ecrire .2 tout simplement)

Maintenant, nous pouvons appeler *x* or *y* dans un script Python qui
les traitera comme le nombre 5 ou .2 respectivement

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # additionner des objets
    x+y




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    5.2



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Ré-assignation
    x = 10

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Vérification
    x




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    10



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Nous utilisons x pour assigner x de nouveau
    x = x + x

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Vérification
    x




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    20



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Incrementation par 1 (on peux aussi incrementer avec n'importe quel nombre)
    x = x+1

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    x




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    21



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    #Autre syntaxe pour incrementer une variable
    x += 1

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    x




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    22



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    #Decrementation par 1
    x = x -1

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    x




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    21



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    #Autre syntaxe pour decrementer une variable
    x -= 1

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    x




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    20



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    #Nous pouvons aussi multiplier l'ancienne valeur de x par un quelconque nombre.
    x *=2

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    x




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    40



.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    #Nous pouvons aussi diviser l'ancienne valeur de x par un quelconque nombre.
    x /=2

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    x




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    20.0



NB: Toutes les operations que nous venons de voir s’applique aussi sur
les flottants

**Tout de meme, voici quelques règles à respecter pour créer un nom de
variable :**

1. Les noms ne doivent pas commencer par un nombre.
2. Pas d’espace dans les noms, utilisez \_ à la place
3. Interdit d’utiliser les symboles suivants : ’",<>/?|()!@#$%^&*~-+
4. C’est une bonne pratique (PEP8) de mettre les noms en minuscules

Les noms de variables permettent de conserver et manipuler plusieurs
valeurs de façon simple avec Python.

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Utilisez toujours des noms explicites pour mieux suivre ce que fait votre code !
    prix_vente = 280
    
    prix_unitaire = 150
    
    benefice = prix_vente - prix_unitaire

.. raw:: latex

   \diilbookstyleinputcell

.. code:: python

    # Visualiser le benefice !
    benefice




.. raw:: latex

   \diilbookstyleoutputcell

.. parsed-literal::
    :class: output

    130



Les Bases Mathématiques pour l’Apprentissage Automatique
--------------------------------------------------------

Dans cette section, nous allons présenter les notions mathématiques
essentielles à l’apprentissage automatique (machine learning). Nous
n’aborderons pas les théories complexes des mathématiques afin de
permettre aux débutants (en mathématiques) ou mêmes les personnes hors
du domaine mais intéressées à l’apprentissage automatique de pouvoir en
profiter.

Algèbre linéaire et Analyse
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Définition d’espaces vectoriels.** Un espace vectoriel est un triplet
:math:`(V, +, *)` formé d’un ensemble :math:`V` muni de deux lois,

.. math::


   \begin{aligned}
        +:\quad & V\times V \longrightarrow{V}\\
       &(u,v)\mapsto u+v \\
       \text{et} \qquad \qquad\\
       *:\quad &\mathbb{K}\times V \longrightarrow{V}, \text{ avec $\mathbb{K}$ un corps commutatif}\\
       &(\lambda,v)\mapsto \lambda * v=\lambda v\end{aligned}

qui vérifient:

1. :math:`\text{ associativité de } + :  \forall\  u,v, w \in V, \quad (u+v)+w=u+(v+w)`

2. :math:`\text{ commutativité de } + : \forall\ u,v\in V,\quad u+v=v+u`

3. :math:`\text{ existence d'élément neutre pour } + :  \exists~ e \in V : \forall\ u \in V, \quad u+e=e+u=u`

4. :math:`\text{ existence d'élément opposé pour } + : \forall \ u \in V, \exists ~ v \in V :u+v=v+u=0. \text{ On note } v=-u \text{ et } v \text{ est appelé l'opposé de } u`

5. :math:`\text{ existence de l'unité pour } * :  \exists~ e \in \mathbb{K} \text{ tel que } \forall\  u\in V,\quad e*u=u`

6. :math:`\text{ associativité de } * :  \forall\  (\lambda_1, \lambda_2, u) \in \mathbb{K} \times \mathbb{K}\times V,\quad  (\lambda_1 \lambda_2)* u =\lambda_1*(\lambda_2 * u)`

7. :math:`\text{ somme de vecteurs (distributivité de * sur +)} :  \forall\  (\lambda, u, v) \in \mathbb{K}\times V\times V, \quad\lambda*(u+v)=\lambda * u+\lambda * v`

8. :
   :math:`\forall\  (\lambda_1, \lambda_2, u) \in \mathbb{K} \times \mathbb{K}\times V,\quad  (\lambda_1+\lambda_2) * u=\lambda_1 * u +\lambda_2 * u.`

| **Remarque 1:** Les éléments de :math:`V` sont appelés des
  **vecteurs**, ceux de :math:`\mathbb{K}` sont appelés des
  **scalaires** et l’élément neutre pour :math:`+` est appelé **vecteur
  nul**. Finalement, :math:`V` est appelé :math:`\mathbb{K}`-espace
  vectoriel ou espace vectoriel sur :math:`\mathbb{K}`.
| **Base d’un espace vectoriel.** Soit :math:`V` un
  :math:`\mathbb{K}`-espace vectoriel. Une famille de vecteurs
| :math:`\mathcal{B}=\big\{b_1, b_2, \dots, b_n\big\}` est appelée base
  de :math:`V` si les deux propriétés suivantes sont satisfaites:

-  :math:`\forall\  u \in V, \exists~ c_1, \dots, c_n \in \mathbb{K}`
   tels que :math:`\displaystyle u = \sum_{i=1}^{n}c_i b_i`
   (On dit que :math:`\mathcal{B}` est
   :math:`\textbf{une famille génératrice}` de :math:`V`).
-  :math:`\displaystyle \forall\  \lambda_1, \dots, \lambda_n \in \mathbb{K}, \quad\sum_{i=1}^{n}\lambda_i b_i=0\Longrightarrow \lambda_i = 0 \quad\forall\  i`.
   (On dit que les éléments de :math:`\mathcal{B}` sont *linéairement
   indépendants*).

| Lorsque :math:`\displaystyle u = \sum_{i=1}^{n}c_i b_i`, on dit que
  :math:`c_1, \dots, c_n` sont les coordonnées de :math:`u` dans la base
  :math:`\mathcal{B}`. Si de plus aucune confusion n’est à craindre, on
  peut écrire:

  .. math::

     \mathbf{u}=\begin{bmatrix}
     c_1\\c_2\\ \vdots\\ c_n
     \end{bmatrix}.

  \ **Définition.** Le nombre d’éléments dans une base d’un espace
  vectoriel est appelé **dimension** de l’espace vectoriel.
| **NB:** Un espace vectoriel ne peut être vide (il contient toujours le
  vecteur nul). L’\ **espace vectoriel nul** :math:`\{0\}` n’a pas de
  base et est **de dimension nulle**. Tout **espace vectoriel non nul**
  de dimension finie admet une infinité de bases mais sa **dimension est
  unique**.
| **Exemples d’espaces vectoriels**: Pour tous :math:`n,m\ge1`,
  l’ensemble des matrices :math:`\mathcal{M}_{nm}` à coefficients réels
  et l’ensemble :math:`\mathbb{R}^n` sont des :math:`\mathbb{R}`-espace
  vectoriels. En effet, il est très facile de vérifier que nos exemples
  satisfont les huit propriétés énoncées plus haut. Dans le cas
  particulier :math:`V=\mathbb{R}^n`, toute famille d’exactement
  :math:`n` vecteurs linéairement indépendants en est une base. En
  revanche, toute famille de moins de :math:`n` vecteurs ou qui contient
  plus que :math:`n` vecteurs ne peut être une base de
  :math:`\mathbb{R}^n`.

**Matrices**: Soit :math:`\mathbb{K}` un corps commutatif. Une matrice
en mathématiques à valeurs dans :math:`\mathbb{K}` est un tableau de
nombres, où chaque nombre est un élément de :math:`\mathbb{K}`. Chaque
ligne d’une telle matrice est un vecteur (élément d’un
:math:`\mathbb{K}`-espace vectoriel). Une matrice est de la forme:

.. math::

   \mathbf{M}=\begin{bmatrix}
   a_{11} &a_{12} \dots a_{1n}\\
   a_{21} &a_{22} \dots a_{2n}\\
   \vdots\\
   a_{m1}& a_{m2} \dots a_{mn}
   \end{bmatrix}.

On note aussi
:math:`\mathbf{M}=\big{(}a_{ij}\big{)}_{1\le i\le m, 1\le j\le n}`.

| La matrice ci-dessus est carrée si :math:`m=n`. Dans ce cas, la suite
  :math:`[a_{11}, a_{22}, \dots, a_{mm}]` est appelée **diagonale** de
  :math:`M`. Si tous les coefficients hors de la diagonale sont zéro, on
  dit que la matrice est diagonale. Une matrice avec tous ses
  coefficients nuls est dite matrice **nulle**.
| **Produit de matrices.** Soient
  :math:`\mathbf{A}=\big{(}a_{ij}\big{)}_{1\le i\le m, 1\le j\le n}, \mathbf{B}=\big{(}b_{ij}\big{)}_{1\le i\le n, 1\le j\le q}`
  deux matrices.
| On définit le produit de :math:`\mathbf{A}` par :math:`\mathbf{B}` et
  on note :math:`\mathbf{A}\times \mathbf{B}` ou simplement
  :math:`\mathbf{A}\mathbf{B}`, la matrice :math:`M` définie par:

  .. math::

     \begin{aligned}
         \mathbf{M}_{ij} = \sum_{\ell=1}^{n}a_{i\ell}b_{\ell j}, \text{ pour tout } i \text{ et } j.\end{aligned}

  **Important.**

-  Le produit :math:`\mathbf{AB}` est possible si et seulement si le
   nombre de colonnes de :math:`\mathbf{A}` est égal au nombre de lignes
   de :math:`\mathbf{B}`.

-  Dans ce cas, :math:`\mathbf{AB}` a le même nombre de lignes que
   :math:`\mathbf{A}` et le même nombre de colonnes que
   :math:`\mathbf{B}`.

-  Un autre point important à noter est que le produit matriciel n’est
   pas commutatif (:math:`\mathbf{AB}` n’est pas toujours égal à
   :math:`\mathbf{BA}`).

**Exemple.** Soient les matrices :math:`\mathbf{A}` et
:math:`\mathbf{B}` définies par:

.. math::

   \mathbf{A} = \begin{bmatrix}
   2 & -3 & 0\\
   5 &11 & 5\\
   1& 2 & 3
   \end{bmatrix}, \quad \mathbf{B} = \begin{bmatrix}
   1 & 3\\
   -5 &1\\
   1 & 2
   \end{bmatrix},
   \mathbf{A}+\mathbf{B} = \begin{bmatrix}
   1 & 3\\
   -5 &1\\
   1 & 2
   \end{bmatrix}

Le nombre de colonnes de la matrice :math:`\mathbf{A}` est égal au
nombre de lignes de la matrice :math:`\mathbf{B}`.

.. math::

   \mathbf{AB} = \begin{bmatrix}
   2\times1+(-3)\times(-5)+0\times1 & 2\times3+(-3)\times1+0\times2\\
   5\times1+11\times(-5)+5\times1 &5\times3+11\times1+5\times2\\
   1\times1+2\times(-5)+3\times1& 1\times3+2\times1+3\times2
   \end{bmatrix} = \begin{bmatrix}
   17 & 3\\
   -45 &33\\
   -6 & 11
   \end{bmatrix}.

Le produit :math:`\mathbf{BA}` n’est cependant pas possible.

| **Somme de matrices et multiplication d’une matrice par un scalaire.**
| La somme de matrices et multiplication d’une matrice par un scalaire
  se font coefficients par coefficients.
| Avec les matrice :math:`\mathbf{A}, \mathbf{B}` de l’exemple
  précédent, et
  :math:`\mathbf{C}=\begin{bmatrix} -2 & -7 & 3\\ 5 &10 & 5\\ 12& 9 & 3 \end{bmatrix}`,
  on a:

  .. math::

     \mathbf{A}+ \mathbf{C} = \begin{bmatrix}
     2+(-2) & -3+(-7) & 0+3\\
     5+5 &11+10 & 5+5\\
     1+12& 2+9 & 3+3
     \end{bmatrix}=\begin{bmatrix}
     0 & -10 & 3\\
     10 &21 & 10\\
     13& 11 & 6
     \end{bmatrix}, \text{ et pour tout } \lambda \in \mathbb{R}, \quad
     \lambda \mathbf{B} = \begin{bmatrix}
     \lambda & 3 \lambda\\
     -5 \lambda & \lambda\\
     \lambda & 2\lambda
     \end{bmatrix}.

| **NB:** La somme de matrice n’est définie que pour des matrices de
  même taille.
| **Déterminant d’une matrice.**

Soit :math:`\mathbf{A}=(a_{ij})_{1\le i\le n, 1\le j\le n}` une matrice
carrée d’ordre :math:`n`. Soit :math:`\mathbf{A}_{i,j}` la sous-matrice
de :math:`\mathbf{A}` obtenue en supprimant la ligne :math:`i` et la
colonne :math:`j` de :math:`\mathbf{A}`. On appelle **déterminant** (au
développement suivant la ligne :math:`i`) de :math:`\mathbf{A}` et on
note :math:`\operatorname{det}(\mathbf{A})`, le nombre

.. math::


   \begin{aligned}
       \operatorname{det}(\mathbf{A}) = \sum_{j=1}^{n}a_{ij}(-1)^{i+j}\operatorname{det}(\mathbf{A}_{i,j}),\end{aligned}

avec le déterminant d’une matrice carrée de taille :math:`2\times 2`
donné par:

.. math::

   \begin{aligned}
       \operatorname{det} \left(\begin{bmatrix}
   a & b\\
   c & d\\
   \end{bmatrix}\right) = ad-bc.\end{aligned}

| **NB:** Le développement suivant toutes les lignes donne le même
  résultat.
| Le déterminant d’une matrice a une deuxième formulation dite de
  `Leibniz <https://fr.wikipedia.org/wiki/Formule_de_Leibniz#D>`__ que
  nous n’introduisons pas dans ce document.
| **Inverse d’une matrice.** Soit :math:`\mathbf{A}` une matrice carrée
  d’ordre :math:`n`. :math:`\mathbf{A}` est **inversible** s’il existe
  une autre matrice notée :math:`\mathbf{A}^{-1}` telle que
  :math:`\mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=\mathbf{I}_n`,
  où :math:`\mathbf{I}_n` est la matrice identité de taille
  :math:`n\times n`.
| Les matrices, leurs inverses et les opérations sur les matrices sont
  d’une importance capitale dans l’apprentissage automatique.
| **Vecteurs propres, valeurs propres d’une matrice.**
| Soient :math:`E` un espace vectoriel et :math:`\mathbf{A}` une
  matrice. Un vecteur :math:`\mathbf{v}\in E` est dit **vecteur propre**
  de :math:`\mathbf{A}` si :math:`\mathbf{v}\neq 0` et il existe un
  scalaire :math:`\lambda` tel que
  :math:`\mathbf{A}\mathbf{v}=\lambda \mathbf{v}`. Dans ce cas, on dit
  que :math:`\lambda` est la **valeur propre** associée au vecteur
  propre :math:`\mathbf{v}`.

| **Applications linéaires et changement de base d’espaces vectoriels.**
| Soient :math:`(E, \mathcal{B}),\ (F, \mathcal{G})` deux
  :math:`\mathbb{K}`-espace vectoriels, chacun muni d’une base et
  :math:`f:\ E \rightarrow F` une application.
| On dit que :math:`f` est **linéaire** si les propriétés suivantes sont
  satisfaites:

1. Pour tous :math:`\mathbf{u}, \mathbf{v}\in E`,
   :math:`f(\mathbf{u}+\mathbf{v})=f(\mathbf{u})+f(\mathbf{v})`.

2. Pour tout :math:`(\lambda, \mathbf{u}) \in \mathbb{K}\times E`,
   :math:`f(\lambda \mathbf{u})=\lambda f(\mathbf{u})`.

| On suppose que :math:`\mathcal{B}=\{e_1, e_2, \dots, e_n\}` et
  :math:`\mathcal{G}=\{e'_1, e'_2, \dots, e'_m\}`.
| De manière équivalente, :math:`f` est linéaire s’il existe une matrice
  :math:`\mathbf{A}` telle que pour tout
  :math:`\mathbf{x}\in E, \quad f(x)=\mathbf{A}\mathbf{x}`.
| Dans ce cas, la matrice :math:`\mathbf{A}` que l’on note
  :math:`Mat_{\mathcal{B},\mathcal{G}}(f)` est appelée matrice
  (représentative) de l’application linéaire :math:`f` dans le couple de
  coordonnées :math:`(\mathcal{B},\mathcal{G})`.
| La matrice :math:`\mathbf{A}` est unique et de taille
  :math:`m\times n` (notez la permutation *dimension de l’espace
  d’arrivée puis dimension de l’espace de départ dans la taille de la
  matrice*). De plus, la colonne :math:`j` de la matrice
  :math:`\mathbf{A}` est constituée des coordonnées de :math:`f(e_j)`
  dans la base :math:`\mathcal{G}` de :math:`F`. Lorsque :math:`E=F`,
  l’application linéaire :math:`f` est appelée **endomorphisme** de
  :math:`E` et on écrit simplement :math:`Mat_{\mathcal{B}}(f)` au lieu
  de :math:`Mat_{\mathcal{B},\mathcal{G}}(f)`.

| **Définition.** Soient :math:`E` un espace vectoriel de dimension
  finie et, :math:`\mathcal{B}` et :math:`\mathcal{C}`, deux bases de
  :math:`E`. On appelle **matrice de passage** de la base
  :math:`\mathcal{B}` à la base :math:`\mathcal{C}` la matrice de
  l’application identité

  .. math::

     \begin{aligned}
         id_E: \quad &(E, \mathcal{C})\rightarrow (E, \mathcal{B}):\\
         & x \mapsto x\quad .\end{aligned}

  \ Cette matrice est notée :math:`P_{\mathcal{B}}^{\mathcal{C}}` et on
  a
  :math:`P_{\mathcal{B}}^{\mathcal{C}}:=Mat_{\mathcal{C},\mathcal{B}}(id_E)`.
| **Note:** Si
  :math:`\mathbf{x}=\begin{bmatrix} x_1\\x_2\\ \vdots\\ x_n \end{bmatrix}`
  est un vecteur de :math:`E` exprimé dans la base :math:`\mathcal{B}`,
  alors l’expression de :math:`\mathbf{x}` dans la base
  :math:`\mathcal{C}` est donnée par
  :math:`\begin{bmatrix} x'_1\\x'_2\\ \vdots\\ x'_n \end{bmatrix}=(P_{\mathcal{B}}^{\mathcal{C}})^{-1}\mathbf{x}=P_{\mathcal{C}}^{\mathcal{B}}\mathbf{x}`.
| **Exemple.** Si :math:`E=\mathbb{R}^3` avec ses deux bases

| 

  .. math::


     \mathcal{B}=\left(
     \begin{bmatrix}
     1\\0\\0
     \end{bmatrix},\begin{bmatrix}
     0\\1\\0
     \end{bmatrix},\begin{bmatrix}
     0\\0\\1
     \end{bmatrix}
     \right) \text{ et } \mathcal{C}=\left(
     \begin{bmatrix}
     -1\\2\\3
     \end{bmatrix},\begin{bmatrix}
     0\\1\\5
     \end{bmatrix},\begin{bmatrix}
     0\\0\\1
     \end{bmatrix}
     \right),

  \ on a
  :math:`P_{\mathcal{B}}^{\mathcal{C}} = \begin{bmatrix} -1&0&0\\ 2&1&0\\ 3&5&1 \end{bmatrix}`
  (c’est-à-dire qu’on exprime les vecteurs de :math:`\mathcal{C}` dans
  :math:`\mathcal{B}` pour former
  :math:`P_{\mathcal{B}}^{\mathcal{C}}`).
| **Formule du changement de base pour une application linéaire.**
| Soient :math:`E` une application linéaire et, :math:`\mathcal{B}` et
  :math:`\mathcal{C}`, deux bases de :math:`E`. Alors

  .. math:: Mat_{\mathcal{C}}(f)=P_{\mathcal{C}}^{\mathcal{B}} Mat_{\mathcal{B}}(f)P_{\mathcal{B}}^{\mathcal{C}},

  ou encore

  .. math:: Mat_{\mathcal{C}}(f)=(P_{\mathcal{B}}^{\mathcal{C}})^{-1} Mat_{\mathcal{B}}(f)P_{\mathcal{B}}^{\mathcal{C}}.
| **Diagonalisation et décomposition en valeurs singulières.**
| **Diagonalisation.** Soit :math:`\mathbf{A}` une matrice carrée à
  coefficients dans
  :math:`\mathbb{K}=\mathbb{R} \text{ ou } \mathbb{C}`. On dit que
  :math:`\mathbf{A}` est **diagonalisable** s’il existe une matrice
  inversible :math:`\mathbf{P}` et une matrice diagonale
  :math:`\mathbf{D}` telles que
  :math:`\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}`. On dit aussi
  que :math:`\mathbf{A}` est similaire à :math:`\mathbf{D}`.
| **Important.** Soient :math:`E` un espace vectoriel de dimension finie
  et :math:`f` un endomorphisme de :math:`E` de matrice représentative
  (dans une base :math:`\mathcal{B}` de :math:`E`) diagonalisable
  :math:`\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^{-1}`. On rappelle
  que les colonnes de :math:`\mathbf{P}` sont les vecteurs propres de
  :math:`\mathbf{A}`. Alors ces colonnes (dans leur ordre) constituent
  une base de :math:`E`, et dans cette base, la matrice
  :math:`\mathbf{A}` est représentée par la matrice diagonale
  :math:`\mathbf{D}`. En d’autres termes, si :math:`\mathcal{C}` est la
  base des vecteurs propres de :math:`\mathbf{A}`, alors
  :math:`Mat_{\mathcal{C}}(f)=\mathbf{D}`. Enfin, la matrice
  :math:`\mathbf{D}` est constituée des valeurs propres de
  :math:`\mathbf{A}` et le processus de calcul de :math:`\mathbf{P}` et
  :math:`\mathbf{D}` est appelé **diagonalisation**.
| **Décomposition en valeurs singulières.**
| Soit :math:`\mathbf{M}` une matrice de taille :math:`m\times n` et à
  coefficients dans
  :math:`\mathbb{K}=\mathbb{R} \text{ ou } \mathbb{C}`. Alors
  :math:`\mathbf{M}` admet une factorisation de la forme
  :math:`\mathbf{M}=\mathbf{U}\mathbf{\Sigma} \mathbf{V}^*`, où $$

-  | :math:`\mathbf{U}` est une matrice unitaire (sur
     :math:`\mathbb{K}`) de taille :math:`m\times m`.

-  | :math:`\mathbf{V}^*` est l’adjoint (conjugué de la transposée) de
     :math:`\mathbf{V}`, matrice unitaire (sur :math:`\mathbb{K}`) de
     taille :math:`n\times n`

-  :math:`\mathbf{\Sigma}` est une matrice de taille :math:`m\times n`
   dont les coefficients diagonaux sont les valeurs singulières de
   :math:`\mathbf{M}`, i.e, les racines carrées des valeurs propres de
   :math:`\mathbf{M}^*\mathbf{M}` et tous les autres coefficients sont
   nuls.

Cette factorisation est appelée **la décomposition en valeurs
singulières** de :math:`\mathbf{M}`. **Important.** Si la matrice
:math:`\mathbf{M}` est de rang :math:`r`, alors

-  | les :math:`r` premières colonnes de :math:`\mathbf{U}` sont les
     vecteurs singuliers à gauche de :math:`\mathbf{M}`

-  les :math:`r` premières colonnes de :math:`\mathbf{V}` sont les
   vecteurs singuliers à droite de :math:`\mathbf{M}`

-  les :math:`r` premiers coefficients strictement positifs de la
   diagonale de :math:`\mathbf{\Sigma}` sont les valeurs singulières de
   :math:`\mathbf{M}` et tous les autres coefficients sont nuls.

| **Produit scalaire et normes vectorielles.** Soit :math:`V` un espace
  vectoriel sur :math:`\mathbb{R}`.
| On appelle produit scalaire sur :math:`V` toute application

.. math::


   \begin{aligned}
       \big{<}.,.\big{>}:\quad &V\times V\rightarrow{\mathbb{R}}\\
       &(\mathbf{u},\mathbf{v})\mapsto \big{<}\mathbf{u},\mathbf{v}\big{>}, \end{aligned}

telle que,
:math:`\forall ( \lambda_1, \lambda_2, \mathbf{u}, \mathbf{v}, \mathbf{w}) \in \mathbb{R}\times\mathbb{R}\times V\times V \times V,`

-  :math:`\langle\mathbf{u}, \mathbf{v}\rangle = \langle\mathbf{v}, \mathbf{u}\rangle`\ (symétrie)

-  

   1. :math:`\langle\lambda_1 \mathbf{u}+\lambda_2 \mathbf{v}, \mathbf{w}\rangle = \lambda_1\langle \mathbf{u},\mathbf{w}\rangle +\lambda_2\langle \mathbf{v},\mathbf{w}\rangle`
      (linéarité à gauche)

   2. :math:`\langle\mathbf{u}, \lambda_1 \mathbf{v}+\lambda_2 \mathbf{w}\rangle = \lambda_1\langle \mathbf{u},\mathbf{v}\rangle +\lambda_2\langle \mathbf{u},\mathbf{w}\rangle`
      (linéarité à droite)

-  :math:`\langle\mathbf{u}, \mathbf{u}\rangle \geq 0 \qquad` (positive)

-  :math:`\langle\mathbf{u}, \mathbf{u}\rangle = 0 \implies \mathbf{u}=0 \qquad`
   (définie)

.. math::


   \begin{aligned}
       \|.\|: \quad&V\rightarrow{\mathbb{R_{+}}}\\
       &\mathbf{v}\mapsto \|\mathbf{v}\|\end{aligned}

| :math:`V`
  :math:`\forall\  (\lambda, \mathbf{u}, \mathbf{v})\in \mathbb{R}\times V\times V`

-  :math:`\|\lambda\mathbf{u}\| = |\lambda| \times \|\mathbf{u}\|`

-  :math:`\|\mathbf{u} + \mathbf{v} \| \leq \|\mathbf{u}\| + \|\mathbf{u}\| + \|v\|`\ (inégalité
   triangulaire)

**Remarque 2** Si :math:`\big{<}.,.\big{>}` est un produit scalaire sur
:math:`V`, alors :math:`\big{<}.,.\big{>}` induit une norme sur
:math:`V`. En effet,

| 

  .. math::


     \begin{aligned}
         \|.\|_{\big{<}.,.\big{>}}:\quad&V\rightarrow{\mathbb{R_{+}}}\\
         & \mathbf{u}\mapsto \|\mathbf{u}\|=\sqrt{\big{<}\mathbf{u},\mathbf{u}\big{>}}\end{aligned}
| **Exemples de normes et produits scalaires.**
| Prenons :math:`V=\mathbb{R}^n`.
| :math:`\bullet` Les applications

  .. math::

     \begin{aligned}
         \rho:\quad &V\times V\rightarrow{\mathbb{R}}\\
         &(\mathbf{u},\mathbf{v})\mapsto \sum_{i=1}^{n}u_iv_i ,\end{aligned}

| et

  .. math::

     \begin{aligned}
         \mu:\quad &V\rightarrow{\mathbb{R}_+}\\
         &\mathbf{u}\mapsto \sqrt{\sum_{i=1}^{n}u_i^2},\end{aligned}

  \ sont respectivement un produit scalaire et une norme sur :math:`V`.
  Il faut remarquer que
  :math:`\forall\  \mathbf{u} \in V, \quad \mu(\mathbf{u})=\sqrt{\rho(\mathbf{u},\mathbf{u})}`.
| :math:`\bullet` Pour tout :math:`p\in \mathbb{N}^*`, l’application

  .. math::

     \begin{aligned}
         \mu_p:\quad &V\rightarrow{\mathbb{R}_+}\\
         &\mathbf{u}\mapsto \bigg{(}\sum_{i=1}^{n}|u_i|^p\bigg{)}^{\frac{1}{p}},\end{aligned}

  est une norme sur :math:`V` appelée norme :math:`p`.
| Dans le cas :math:`p=2`, on retrouve la norme :math:`\mu` ci-dessus
  appelée norme euclidienne.

| **Remarque 3.** Un espace vectoriel muni d’une norme est appelé
  **espace vectoriel normé**.
| **Notion de distance.**
| Soit :math:`E` un ensemble non vide. Toute application
  :math:`d:E \times E \rightarrow \mathbb{R}_{+}` qui satisfait pour
  tout :math:`x, y, z \in E`:

  .. math::

     \begin{aligned}
         &\bullet \quad d(x,y) = d(y,x) \text{ (symétrie)}\\
         &\bullet \quad d(x,y) = 0 \Longrightarrow x=y\text{ (séparation)}\\
         &\bullet \quad d(x,y) \le d(x,z)+d(z,y) \text{ (inégalité triangulaire)}\end{aligned}

Exemples de distances.
^^^^^^^^^^^^^^^^^^^^^^

:math:`\bullet`

.. math::

   \begin{aligned}
       d:\quad &\mathbb{R}^n\times \mathbb{R}^{n}\rightarrow{\mathbb{R}_+}\nonumber\\
       &(\mathbf{u}, \mathbf{v})\mapsto \bigg{(}\sum_{i=1}^{n}|u_i-v_i|\bigg{)}.
       \end{aligned}

\ :math:`\bullet`

.. math::

   \begin{aligned}
       d:\quad &\mathbb{R}^n\times \mathbb{R}^n\rightarrow{\mathbb{R}_+}\nonumber \\
       &(\mathbf{u}, \mathbf{v})\mapsto \bigg{(}\sum_{i=1}^{n}|u_i-v_i|^2\bigg{)}^{\frac{1}{2}}.
       \end{aligned}

| :math:`\bullet` C’est la généralisation de la distance euclidienne et
  de la distance de Manhattan

  .. math::

     \begin{aligned}
         d_{Minkowski}:\quad &\mathbb{R}^n\times \mathbb{R}^n\rightarrow{\mathbb{R}_+}\nonumber \\
         &(\mathbf{u}, \mathbf{v})\mapsto \bigg{(}\sum_{i=1}^{n}|u_i-v_i|^p\bigg{)}^{\frac{1}{p}}, p\ge 1. \end{aligned}

  \ **Espaces métriques.**
| **Définition.** Un **espace métrique** est un ensemble :math:`E` muni
  d’une distance :math:`d`; on écrit :math:`(E, d)`.
| **Remarque 4.** Tout espace vectoriel normé est un espace métrique.
| **Suites dans un espace métrique.**
| Soit :math:`(E,d)` un espace métrique. On appelle **suite**
  (d’éléments de :math:`E`) et on note :math:`(u_n)_{n\in I}` ou
  :math:`(u)_n` une application:

.. math::


   \begin{aligned}
       u: \quad& I \rightarrow E\\
       & n \mapsto u(n):=u_n\end{aligned}

\ où :math:`I` est une partie infinie de :math:`\mathbb{N}`. On dit que
la suite :math:`(u)_n` converge vers :math:`u^*\in E` si pour tout
:math:`\epsilon>0` il existe :math:`N \in \mathbb{N}` tels que:

.. math::

   \begin{aligned}
       \forall\  n\in \mathbb{N}, \quad n>N \Longrightarrow d(u_n, u^*) < \epsilon\end{aligned}

En d’autres termes, la suite :math:`(u)_n` converge vers
:math:`u^*\in E` si pour tout :math:`\epsilon>0`, il existe un entier
:math:`N\in \mathbb{N}` tel que pour tout :math:`n>N`, :math:`u_n` est
contenu dans la boule :math:`\mathcal{B}_{\epsilon}` centrée en
:math:`u^*` et de rayon :math:`\epsilon`.

| **NB:** La suite :math:`(u)_n` à valeurs dans :math:`E` peut converger
  dans un ensemble autre que :math:`E`.
| **Définition.** La suite :math:`(u)_n` d’éléments de :math:`E` est
  dite de Cauchy si pour tout :math:`\epsilon>0`, il existe
  :math:`N\in\mathbb{N}` tel que:

.. math::


   \begin{aligned}
       \forall\  n>m \in \mathbb{N},\quad m>N \Longrightarrow d(u_n, u_m)<\epsilon.\end{aligned}

| Autrement dit, tous les termes :math:`u_n, u_m` d’une suite de Cauchy
  se rapprochent de plus en plus lorsque :math:`n` et :math:`m` sont
  suffisamment grands.
| **Espaces métriques complets.**
| **Définition.** Un espace métrique :math:`(E,d)` est dit **complet**
  si toute suite de Cauchy de :math:`E` converge dans :math:`E`.
| Un espace métrique complet est appelé **espace de Banach**.

Calcul du gradient (dérivation).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Fonction réelle.**
| **Définition.**
| Soit :math:`f: J\rightarrow \mathbb{R}` une fonction, avec :math:`J`
  un intervalle ouvert de :math:`\mathbb{R}`.
| On dit que :math:`f` est **dérivable** en :math:`a\in J` si la limite:

.. math::


   \begin{aligned}
       \lim_{h\rightarrow 0} \frac{f(a+h)-f(a)}{h} \text{ est finie.}
   \end{aligned}

| Si :math:`f` est dérivable en :math:`a`, la dérivée de :math:`f` en
  :math:`a` est notée :math:`f'(a).` La fonction dérivée de :math:`f`
  est notée :math:`f'` ou :math:`\frac{\mathrm{d}f}{\mathrm{d}x}` ou
  :math:`\mathrm{d}f`.
| **Exemple de dérivées.**

-  | **Fonctions polynomiales.**
   | La dérivée de la fonction
     :math:`f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots + a_1x+a_0`, avec les
     :math:`a_i` des constantes, est
     :math:`f'(x)=na_nx^{n-1}+(n-1)a_{n-1}x^{n-2}+\dots+a_1`.

-  | **Fonction exponentielle de base :math:`e`**.
   | La dérivée de la fonction :math:`f(x)=\exp(x)` est la fonction
     :math:`f` elle-même, i.e,
     :math:`\frac{\mathrm{d}\exp}{\mathrm{d}x}(x)=\exp(x)`.

-  | **Fonctions trigonométriques.**
   | :math:`\frac{\mathrm{d}\cos}{\mathrm{d}x}( x)=-\sin x` et
     :math:`\frac{\mathrm{d} \sin}{dx}(x)=\cos x`.

-  | **Fonction logarithme népérien**.
   | :math:`\frac{\mathrm{d} \ln}{\mathrm{d}x} (x) = \frac{1}{x}`.

| **Propriétés.**
| Soient :math:`J\subseteq \mathbb{R}` un intervalle ouvert,
  :math:`u,\ v\ : J\rightarrow \mathbb{R}` deux fonctions et
  :math:`\lambda \in \mathbb{R}`. Alors on a les propriétés suivantes de
  la dérivée:

1. | :math:`(u+v)' = u'+v'`

2. | :math:`(uv)' = uv'+u'v`

3. :math:`(\lambda u)' = \lambda u'`

| Ces propriétés s’étendent aux fonctions vectorielles en dimension
  supérieure.
| **Fonctions vectorielles.**
| Soit :math:`f: \mathcal{O}\rightarrow \mathbb{R}^p` une fonction, avec
  :math:`\mathcal{O}` une partie ouverte de
  :math:`\mathbb{R}^n, n, p\ge 1`.
| On dit que :math:`f` est **différentiable** (au sens de Fréchet) en
  :math:`\mathbf{a}\in \mathcal{O}`, s’il existe une application
  linéaire continue :math:`L: \mathbb{R}^n\rightarrow \mathbb{R}^p`
  telle que pour tout :math:`h\in \mathbb{R}^n`, on a

  .. math::

     \begin{aligned}
         \lim_{h\rightarrow 0} \frac{f(\mathbf{a}+h)-f(\mathbf{a})-L(h)}{\|h\|}=0.\end{aligned}

  Si :math:`f` est différentiable en tout point de :math:`\mathcal{O}`,
  on dit que :math:`f` est différentiable sur :math:`\mathcal{O}`.
| La différentielle de :math:`f` est notée :math:`Df`.
| **Dérivées partielles.**
| Soient
  :math:`\mathbf{a}=\begin{bmatrix} a_1\\ a_2\\ \vdots \\ a_n \end{bmatrix}\in \mathcal{O}\subseteq{\mathbb{R}^n}`
  et :math:`f: \mathcal{O}\rightarrow \mathbb{R}^p` une fonction.
| On dit que :math:`f` admet une dérivée partielle par rapport à la
  :math:`j-ème` variable :math:`x_j` si la limite:

  .. math::

     \begin{aligned}
         \lim_{h\rightarrow 0}\frac{f(a_1, a_2, \dots, a_j+h, \dots, a_n)-f(\mathbf{a})}{h} \text{ est finie.}\end{aligned}

  La dérivée partielle par rapport à la variable :math:`x_j` de
  :math:`f` en :math:`\mathbf{a}` est notée
  :math:`\frac{\partial f}{\partial x_j}(\mathbf{a})`.
| **Note.** Si :math:`f` est différentiable, alors :math:`f` admet des
  dérivées partielles par rapport à toutes les variables.
| **Gradient et Matrice Jacobienne.** Soit
  :math:`f: \mathcal{O}\subseteq\mathbb{R}^n \rightarrow \mathbb{R}^p`
  une fonction différentiable.
| On suppose que les fonctions composantes de :math:`f` sont
  :math:`f_1, f_2, \dots, f_p`.
| Alors la matrice des dérivées partielles

  .. math::

     \begin{bmatrix}
     \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} &\dots & \frac{\partial f_1}{\partial x_n}\\[0.2cm]
     \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} &\dots & \frac{\partial f_2}{\partial x_n}\\
     \vdots&\vdots& & \vdots\\\vspace{0.2cm}
     \frac{\partial f_p}{\partial x_1} & \frac{\partial f_p}{\partial x_2} &\dots & \frac{\partial f_p}{\partial x_n}
     \end{bmatrix}

  \ est appelée la **matrice jacobienne** de :math:`f`, notée
  :math:`\mathbf{J}_f` ou :math:`\mathbf{J}(f)`.
| Dans le cas :math:`p=1`, le vecteur
  :math:`\begin{bmatrix} \frac{\partial f}{\partial x_1} \\[0.2cm] \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}`
  est appelé :math:`\operatorname{\mathbf{gradient}}` de :math:`f` et
  noté :math:`\mathbf{\nabla} f` ou
  :math:`\operatorname{\mathbf{grad}}(f)`.
| **Exemples du calcul de dérivées et de gradients sur
  :math:`\mathbb{R}^n`.**

-  | :math:`f(\mathbf{x})=\big{<}\mathbf{x},\mathbf{x}\big{>}=\mathbf{x}^T\mathbf{x}`.
     Le gradient de :math:`f` est
     :math:`\nabla f(\mathbf{x})=2\mathbf{x}`

-  | :math:`f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}`, avec
     :math:`\mathbf{A}` une matrice et :math:`\mathbf{b}` un vecteur. On
     a :math:`Df(\mathbf{x})=\mathbf{A}.`

Dérivées de fonctions composées.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Il existe souvent des fonctions dont le gradient ne peut facilement
  être calculé en utilisant les formules précédentes. Pour trouver le
  gradient d’une telle fonction, on va réécrire la fonction comme étant
  une composition de fonctions dont le gradient est facile à calculer en
  utilisant les techniques que nous allons introduire. Dans cette partie
  nous allons présenter trois formules de dérivation de fonctions
  composées.
| **Composition de fonctions à une seule variable.**
| Soit :math:`f,g,h: \mathbb{R}\rightarrow\mathbb{R}`, trois fonctions
  réelles telles que :math:`f(x) = g(h(x))`.

  .. math:: \frac{\mathrm{d} f}{\mathrm{d} x} = \frac{\mathrm{d} g}{\mathrm{d} h}\frac{\mathrm{d} h}{\mathrm{d} x}

  **Formule de dérivée totale.**
| Soit :math:`f:\mathbb{R}^{n+1}\rightarrow\mathbb{R}` telle que
  :math:`f = f(x,u_1(x),\dots,u_n(x))` avec
  :math:`u_i:\mathbb{R}\rightarrow\mathbb{R}` alors

  .. math:: \frac{\mathrm{d} f\left(x, u_{1}, \ldots, u_{n}\right)}{\mathrm{d} x}=\frac{\partial f}{\partial x}+\frac{\partial f}{\partial u_{1}} \frac{\mathrm{d} u_{1}}{\mathrm{d} x}+\frac{\partial f}{\partial u_{2}} \frac{\mathrm{d} u_{2}}{\mathrm{d} x}+\ldots+\frac{\partial f}{\partial u_{n}} \frac{\mathrm{d} u_{n}}{\mathrm{d} x}=\frac{\partial f}{\partial x}+\sum_{i=1}^{n} \frac{\partial f}{\partial u_{i}} \frac{\mathrm{d} u_{i}}{\mathrm{d} x}.

| **Formule générale de dérivées de fonctions composées.**
| Soit

  .. math::

     \begin{array}{l}
     f :\mathbb{R}^{k} \rightarrow\mathbb{R}^{m} \\
     \mathbf{x} \mapsto f(\mathbf{x})
     \end{array}
     \begin{array}{l}
     g :\mathbb{R}^{n} \rightarrow\mathbb{R}^{k} \\
     \mathbf{x} \mapsto g(\mathbf{x})
     \end{array}

  \ où :math:`\mathbf{x}=(x_1,\dots,x_n)` ,
  :math:`f(\mathbf{x}) = (f_1(\mathbf{x}),\dots,f_m(\mathbf{x}))` et
  :math:`g(\mathbf{x}) = (g_1(\mathbf{x}),\dots,g_k(\mathbf{x}))`.

Le gradient de :math:`f(g(\mathbf{x}))` est défini comme suit:

.. math::


   \frac{\partial}{\partial \mathbf{x}} \mathbf{f}(\mathbf{g}(\mathbf{x}))=\left[\begin{array}{cccc}
   \frac{\partial f_{1}}{\partial g_{1}} & \frac{\partial f_{1}}{\partial g_{2}} & \ldots & \frac{\partial f_{1}}{\partial g_{k}} \\
   \frac{\partial f_{2}}{\partial g_{1}} & \frac{\partial f_{2}}{\partial g_{2}} & \cdots & \frac{\partial f_{2}}{\partial g_{k}} \\
   \vdots &\vdots & \ddots & \vdots \\
   \frac{\partial f_{m}}{\partial g_{1}} & \frac{\partial f_{m}}{\partial g_{2}} & \ldots & \frac{\partial f_{m}}{\partial g_{k}}
   \end{array}\right]\left[\begin{array}{cccc}
   \frac{\partial g_{1}}{\partial x_{1}} & \frac{\partial g_{1}}{\partial x_{2}} & \ldots & \frac{\partial g_{1}}{\partial x_{n}} \\
   \frac{\partial g_{2}}{\partial x_{1}} & \frac{\partial g_{2}}{\partial x_{2}} & \cdots & \frac{\partial g_{2}}{\partial x_{n}} \\
   \vdots &\vdots & \ddots & \vdots \\
   \frac{\partial g_{k}}{\partial x_{1}} & \frac{\partial g_{k}}{\partial x_{2}} & \cdots & \frac{\partial g_{k}}{\partial x_{n}}
   \end{array}\right]

Probabilités
~~~~~~~~~~~~

| La théorie des probabilités constitue un outil fondamental dans
  l’apprentissage automatique. Les probabilités vont nous servir à
  modéliser une expérience aléatoire, c’est-à-dire un phénomène dont on
  ne peut pas prédire l’issue avec certitude, et pour lequel on décide
  que le dénouement sera le fait du hasard.
| **Définition.**
| Une probabilité est une application sur :math:`\mathcal{P}(\Omega),`
  l’ensemble des parties de :math:`\Omega` telle que:

-  :math:`0 \leq \operatorname{\mathbb{P}}(A) \leq 1,` pour tout
   événement :math:`A \subseteq \Omega`;

-  :math:`\operatorname{\mathbb{P}}(A)=\sum_{\{\omega\} \in A} \operatorname{\mathbb{P}}(\omega),`
   pour tout événement :math:`A`;

-  :math:`\operatorname{\mathbb{P}}(\Omega)=\sum_{A_{i}} \operatorname{\mathbb{P}}(A_{i})=1,`
   avec les :math:`A_{i} \subseteq \Omega` une partition de
   :math:`\Omega`.

**Proposition.** Soient :math:`A` et :math:`B` deux événements,

1. :math:`\operatorname{Si} A` et :math:`B` sont incompatibles,
   :math:`\operatorname{\mathbb{P}}(A \cup B)=\operatorname{\mathbb{P}}(A)+\operatorname{\mathbb{P}}(B).`

2. :math:`\operatorname{\mathbb{P}}\left(A^{c}\right)=1-\operatorname{\mathbb{P}}(A)`,
   avec :math:`A^{c}` le complémentaire de :math:`A`.

3. :math:`\operatorname{\mathbb{P}}(\emptyset)=0.`

4. :math:`\operatorname{\mathbb{P}}(A \cup B)=\operatorname{\mathbb{P}}(A)+\operatorname{\mathbb{P}}(B)-\operatorname{\mathbb{P}}(A \cap B).`

| Preuve voir [@epardoux]
| Ci-dessous une définition plus générale de probabilité, valable pour
  des espaces des événements possibles non dénombrables.
| **Définition.** Soit :math:`A` une expérience alátoire et
  :math:`\Omega` l’espace des événements possibles associés. Une
  probabilité sur :math:`\Omega` est une application définie sur
  l’ensemble des événements, qui vérifie:

::: {.center}

-  **Axiome 1:** :math:`0\leq \operatorname{\mathbb{P}}(A)\leq 1`, pour
   tout événement :math:`A`;

-  **Axiome 2:** Pour toute suite d’événements
   :math:`(A_i)_{i\in \operatorname{\mathbf{N}}}`, deux à deux
   incompatibles,

   .. math:: \operatorname{\mathbb{P}}\left(\bigcup_{i \in \operatorname{\mathbf{N}}} A_{i}\right)=\sum_{i \in \operatorname{\mathbf{N}}} \operatorname{\mathbb{P}}\left(A_{i}\right);

-  **Axiome 3:** :math:`\operatorname{\mathbb{P}}(\Omega) = 1.` :::

:math:`\mathrm{NB}:` Les événements
:math:`\left(A_{i}\right)_{i \in \operatorname{\mathbf{N}}}` sont deux à
deux incompatibles, si pour tous
:math:`i \neq j, A_{i} \cap A_{j}=\emptyset`.

Indépendance et conditionnement.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Motivation.**
| Quelle est la probablité d’avoir un cancer du poumon?
| Information supplémentaire: vous fumez une vingtaine de cigarettes par
  jour. Cette information va changer la probabilité. L’outil qui permet
  cette mise à jour est la probabilité conditionnelle.
| **Définition.**
| Étant donnés deux événements :math:`A` et :math:`B`, avec
  :math:`\operatorname{\mathbb{P}}(A) > 0`, on appelle probabilité de
  :math:`B` conditionnellement à :math:`A`, ou sachant :math:`A,` la
  probabilité notée :math:`\operatorname{\mathbb{P}}(B \mid A)` définie
  par:

| 

  .. math::


     \operatorname{\mathbb{P}}(B \mid A)=\frac{\operatorname{\mathbb{P}}(A \cap B)}{\mathbb{P}(A)}.

  \ L’équation `[prob_condit] <#prob_condit>`__ peut aussi s’écrire
  comme :math:`\mathbb{P}(A \cap B)=\mathbb{P}(B \mid A) \mathbb{P}(A)`.
| De plus, la probabilité conditionnelle sachant :math:`A`, notée
  :math:`\mathbb{P}(. \mid A)` est une nouvelle probabilité et possède
  toutes les propriétés d’une probabilité.

| **Proposition.** Formule des probabilités totales généralisée
| Soit :math:`(A_i)_{i\in I}` (:math:`I` un ensemble fini d’indices) une
  partition de :math:`\Omega` telle que
  :math:`0 < \mathbb{P}(A_i)\leq 1 \quad\forall\  i\in I.` Pour tout
  événement B, on a

  .. math:: \mathbb{P}(B)=\sum_{i \in I} \mathbb{P}\left(B|A_{i}\right)\mathbb{P}\left(A_{i}\right).

  La formule des probabilités totales permet de servir les étapes de
  l’expérience aléatoire dans l’ordre chronologique. **Proposition.**
  Formule de Bayes généralisée
| Soit :math:`(A_i)_{i\in I}` une partition de :math:`\Omega` tel que
  :math:`0\leq \mathbb{P}(A_{i})\leq 1,\forall\  i\in I`. Soit un
  événement :math:`B`, tel que :math:`\mathbb{P}(B)>0`. Alors pour tout
  :math:`i\in I`,

  .. math::

     \mathbb{P}(A_{i}|B)=\frac{ \mathbb{P}\left(B|A_{i}\right)\mathbb{P}\left(A_{i}\right)}{\sum_{i \in I} \mathbb{P}\left(B|A_{i}\right)\mathbb{P}\left(A_{i}\right)}.

| **Définition.**
| Deux événements :math:`A` et :math:`B` sont dits **indépendants** si

  .. math:: \mathbb{P}(A\cap B) = \mathbb{P}(A)\mathbb{P}(B).

  \ S’ils sont de probabilité non nulle, alors

  .. math:: \mathbb{P}(B|A) = \mathbb{P}(B) \Leftrightarrow \mathbb{P}(A|B) = \mathbb{P}(A) \Leftrightarrow \mathbb{P}(A\cap B) = \mathbb{P}(A)\mathbb{P}(B).

Variables aléatoires.
^^^^^^^^^^^^^^^^^^^^^

| **Définition.**
| Une variable aléatoire (v.a) :math:`X` est une fonction définie sur
  l’espace fondamental :math:`\Omega`, qui associe une valeur numérique
  à chaque résultat de l’expérience aléatoire étudiée. Ainsi, à chaque
  événement élémentaire :math:`\omega`, on associe un nombre
  :math:`X(\omega)`.

Une variable qui ne prend qu’un nombre dénombrable de valeurs est dite
**discrète** (par exemple le résultat d’une lancée d’une pièce de
monnaie, ...), sinon, elle est dite **continue** (par exemple le prix
d’un produit sur le marché au fil du temps, distance de freinage d’une
voiture roulant à 100 km/h).

Variable aléatoire discrète
^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Définition.**
| L’espérance mathématique ou moyenne d’une v.a discrète :math:`X` est
  le réel

  .. math:: \mathbb{E}[X] = \sum_{k=0}^{\infty} k \mathbb{P}[X = k].

Pour toute fonction :math:`g`,

.. math:: \mathbb{E}[g(X)] = \sum_{k=0}^{\infty} g(k) \mathbb{P}[X = k].

| **Définition.**
| La variance d’une v.a discrète :math:`X` est le réel positif

.. math::


   Var[X] = \mathbb{E}\left[(X-\mathbb{E}[X])^2\right] = \sum_{k=0}^{\infty} \left(k-\mathbb{E}[X]\right)^2 \mathbb{P}[X = k] = \mathbb{E}[X^2] -
   \mathbb{E}[X]^2

\ et l’écart-type de :math:`X` est la racine carrée de sa variance. $$

| **Exemple:** Loi de Bernoulli
| La loi de Bernoulli est fondamentale pour la modélisation des
  problèmes de classification binaire en apprentissage automatique. On
  étudie que les expériences aléatoires qui n’ont que deux issues
  possibles (succès ou échec). Une expérience aléatoire de ce type est
  appelée une épreuve de Bernoulli. Elle se conclut par un succès si
  l’évènement auquel on s’intéresse est réalisé ou un échec sinon. On
  associe à cette épreuve une variable aléatoire :math:`Y` qui prend la
  valeur :math:`1` si l’évènement est réalisé et la valeur :math:`0`
  sinon. Cette v.a. ne prend donc que deux valeurs (:math:`0` et
  :math:`1`) et sa loi est donnée par :

  .. math:: \mathbb{P}[Y=1]=p, \quad \mathbb{P}[Y=0]=q=1-p.\qquad \operatorname{Avec } p \in [0, 1].

On dit alors que :math:`Y` suit une loi de Bernoulli de paramètre
:math:`p,` notée :math:`\mathcal{B}(p)`. La v.a. :math:`Y` a pour
espérance :math:`p` et pour variance :math:`p(1-p) .` En effet,

.. math:: \mathbb{E}[Y]=0 \times(1-p)+1 \times p=p

\ et

.. math:: \operatorname{Var}(Y)=\mathbb{E}\left[Y^{2}\right]-\mathbb{E}[Y]^{2}=\mathbb{E}[Y]-\mathbb{E}[Y]^{2}=p(1-p).

**Schéma de Bernoulli** :

-  Chaque épreuve a deux issues : succès :math:`[S]` ou échec
   :math:`[E]`.

-  Pour chaque épreuve, la probabilité d’un succès est la même, notons
   :math:`\mathbb{P}(S) = p` et :math:`\mathbb{P}(E) = q = 1 - p.`

-  Les :math:`n` épreuves sont **indépendantes** : la probabilité d’un
   succès ne varie pas, elle ne dépend pas des informations sur les
   résultats des autres épreuves.

Variable aléatoire continue
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contrairement aux v.a. discrètes, les v.a. continues sont utilisées pour
mesurer des grandeurs "continues" (comme distance, masse, pression...).
Une variable aléatoire continue est souvent définie par sa densité de
probabilité ou simplement densité. Une densité :math:`f` décrit la loi
d’une v.a :math:`X` en ce sens:

.. math:: \forall\  a,b \in \mathbb{R}, \quad \mathbb{P}[a\leq X \leq b] = \int_{a}^{b} f(x)dx

et

.. math:: \forall\  x\in \mathbb{R}, \quad F(x) = \mathbb{P}[X\leq x] =  \int_{-\infty}^{x} f(t)dt

. On en déduit qu’une densité doit vérifier

.. math:: \forall\  x\in \mathbb{R}, \quad f(x)\geq 0 \text{ et } \int_{\mathbb{R}}^{} f(x)dx = 1

.

| **Définition.**
| On appelle densité de probabilité toute fonction réelle positive,
  d’intégrale :math:`1`.

| **Définition.**
| L’espérance mathématiques de la v.a :math:`X` est définie par

  .. math:: \mathbb{E}[X]=\int_{\mathbb{R}}^{} xf(x)dx.

| **Exemple.** **La loi normale**
| C’est la loi de probabilité la plus importante. Son rôle est central
  dans de nombreux modèles probabilistes et en statistique. Elle possède
  des propriétés intéressantes qui la rendent agréable à utiliser. La
  densité d’une variable aléatoire suivant la loi normale de moyenne
  :math:`\mu` et d’écart-type :math:`\sigma`
  (:math:`\mathcal{N}(\mu,\sigma^2)`) est définie par

  .. math:: f(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad \forall\  x \in \mathbb{R}.

  Quand :math:`\mu=0 \quad \text{et} \quad \sigma = 1`, on parle de loi
  normale centrée et réduite.

Loi des grands nombres
^^^^^^^^^^^^^^^^^^^^^^

Considérons une suite :math:`\left(X_{n}\right)_{n \geq 1}` de v.a.
indépendantes et de même loi. Supposons que ces v.a. ont une espérance,
:math:`m` et une variance, :math:`\sigma^{2}`.

| **Théorème.**
| 

  .. math:: \mathbb{E}\left[\sum_{i=1}^{n} X_i\right] = nm

  .. math:: \operatorname{Var}\left[\sum_{i=1}^{n} X_i\right] = n\sigma^2

| **Définition.**
| La moyenne empirique des v.a. :math:`X_1,\dots,X_n` est la v.a.

  .. math:: \bar{X_n} = \frac{X_1+\dots + X_n}{n}.

  \ On sait d’ores et déjà que la moyenne empirique a pour espérance
  :math:`m` et pour variance :math:`\frac{\sigma^2}{n}`. Ainsi, plus
  :math:`n` est grand, moins cette v.a. varie. A la limite, quand
  :math:`n` tend vers l’infini, elle se concentre sur son espérance,
  :math:`m`. C’est la loi des grands nombres.

| **Théorème.** Convergence en Probabilité
| Quand :math:`n` est grand, :math:`\bar{X_n}` est proche de :math:`m`
  avec une forte probabilité. Autrement dit,
  :math:`\forall\ \varepsilon \ge 0, \quad \lim\limits\_{n\to\infty} \mathbb{P}(|\bar{X_n}-m|> \varepsilon) = 0.`

**Théorème central limite** Le Théorème central limite est très
important en apprentissage automatique. Il est souvent utilisé pour la
transformation des données surtout au traitement de données aberrantes.

| **Théorème.**
| Pour tous réels :math:`a<b`, quand :math:`n` tend vers
  :math:`+\infty`,

  .. math:: \mathbb{P}\left(a \leq \frac{\bar{X}_{n}-m}{\sigma / \sqrt{n}} \leq b\right) \longrightarrow \int_{a}^{b} \frac{1}{\sqrt{2 \pi}} e^{-x^{2} / 2} \mathrm{d} x.

  On dit que
  :math:`\displaystyle \frac{\bar{X}_{n}-m}{\sigma / \sqrt{n}}` converge
  en loi vers la loi normale :math:`\mathcal{N}(0,1)`.

Intervalles de confiance
^^^^^^^^^^^^^^^^^^^^^^^^

Soit :math:`X` un caractère (ou variable) étudié sur une population, de
moyenne :math:`m` et de variance :math:`\sigma^2`. On cherche ici à
donner une estimation de la moyenne :math:`m` de ce caractère, calculée
à partir de valeurs observées sur un échantillon
:math:`(X_1, ..., X_n)`. La fonction de l’échantillon qui estimera un
paramètre est appelée estimateur, son écart-type est appelé erreur
standard et est noté SE. L’estimateur de la moyenne :math:`m` est la
moyenne empirique:

.. math:: \frac{1}{n}\sum_{i=1}^{n} X_i

D’après les propriétés de la loi normale, avec un erreur
:math:`\alpha = 5\%` quand :math:`n` est grand on sait que

.. math:: \mathbb{P}\left[m-2\sigma/ \sqrt{n}\leq \bar{X_n}\leq m+2\sigma/ \sqrt{n}\right] = 1- \alpha = 0.954

| ou, de manière équivalente,

  .. math:: \mathbb{P}\left[\bar{X_n}-2\sigma/ \sqrt{n}\leq m\leq \bar{X_n}+2\sigma/ \sqrt{n}\right] = 1- \alpha = 0.954

  Ce qui peut se traduire ainsi: quand on estime :math:`m` par
  :math:`\bar{X_n}`, l’erreur faite est inférieure à
  :math:`2\sigma/ \sqrt{n}`, pour :math:`95,4\%` des échantillons. Ou
  avec une probabilité de :math:`95,4\%`, la moyenne inconnue :math:`m`
  est dans l’intervalle
  :math:`\left[\bar{X_n}-2\sigma/ \sqrt{n},\ \bar{X_n}+2\sigma/ \sqrt{n}\right]`.
| Voir [@estatML] pour plus d’explication.
| **Définition.**
| On peut associer à chaque incertitude :math:`\alpha`, un intervalle
  appelé intervalle de confiance de niveau de confiance
  :math:`1 - \alpha`, qui contient la vraie moyenne :math:`m` avec une
  probabilité égale à :math:`1 - \alpha`.

| **Définition.**
| Soit :math:`Z` une v.a.. Le fractile supérieur d’ordre :math:`\alpha`
  de la loi de :math:`Z` est le réel :math:`z` qui vérifie

  .. math:: \mathbb{P}\left[Z\geq z\right] = \alpha

  \ Le fractile inférieur d’ordre :math:`\alpha` de la loi :math:`Z` est
  le réel :math:`z` qui vérifie

  .. math:: \mathbb{P}\left[Z\leq z\right] = \alpha.

  Quand l’écart-type théorique de la loi du caractère :math:`X` étudié
  n’est pas connu, on l’éstime par l’écart-type empirique
  :math:`s_{n-1}`. Comme on dispose d’un grand échantillon, l’erreur
  commise est petite. L’intervalle de confiance, de niveau de confiance
  :math:`1-\alpha` devient :

  .. math:: \left[\bar{x}_{n}-z_{\alpha / 2} \frac{s_{n-1}}{\sqrt{n}}, \ \bar{x}_{n}+z_{\alpha / 2} \frac{s_{n-1}}{\sqrt{n}}\right]

  où

  .. math:: s_{n-1}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}.

Estimations paramétriques
~~~~~~~~~~~~~~~~~~~~~~~~~

| Soit :math:`(\Omega,\mathcal{A},\mathbf{P})` un espace probabilisé et
  :math:`\mathbf{x}` une :math:`v.a.` de :math:`(\Omega,\mathcal{A})`
  dans :math:`(E,\mathcal{E})`. La donnée d’un modèle statistique c’est
  la donnée d’une famille de probabilités sur :math:`(E,\mathcal{E})`,
  :math:`\{\mathbb{P}_{\theta},\theta\in\Theta\}`. Le modèle étant
  donné, on suppose alors que la loi de :math:`\mathbf{x}` appartient au
  modèle :math:`\{\mathbf{P}_{\theta},\theta\in\Theta\}`. Par exemple
  dans le modèle de Bernoulli, :math:`\mathbf{x} = (x_1,\dots,x_n)` où
  les :math:`x_i` sont :math:`i.i.d.` (indépendantes et identiquement
  distribuées) de loi de Bernoulli de paramètre
  :math:`\theta\in\left]0,1\right]`. :math:`E = \{0,1\}^n`,
  :math:`\mathcal{E} = \mathcal{P}(E)`,
  :math:`\Theta = \left]0,1\right]` et
  :math:`P_{\theta}=\left((1-\theta) \delta_{0}+\theta \delta_{1}\right)^{\otimes n}.`
| **Définition.**
| On dit que le modèle
  :math:`\left\{\mathbb{P}_{\theta},\theta\in\Theta\right\}` est
  identifiable si l’application

  .. math::

     \begin{array}{l}
             \Theta \rightarrow\left\{P_{\theta}, \theta \in \Theta\right\} \\
             \theta \mapsto P_{\theta}
         \end{array}

  \ est injective.

| **Définition.**
| Soit :math:`g:\  \Theta\rightarrow\mathbb{R}^k`. On appelle estimateur
  de :math:`g(\theta)` au vu de l’observation :math:`x`, toute
  application :math:`T : \Omega\rightarrow \mathbb{R}^k` de la forme
  :math:`T = h(x)` où :math:`h : E\mapsto\mathbb{R}^k` mesurable. Un
  estimateur ne doit pas dépendre de la quantité :math:`g(\theta)` que
  l’on cherche à estimer. On introduit les propriètés suivantes d’un
  estimateur.
| **Définition.**
| :math:`T` est un estimateur sans biais de :math:`g(\theta)` si pour
  tout
  :math:`\theta \in\Theta,\quad \mathbb{E}_{\theta}[T] = g(\theta)`.

Dans le cas contraire, on dit que l’estimateur :math:`T` est biaisé et
on appelle biais la quantité :math:`\mathbb{E}_{\theta}[T] - g(\theta)`.

Généralement :math:`\mathbf{x}` est un vecteur
:math:`\left(x_{1}, \ldots, x_{n}\right)` d’observations :math:`(n`
étant le nombre d’entre elles). Un exemple important est le cas où
:math:`x_{1},\ldots, x_{n}` forme un :math:`n`-échantillon c’est à dire
lorsque que :math:`x_{1}, \ldots, x_{n}` sont i.i.d. On peut alors
regarder des propriétés asymptotiques de l’estimateur, c’est-à-dire en
faisant tendre le nombre d’observations :math:`n` vers :math:`+\infty`.
Dans ce cas, il est naturel de noter :math:`T = T_n` comme dépendant de
:math:`n`. On a alors la définition suivante :

**Définition.**

:math:`T_n` est un estimateur consistant de :math:`g(\theta)` si pour
tout :math:`\theta \in \Theta`, :math:`T_n` converge en probabilité vers
:math:`g(\theta)` sous :math:`P_{\theta}` lorsque :math:`n\to\infty`.

| On définit le risque quadratique de l’estimateur dans le cas où
  :math:`g(\theta)\in\mathbb{R}`.
| **Définition.**
| Soit :math:`T_n` un estimateur de :math:`g(\theta)`. Le risque
  quadratique de :math:`T_n` est défini par

  .. math:: R(T_n,g(\theta)) = \mathbb{E}_{\theta}[(T_n - g(\theta))^2].

Estimation par la méthode des moments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Considérons un échantillon :math:`\mathbf{x} = (x_1,\dots,x_n)`. Soit
:math:`f = (f_1,\dots,f_k)` une application de :math:`\mathcal{X}` dans
:math:`\mathbb{R}^k` tel que le modèle
:math:`\{\mathbb{P}_{\theta},\theta\in\Theta\}` est identifiable si
l’application :math:`\Phi`

.. math::


   \begin{array}{l}
   \Phi: ~\Theta \rightarrow \mathbb{R}^k \\
   \quad ~~~\theta \mapsto \Phi(\theta) = \mathbb{E}_{\theta}[f(x)]
   \end{array}

est injective. On définit l’estimateur :math:`\hat{\theta}_n` comme la
solution dans :math:`\Theta` (quand elle existe) de l’équation

.. math:: \mathbb{E}_{\theta}[f(\mathbf{x})]\approx \frac{1}{n}\sum_{i=1}^{n} f(x_i).

Souvent, lorsque :math:`\mathcal{X}\subset \mathbb{R},` on prend
:math:`f_i(x) = x^i` et :math:`\Phi` correspond donc au ième moment de
la variable de :math:`X_i` sous :math:`\mathbb{P}_{\theta}`. Ce choix
justifie le nom donné à la méthode. Voici quelques exemples
d’estimateurs bâtis sur cette méthode.

| **Exemple.** Loi uniforme
| Ici :math:`k=1`, :math:`Q_{\theta}` est la loi uniforme sur
  :math:`[0,\theta]` avec :math:`\theta > 0`. On a pour tout
  :math:`\theta`,
  :math:`\displaystyle \mathbb{E}_{\theta}[X_1] = \frac{\theta}{2}`, on
  peut donc prendre par exemple
  :math:`\displaystyle \Phi(\theta) = \frac{\theta}{2}` et
  :math:`f(x) = x`. L’estimateur obtenu par la méthode des moments est
  alors :math:`\hat{\theta}_n =2\bar{X_n}`. Cet estimateur est sans
  biais et constant.
| **Exemple.** Loi normale
| Ici :math:`k=2`, on prend :math:`Q_{\theta} = \mathcal{N}(m,\sigma^2)`
  avec
  :math:`\theta = (m,\sigma^2)\in\mathbb{R}\times\mathbb{R}_{+}^{*}`.
  Pour tout :math:`\theta`, :math:`\mathbb{E}_{\theta}[X_1] = m` et
  :math:`\mathbb{E}_{\theta}[X_1^2] = m^2 + \sigma^2` , on peut donc
  prendre par exemple, :math:`f_1(x) = x` et :math:`f_2(x) = x^2` ce qui
  donne :math:`\Phi(m,\ \sigma^2) = (m,m^2+\sigma^2)`. L’estimateur
  obtenu par la méthode des moments vérifie

  .. math:: \hat{m}_{n}=\bar{X}_{n} \text { et } \hat{m}_{n}^{2}+\hat{\sigma}_{n}^2=\frac{1}{n} \sum_{i=1}^{n} X_{i}^{2},

  c’est-à-dire

  .. math:: \hat{\theta}_{n}=\left(\bar{X}_{n},\ \frac{1}{n} \sum_{i=1}^{n}\left(X_{i}-\bar{X}_{n}\right)^{2}\right).

  L’estimateur est consistant mais l’estimateur de la variance est
  biaisé.

Estimation par maximum de vraisemblance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Soit :math:`\{E,\ \mathcal{E},\ \{P_{\theta},\ \theta\in\Theta\}\}` un
  modèle statistique, où :math:`\Theta\subset\mathbb{R}^k`. On suppose
  qu’il existe une mesure :math:`\sigma`-finie :math:`\mu` qui domine le
  modèle, c’est à dire que :math:`\forall\  \theta\in\Theta`,
  :math:`P_{\theta}` admet une densité par rapport à :math:`\mu`.
| **Définition.**
| Soit :math:`\mathbf{x}` une observation. On appelle vraisemblance de
  :math:`\mathbf{x}` l’application

  .. math::

     \begin{array}{l}
         \Theta \rightarrow\mathbb{R}_+ \\
         \theta \mapsto \mathbb{P}(\theta,\ \mathbf{x})
         \end{array}

  \ On appelle estimateur du maximum de vraisemblance de :math:`\theta`,
  tout élément :math:`\hat{\theta}` de :math:`\Theta` maximisant la
  vraisemblance, c’est à dire vérifiant

  .. math:: \hat{\theta} = \arg \underset{\theta\in\Theta}{\max}\  \mathbf{P}(\theta,\ \mathbf{x})

Considérons le cas typique où
:math:`\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right),` les :math:`x_{i}`
formant un :math:`n`-échantillon de loi :math:`Q_{\theta_{0}}` où
:math:`Q_{\theta_{0}}` est une loi sur :math:`\mathcal{X}` de paramètre
inconnu :math:`\theta_{0} \in \Theta \subset` :math:`\mathbb{R}^{k} .`
On suppose en outre que pour tout :math:`\theta \in \Theta, Q_{\theta}`
est absolument continue par rapport à une mesure :math:`\nu` sur
:math:`\mathcal{X}`. Dans ce cas, en notant

.. math:: q(\theta, x)=\frac{d Q_{\theta}}{d \nu}(x)

et en prenant :math:`\mu=\nu^{\otimes n}` on a la vraisemblance qui
s’écrit sous la forme

.. math:: \mathbb{P}(\theta, \mathbf{x})=\prod_{i=1}^{n} q\left(\theta, x_{i}\right)

et donc

.. math:: \hat{\theta}_{n}=\arg \max _{\theta \in \Theta} \frac{1}{n} \sum_{i=1}^{n} \log \left[q\left(\theta, x_{i}\right)\right]

avec la convention :math:`\log (0)=-\infty .`

| **Exemple.** Modèle de Bernoulli
| Soit :math:`Q_{\theta_{0}}=\mathcal{B}(\theta)` avec
  :math:`\theta \in[0,1]=\Theta`. Pour tout :math:`\theta \in] 0,1[` et
  :math:`x \in\{0,1\}`

  .. math:: q(\theta, x)=\theta^{x}(1-\theta)^{1-x}=(1-\theta) \exp \left[x \log \left(\frac{\theta}{1-\theta}\right)\right]

  et donc l’estimateur du maximum de vraisemblance doit maximiser dans
  l’intervalle [0,1].

  .. math:: \log \left(\theta^{S_{n}}(1-\theta)^{n-S_{n}}\right)=S_{n} \log \left(\frac{\theta}{1-\theta}\right)+n \log (1-\theta)

  avec :math:`S_n = \sum_{i} x_i` ce qui conduit à
  :math:`\hat{\theta}_{n}=\bar{\mathbf{x}}` en résolvant l’équation
  :math:`\nabla \log(q(\theta, x)) = 0`.
