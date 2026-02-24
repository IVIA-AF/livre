(ch4)=
# Apprentissage Non-Supervisé

## Introduction et Motivations

Dans le chapitre précedent, nous avons discuté des notions d'apprentissage supervisé. Dans ce type d'apprentissage, on a considéré des données étiquettées de la forme $\mathcal{D} =  \{ (\mathbf{x}_i, y_i), i = 1,\ldots, n \}$ où l'objectif consiste à trouver une modélisation $f$ telle qu'on ait l'approximation $y \simeq f(\mathbf{x})$, pour tout $(\mathbf{x}, y)\in \mathcal{D}$. Cependant, il est important de se demander ce qu'il en est du cas où l'on n'a pas d'étiquettes. En effet, d'après quelques [médias](https://interestingengineering.com/number-of-cameras-across-the-world-will-reach-45-trillion-by-2022), il y a plus d'appareils photos que d'êtres humains, donc il y a une gigantesque quantité de données images dans le monde entier. On a aussi tant de données textes, et autres. Étiqueter toutes ces données est une tâche difficile. Pourtant, il y a certains types d'apprentissages qu'on peut effectuer sur de telles données. C'est ce qu'on appelle apprentissage non supervisé.

L'apprentissage non supervisé est un type d'apprentissage automatique pour lequel les donneés utilisées ne sont pas étiquettées. L'objectif de l'apprentissage est donc de découvrir les structures sous-jacentes à ces données. Un tel type d'apprentissage comprend des méthodes comme $K$-moyennes, le regroupement hiérarchique, les réduction de dimensions, ainsi que d'autres méthodes plus avancées dans les cas où ces données ne peuvent pas être linéarement separées (ce qui est souvent le cas en pratique). Ces méthodes ont d'importantes applications à savoir: les systèmes de recommandations, segmentation du marché, détection d'anomalies, imagèrie médicales, etc.

Dans un premier temps, nous allons voir quelques algorithmes d'apprentissage non supervisé, commençant par les algorithmes de régroupement ($K$-moyennes, regroupement hiérarchique), puis ceux de réduction de dimensions (Analyse en composantes principales et positionnement multidimensionnel), et nous allons finir par quelques applications de ces algorithmes.

## Les algorithmes de l'apprentissage non supervisé

Les algorithmes de l'apprentissage non supervisé sont principalement divisés en deux grands groupes, les algorithmes de partitionnement et les algorithmes de réduction de dimension. Dans ce qui suit, nous présenterons respectivement l'algorithme de partitionnement qui est le $K$-moyennes et les algorithmes de réduction: le positionnement multidimensionnel, et l'analyse à composantes principales. Nous devons noter que les algorithmes les plus populaires de l'apprentissage non supervisé sont le **$K$-moyennes** et l'**analyse en composantes principales**.

(algorithmes-de-partitionnement.)=
## Algorithmes de Partitionnement.

### $\textbf{K}$-moyennes

Dans une optique de regroupement des données en différentes catégories ou classes représentant les différents types de données, il est nécessaire d'utiliser des algorithmes spécifiques à l'instar de l'algorithme des K-moyennes. En effet, imaginons que nous avons un ensemble de données que nous souhaitons partitionner en trois catégories. Ces données présentent des catégories différentes et peuvent être regroupées selon leur similitude tel que décrite par la {ref}`fig-1`.

```{figure} images/datakmoyen.png
:name: fig-1
:alt: Représentation des données partitionnées en trois catégories

Représentation des données partitionnées en trois catégories
```


Idéalement l'intuition humaine peut nous permettre de détecter les regroupements pour le cas des données simples. Mais alors, est-il possible de demander à la machine si elle peut le faire à notre place, c'est -à-dire regrouper selon les trois catégories réquises.

**K-moyennes** est une méthode qui permet de regrouper les données en fonction du nombre de groupes $K$ qui lui a été recommandé. Elle comporte plusieurs étapes, à savoir:

- Étape 1: Sélectionner le nombre de groupe dont nous souhaitons identifier dans les données. Celui-ci représente le \"$K$\" dans l'expression $K$-moyen. Dans notre cas par exemple $K=3$ car nous souhaitons regrouper en groupe de 3. Notons aussi que $K$ est un paramètre qui n'est pas directement rélié aux données.

- Étape 2: Sélectionner aléatoirement 3 points différents dans nos données qui constitueront nos centroïde (regroupement initial).

- Étape 3: Mesurer la distance entre chaque point du données et nos 3 points initiaux (centroïde).

- Étape 4: Assigner à chaque point le regroupement correspondant au centroïde le plus proche.

- Étape 5: Calculer la moyenne de chaque regroupement (mise à jour de centroïde)

```{figure} images/kmean.png
:name: fig-application de k-moyen
:width: 90.0%
:alt: Application des K-moyennes

Application des <span class="math inline"><em>K</em></span>-moyennes
```


#### Comment choisir [la valeur de $K$?](https://blogs.oracle.com/datascience/introduction-to-k-means-clustering)

- En fonction des données, nous pouvons déterminer intuitivement la valeur de $K$.

- Nous pouvons également essayer différentes valeurs de $K$ en commençant par exemple par $K=1$ (ceci n'étant pas conseillé ), $K$=2, $K$=3, etc.

### Remarque

Il peut arriver que nos données soient complexes, de ce fait, nous devons utiliser des méthodes plus complexes que nous ne développerons pas dans cette partie, comme l'algorithme du **Kernel $K$-moyennes**.

#### K-moyennes: Algorithme

L'algorithme $K-$moyennes est un algorithme itératif qui essaie de partitionner l'ensemble de données en $K$ sous-groupes distincts non chevauchant prédéfinis ( i.e chaque point de données appartient à un seul groupe). Il essaie de rendre les points de données intra-groupe aussi similaires que possible tout en gardant les regroupements aussi différents (loin) que possible. Il attribue des points de données à un regroupement de telle sorte que la somme de la distance au carré entre les points de données et le centre de gravité du regroupement (moyenne arithmétique de tous les points de données appartenant à ce regroupement) soit minimale. Moins nous avons de variation au sein des regroupements, plus les points de données sont homogènes (similaires) au sein du même regroupement. [L'algorithme ](https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/)des $K$-moyennes peut être décrit tel que suit:

1.  Spécifier le nombre de regroupements $K$.

2.  Initialiser les centres de gravité en sélectionnant au hasard $K$ points de données pour les centres de gravité sans remplacement.

3.  Calculer la somme de la distance au carré entre les points de données et tous les centres de gravité.

4.  Attribuer chaque point de données au regroupement le plus proche (centroïde).

5.  Calculer les centres de gravité des regroupements en prenant la moyenne de tous les points de données appartenant à chaque groupe.

6.  Répéter les étapes $3, 4 \text{ et } 5$ jusqu'à ce qu'il n'y ait aucune modification des centres de gravité, c'est-à-dire que l'attribution des points de données aux regroupements ne change pas.

L'approche suivie par $K$-moyennes pour résoudre le problème est appelée Espérance - Maximisation (EM) qui se fait en deux étapes à savoir: le passage à **l'Espérance et la Maximisation**. En effet, l'étape de passage à l'Espérance consiste à affecter les points de données au regroupement le plus proche et l'étape de Maximisation calcule le centroïde de chaque regroupement. Vous trouverez ci-dessous une description de la façon dont nous pouvons le résoudre mathématiquement. Nous définissons la fonction objectif de la manière suivante: $$J = \sum_{i=1}^{m}\sum_{k=1}^{K}w_{ik}|| \textbf{x}_{i} - \boldsymbol{\nu}_{k}||^{2}.$$

où le poids $w_{ik} = 1$ si le point de données $\textbf{x}_i$ appartient au groupe $k$, sinon, $w_{ik}= 0$. De plus, $\nu_{k}$ est le centre de gravité du groupe $k$.

La fonction objectif $K$-moyennes est très populaire dans les applications pratiques du regroupement. Cependant, il s'avère que trouver la solution optimale des $K$-moyennes est souvent irréalisable par le calcul (le problème est NP-difficile). Comme alternative, l'algorithme itératif simple précèdent est souvent utilisé, si bien que, dans de nombreux cas, le terme de regroupement des $K$-moyennes fait référence au résultat de cet algorithme plutôt qu'au regroupement qui minimise le coût objectif des $K$-moyennes.

#### K-moyenne: cas pratique

Veuillez [Cliquer ici](https://drive.google.com/file/d/16Lg90qf5itSIlh-vEERdx8CDuKJHoICF/view?usp=sharing) pour avoir un aperçu de cas pratique écrit en Python.

## Réduction de dimension

Dans cette section, nous présenterons des méthodes ou algorithmes de réduction de dimension, à savoir, le positionnement multidimensionnel et l'analyse à composantes principales.

### Positionnement multidimensionnel (MDS en Anglais)

Le positionnement multidimensionnel, plus connu sous le nom de Multi-Dimensional Scaling (MDS) dans sa version anglaise est, d'après [wikipédia](https://fr.wikipedia.org/wiki/Positionnement_multidimensionnel), un ensemble de techniques statistiques utilisées dans le domaine de la visualisation d'information pour explorer les similarités dans les données. Il contient principalement trois méthodes qui sont: le positionnement multidimensionel classique, le positionnement multidimensionel métrique et le positionnement multidimensionel non métrique.

Pour les données utilisées dans les sections précedentes, les points de données étaient caractérisés par leurs coordonnées dans l'espace affine associé. Cependant, il existe des cas où les coordonnées explicites des points de données ne sont pas disponibles mais plutôt les distances entre chaque paire de points. L'idée générale du positionnement multidimensionnel est la réduction de dimension comme dans le cas de l'analyse en composantes principales, mais ici, nous avons comme entrées, une matrice de similarité entre les points. De la matrice de similarité, nous essayerons d'obtenir les coordonnées des points de données et les répresenter dans un plan, un espace de dimension trois, ou plus (mais de dimension inférieure à la taille des données).

Dans cette partie, nous parlerons du positionnement multidimensionnel classique; pour les autres types de positionnement, le lecteur pourra se référer à la litérature {cite}`bishop2006pattern,schiffman1981introduction`.

Supposons une matrice $M$ où $M_{ij}$ représente la similarité entre les $i^{\`eme}$ et $j^{\`eme}$ exemples de données. Ce que nous avons à notre possession, c'est la matrice de similarité entre les exemples.

Dans le cas du positionnement multidimensionnel, la fonction de perte ou fonction de décision est appelée **stress** et elle est donnée par:

$$\begin{equation}
 \label{cf}
S(\mathbf{z}_{1}, \mathbf{z}_{2},\cdots,\mathbf{z}_{n}) = \sum_{i\neq j}\left(M_{ij}-||\mathbf{z}_{i}-\mathbf{z}_{j}||\right)^{2},
\end{equation}$$

avec $M_{ij} = ||\mathbf{x}_{i}-\mathbf{x}_{j}||$, $\mathbf{x}_{i} \in \mathbb{R}^{d}$ et $\mathbf{z}_{i},\ i= 1,\cdots,n$, les points obtenus aprés la réduction de dimension. De l'équation {eq}`cf`, nous pouvons remarquer que notre objectif principal est de trouver $\mathbf{z}_{i},\ i = 1\cdots n$ de telle sorte que: $||\mathbf{z}_{i}-\mathbf{z}_{j}||= M_{ij}$. Cette solution n'est pas unique, puisqu'à part le fait que $\mathbf{z}^{\star}_{i},\ i=1,\cdots, n$ soit solution, $\mathbf{z}^{\star}_{i}+c^{ste},\ i = 1,\cdots, n$, l'est aussi.

En utilisant l'assomption de la configuration centrée qui stipule:

$$\begin{equation}
 \label{zero_sum}
\sum_{i=1}^{n}\mathbf{x}^{k}_{i} = 0,\quad \forall k=1, \dots, d,
\end{equation}$$

et en définissant la matrice de Gram par $\mathbf{B} = \mathbf{X}\mathbf{X}^{T}$ qui est une matrice carrée de dimension $n\times n$, avec $\mathbf{X} = [\mathbf{x}_{1}, \mathbf{x}_{2}, \cdots, \mathbf{x}_{n}]$, nous avons:

$$\begin{equation}
 \label{norm_square}
d^{2}_{ij} = b_{ii}+b_{jj} - 2b_{ij},
\end{equation}$$

avec $b_{ii} = ||\mathbf{x}_{i}||^{2}$ et $b_{ij} = \mathbf{x}^{T}_{i}\mathbf{x}_{j}$.

Nous posons: $$\begin{align*}
 \label{T_expression}
%\nonumber
 T = \sum_{i}b_{ii}
\end{align*}$$

En utilisant les relations {eq}`norm_square` et {eq}`T_expression`, nous obtenons: $$\begin{equation}
 \label{pp}
    \begin{cases}
    \sum_{i=1}^{n}d^{2}_{ij} = T+nb_{jj}-2\sum_{i=1}^{n}b_{ij}\\
    \sum_{j=1}^{n}d^{2}_{ij} = T+nb_{ii} -2\sum_{j=1}^{n}b_{ij}\\
    \sum_{i,j}^{n}d^{2}_{ij} = 2nT - 2\sum_{i,j=1}^{n}b_{ij}
    \end{cases}
\end{equation}$$

En utilisant la relation {eq}`norm_square`, l'équation {eq}`pp` devient $\left(\sum_{i}b_{ij}=0\right)$:

$$\begin{equation}
 \label{pp1}
    \begin{cases}
    \sum_{i=1}^{n}d^{2}_{ij} = T+nb_{jj}\\
    \sum_{j=1}^{n}d^{2}_{ij} = T+nb_{ii} \\
    \sum_{i,j=1}^{n}d^{2}_{ij} = 2nT 
    \end{cases}
\end{equation}$$

À partir des relations {eq}`zero_sum`, {eq}`norm_square` et {eq}`pp1`, nous pouvons déduire : $$\begin{equation}
b_{ij} = -\frac{1}{2} \left(d^{2}_{ij}-d^{2}_{.j}-d^{2}_{i.}+d^{2}_{..}\right),
\end{equation}$$

avec :

- $\displaystyle \mathbf{d}^{2}_{i.} = \frac{1}{n}\sum_{j=1}^{n}d^{2}_{ij}$,

- $\displaystyle d^{2}_{..}=\frac{1}{n}\sum_{i,j=1}^{n}d^{2}_{ij}$,

- $\displaystyle \mathbf{d}^{2}_{.j} =  \frac{1}{n}\sum_{i=1}^{n}d^{2}_{ij}$.

[L'[algorithme]{style="color: blue"}](http://www.iro.umontreal.ca/~pift6266/A06/cours/unsupervised.pdf) de positionnement classique est donné comme suit:

- Calculer la moyenne par rangées donnée par: $$\begin{equation*}
  \boldsymbol{\mu}_{i} = \frac{1}{n}\sum_{j}M_{ij}
  \end{equation*}$$

- Calculer la matrice $B$ similaire à notre matrice de similarité et définie par:

  $$\begin{equation}
      \mathbf{B} = \left(\mathbf{I}-\frac{1}{n}\mathbf{J}\right)\mathbf{M}^{2} \left(\mathbf{I}-\frac{1}{n}\mathbf{J}\right),
  \end{equation}$$

  avec $\mathbf{J}$, une matrice contenant que des 1 et de dimension $n\times n$. Ici, la matrice $\mathbf{B}$ doit être semi-définie positive, ce qui signifie qu'elle doit avoir des valeurs propres positives ou bien égales à zéro. $\mathbf{B}$ est une matrice ayant comme éléments $b_{ij}$.

- Calculer les vecteurs propres $v_{i}$ et valeurs propres $\lambda_{i}$ de la matrice $\mathbf{B}$.

- La $i$-ème coordonnée réduite pour l'exemple $j$ est $\sqrt\lambda_{i}\times v_{j}^i$

Le positionnement multidimensionnel est utilisé en analyse des préférences sur l'ensemble des domaines d'application de la psychométrie, en particulier dans la conception et le marketing des produits agro-alimentaires [ici](http://www.modulad.fr/archives/numero-32/desbois-32/desbois-32.pdf).

### Analyse en Composantes Principales (ACP)

L'Analyse en composantes principales (ACP, PCA en Anglais) est l'une des plus célèbres méthodes de compression, réduction de dimensions et de visualisation de données. Elle utilise ce qu'on appelle composantes principales pour trouver une base du sous-espace sur lequel on projète les données. Pour mieux comprendre le fonctionnements de l'ACP, nous allons commencer par illustrer le cas des données de dimension $d = 2$. Ensuite on généralisera pour le cas de dimension $d \ge 2$. On considère dorénavant un ensemble de données $\mathcal{D} =  \{ \mathbf{x}_1 , \dots, \mathbf{x}_n\} \subset \mathbb{R}^d$ où $n$ désigne le nombre d'élements de $\mathcal{D}$.

#### Cas $d = 2.$

Supposons qu'on a les données dans le plan $\mathbb{R}^2$. La compression consiste donc à projeter ces données sur un sous-espace de $\mathbb{R}^2$, de dimension $p < 2$. On sait qu'un sous-espace de dimension $0$ est un point. Donc la compression en dimension $p=0$ détruira toutes les informations sur les données en les réduisant en un point. Nous n'avons donc d'autres choix que de compresser en dimension $p = 1$, c'est-à-dire projeter les données sur une droite vectorielle. Pourtant, il y a une infinité de tels sous-espaces. Cependant, nous voulons une compression ayant le maximum d'informations sur nos données. Comment choisir ce sous-espace?

La méthode ACP consiste à choisir ce sous-espace comme la droite maximisant la variance des projections de données. Le vecteur directeur de cette droite s'appelle **première composante principale** ou tout simplement **composante principale** . Le complété orthogonal de ce sous-espace est engendré par la **seconde composante principale**.

```{figure} images/pca.png
:name: fig-acp
:alt: L’illustration de l’ACP

L’illustration de l’ACP
```


Dans la {ref}`fig-acp`, nous avons un ensemble de données dans un système de coordonnées $(O, \mathrm{x}_1, \mathrm{x}_2)$. Supposons qu'on veux compresser l'ensemble de données dans un espace de dimension $1$ qui peut être l'un des axes $(O,\mathrm{x}_1), (O,\mathrm{x}_2), (O,\mathrm{x}_1'), (O,\mathrm{x}_2')$.

- En projetant sur $(O, \mathrm{x}_1)$ (resp. $(O, \mathrm{x}_2)$), on obtiendra une représentation assez compressée de nos données. En fait, quelques représentations des points sont confondues.

- En projetant sur $(O,\mathrm{x}_2')$ les données sont projetées sur un segment de même longueur que le petit axe de l'ellipse $\mathcal{E}$. On obtiendra une représentation trop compressée des données. Tant d'informations sur les données sont donc perdues. Beaucoup de points auront la même représentation.

- En projetant sur $(O, \mathrm{x}_1')$ on voit que la représentation des points est \"presque injective\" [^1]. C'est donc la représentation idéale pour notre exemple.

Dans notre cas, la première composante principale est le vecteur (unitaire) directeur de l'axe $(O,\mathrm{x}_1')$ puisqu'il nous permet d'avoir le maximum de variance lors de la compression.

#### Cas général ($d\ge 2$).

Dans le cas $d=2$, nous avons essayé de donner une explication intuitive et visuelle de ce que l'algorithme ACP fait. Dans ce qui suit, nous allons généraliser la méthode ACP. L'objectif principal de cette méthode est donc de trouver les composantes principales.

***Comment trouver les composantes principales?***

La méthode classique pour trouver les composantes principales est d'utiliser les valeurs propres et vecteurs propres de la matrice de covariances des données. La première composante principale n'est autre que le vecteur propre correspondant à la plus grande valeur propre, la seconde composante principale est celui qui correspond à la deuxième plus grande valeur propre, et ainsi de suite. En effet, on peut prouver que les vecteurs propres de la matrice des covariances donnent les directions sur lesquelles les données ont la variance maximale (voir Section 1.1 de {cite}`jolliffe1986principal`).

Soit $M$ la matrice de covariance des données. Puisque les données sont de dimension $d$, $M$ est une matrice carrée d'ordre $d$ ($M\in \mathcal{M}_{d}(\mathbb{R})$). Rappelons aussi que la matrice de covariance est symétrique définie positive. Donc les valeurs propres de $M$ sont toutes strictement positives.

Soient $\lambda_1, \dots, \lambda_d$ les valeurs propres de $M$ correspondant respectivement aux vecteurs propres $\mathbf{v}_1,\ldots, \mathbf{v}_d\}$. Sans perte de généralité, on peut supposer que les valeurs propres sont arrangées dans l'ordre décroissant, c'est-à-dire $\lambda_1 \ge \lambda_2\ge \cdots \ge \lambda_d$ et que les vecteurs propres sont tous unitaires (de norme 1). Notons que ces vecteurs propres forment une base orhtonormée de $\mathbb{R}^d$.

Notons par $\mathcal{D}' =  \{ \mathbf{x}_1', \dots, \mathbf{x}_n' \}$ les représentations des éléments de $\mathcal{D}$ dans la base $\{\mathbf{v}_1,\ldots, \mathbf{v}_d\}$ de $\mathbb{R}^d$. Pour compresser $\mathcal{D}$ sur un espace de dimension $p$ ($p < d$), l'ACP prend les éléments de $\mathcal{D}'$ et les tronque à la $p$-ième composante.

(algorithme-de-lanalyse-en-composantes-principales.)=
#### Algorithme de l'Analyse en Composantes Principales.

**Remarque.** Avant de procéder à l' ACP, il faut normaliser les données, en soustrayant la moyenne puis en divisant par l'écart-type, composantes par composantes. C'est très important parce que les composantes caractéristiques peuvent avoir différentes unités de mesure.

**Algorithme**: Voici les étapes de l'algorithme :

1.  Calculer la moyenne : $$\hat{\boldsymbol{\mu}} = \frac{1}{n} \sum_{k = 1}^{n} \mathbf{x_k}$$

2.  Calculer la matrice de covariance $$\mathbf{M} = \frac{1}{n} \sum_{k = 1}^{n} (\mathbf{x_k} - \boldsymbol{\mu})(\mathbf{x_k} - \hat{\boldsymbol{\mu}})^T$$

3.  Trouver les valeurs propres et vecteurs propres: $$\mathbf{M}\mathbf{v}_i = \lambda_i \mathbf{v}_i, \ \  i = 1, \dots, d.$$

4.  Choisir les valeurs propres de plus grande valeurs:

    1.  Ranger les valeurs propres dans l'ordre décroissant

    2.  Choisir une valeur de tolérance $\tau \in ]0,1[$.

    3.  Le nombre $p$ de valeurs propres choisies satisfera la relation $$\frac{\sum_{i = 1}^{p} \lambda_i }{\sum_{j = 1}^{d} \lambda_j} \ge \tau .$$

    4.  Choisir les $p$ vecteurs propres correspondants et noter par $\mathbf{P}$ la matrice d'ordre $d\times p$ formée.

5.  Extraire les représentations en dimension $p$ en multipliant $\mathbf{P}^T$ par les $\mathbf{x_k}$.

## Applications

L'objectif généralement lorsque nous effectuons une analyse de regroupement:

- Obtenir une intuition significative de la structure des données que nous traitons.

- Grouper puis prédire, où différents modèles seront construits pour différents sous-groupes si nous pensons qu'il existe une grande variation dans les comportements des différents sous-groupes. Un exemple de cela est de regrouper les patients en différents sous-groupes et de construire un modèle pour chaque sous-groupe afin de prédire la probabilité du risque de crise cardiaque.

De ce fait, l'algorithme $K$-moyenne étant très populaire peut être utilisé dans diverses [applications](https://www.simplilearn.com/tutorials/machine-learning-tutorial/k-means-clustering-algorithm) telles que la segmentation du marche, le regroupement de documents, la segmentation d'images et la compression d'images, etc.

- La classification de documents en plusieurs catégories en fonction des balises, des sujets et du contenu du document;

- Optimisation d'un magasin de livraison, ceci en utilisant une combinaison de $K$-moyens pour trouver le nombre optimal d'emplacements de lancements;

- Identification des localités de crimes, ceci avec des données relatives aux crimes disponibles dans des localités spécifiques d'une ville, la catégorie de crime, la zone du crime et l'association entre les deux peuvent donner un aperçu de qualité des zones sujettes à la criminalité dans une ville ou une localité;

- Segmentation de la clientèle tout en aidant les spécialistes du marketing à améliorer leur base de clients, à travailler sur des domaines cibles et à segmenter les clients en fonction de l'historique des achats, des intérêts ou du suivi des activités;

- détection de fraude à l'assurance: en utilisant des données historiques passées sur les réclamations frauduleuses, il est possible d'isoler les nouvelles réclamations en fonction de leur proximité avec des grappes qui indiquent des modèles frauduleux;

- Analyse des données de covoiturage: l'analyse de ces données est utile non seulement dans le contexte d'uber, mais également pour donner un aperçu des modèles de trafic urbain et nous aider à planifier les villes du futur;

- Criminels de cyber-profilage en classifiant les types de criminels qui se trouvent sur des lieux de crime;

- Regroupement automatique des alertes informatiques;

- Classification de performance académique;

- Moteurs de recherche: Les résultats de recherche sont groupés en utilisant l'algorithme de regroupement;

- La segmentation ainsi que la compression d'images.

## Conclusion

Dans ce chapitre, les données étaient considérées comme linéairement séparables, c'est à dire nous pouvons trouver une ligne droite (dans le cas où nous sommes en dimension deux) ou un hyperplan (de manière générale) qui sépare ces données. De plus la distance que nous avions considérée était celle Euclidienne. Cependant, dans la plupart des cas, nos données sont non-linéaires et la distance considérée peut être géodésique, c'est à dire non Euclidienne ou bien Riemanienne. Pour cela, nous devons nous référer à des méthodes ou bien des algorithmes qui nous permettent de pouvoir faire soit le partitionnement ou la réduction de dimension dans le dit cas et aussi considérer des cas de distance non Euclidienne. Il y a plusieurs modèles qui ont été dévelopés, parmi ceux-là, nous avons les méthodes de Kernel comme Kernel PCA, Kernel Clustering, réseaux de neurones et aussi ISOMAP, dans le cas de distance géodésique. Certaines de ces méthodes vous seront présentées dans le chapitre {ref}`ch5`.

[^1]: Cela signifie que presque chaque point aura une représentation différente de celle d'un autre point.
