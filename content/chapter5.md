(ch5)=
# Les méthodes du noyau (Kernel methods)

## Motivations et Rappels

### Motivations

La plupart du temps, en apprentissage automatique, les difficultés que nous rencontrons ne se situent pas dans l'exécution ou l'implémentation des modèles et algorithmes de prédictions, mais dans l'adaptation de ces derniers aux données soumises à notre analyse.

Les données sont généralement classifiées en deux catégories à savoir:

- Les données $\textbf{linéairement séparables}$ c'est-à-dire les données qui peuvent facilement être séparées en groupes (ou classes) d'échantillons qui ont des propriétés similaires, mesurées sur des observations, à l'aide d'un hyperplan, parfaitement construit via un calcul de décision par combinaison linéaire des échantillons.

- Les données $\textbf{non-linéairement séparables}$ sont totalement le contraire de celles dites linéairement séparables car ici, il n'est pas évident de manière directe séparer les données en groupes (ou classes) d'échantillons qui ont des propriétés similaires, à l'aide d'un hyperplan (en haute dimension).

::::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card}
```{figure} images/ariel1.png
:name: fig-sub-first
:width: 100%

Données linéairement séparables
```
:::

:::{grid-item-card}
```{figure} images/non-lineaire-separable.png
:name: fig-sub-second
:width: 100%

Données non-linéairement séparables
```
:::

::::


À cet effet, il est souvent plus facile de résoudre les problèmes aux données linéairement séparables que ceux qui ne le sont pas, ceci en utilisant les techniques et méthodes présentées dans les chapitres 3 et 4. Cependant, il se trouve que dans la majeur partie des problèmes réels et du vécu quotidien, les données souvent manipulées sont rarement linéairement séparables, car elles sont plus compliquées, ce qui rend plus complexes l'analyse et les prédictions via les modèles basiques de l'apprentissage automatique. D'où l'intérêt de ce chapitre sur les méthodes du noyau.

Le but de ce chapitre est d'étendre les notions vues dans les chapitres précédents et les techniques de l'apprentissage de la statistique linéaire, à un monde réel, plus complexe, mieux structuré et en dimension plus élevée. Nous allons nous appuyer sur les méthodes mathématiques liées aux outils de modélisation pratique et algorithmes ou modèles de prédiction déjà bien connus en apprentissage automatique.

### Rappels

#### Espace de Hilbert

Il y a au moins deux raisons profondes qui expliquent l'importance et l'omniprésence des espaces de Hilbert dans les mathématiques.

Premièrement, ils apparaissent comme généralisation naturelle des espaces euclidiens de dimension finie (par exemple, le plan $\mathbb{R}^{2}$ ou l'espace $\mathbb{R}^{n}\ (n \geqslant 3)$). Ils bénéficient des propriétés familières telles que le produit scalaire, l'orthogonalité, les projections (orthogonales), le théorème de Pythagore, etc.

Crucialement, on demande que les espaces de Hilbert abstraits soient complets pour la topologie qui dérive de leur norme. Cette condition de complétude est importante, et on la requiert afin que les constructions géométriques et les passages à la limite se passent aussi bien en dimension infinie qu'en dimension finie, et aussi, afin qu'il existe des bases orthonormées, de cardinal infini, le long desquelles on puisse décomposer chaque vecteur.

**Définitions**

Soit $E$ un espace vectoriel normé sur $\mathbb{K}=\mathbb{R}$ ou $\mathbb{C}$.

La suite $\displaystyle (U_{n})_{n}$ est dite de $\textbf{Cauchy}$ si et seulement si,

:::{div}
:class: center
$\displaystyle \forall \epsilon \ge 0$, $\displaystyle \exists n_0 \in \mathbb{N}$, $\displaystyle \forall n \ge n_0$, $\displaystyle || U_{n+p} - U_n || \le \epsilon$, $\displaystyle \forall p \in \mathbb{N}.$
:::

De façon équivalente:

:::{div}
:class: center
$\displaystyle \forall \epsilon \ge 0$, $\displaystyle \exists n_0 \in \mathbb{N}$, $\displaystyle \forall n, m \ge n_0$, $\displaystyle || U_n - U_m || \le \epsilon.$
:::

*Remarque:* La suite $(U_{n})_{n}$ de $E$ est dite de Cauchy si et seulement si:

:::{div}
:class: center
$\displaystyle \epsilon_{n} = \operatorname{Sup}_{p \in \mathbb{N}} || U_{n+p} - U_n || \rightarrow 0.$
:::

*Propriétés:*

- Toute suite de Cauchy est bornée.

- Toute suite convergente est de Cauchy.

Un espace vectoriel normé est dit $\textbf{complet}$ si et seulement si toute suite de Cauchy de $E$ est convergente. Un espace vectoriel normé complet est dit un $\textbf{Banach}$. Un ensemble $F \subset E$ est dite complet si toute suite de Cauchy d'éléments de $F$ converge dans $F$.

**Définition: (Espace de Hilbert)**

Un **espace de Hilbert** est un espace vectoriel réel ou complexe muni d'un produit scalaire et qui est $\textbf{complet}$ pour la norme associée.

#### Quelques propriétés et caractéristiques des espaces de Hilbert

$\textbf{Définition: (Espace topologique)}$

Sur un ensemble $E$, on peut définir une topologie $T$ comme un ensemble de parties de $E$ vérifiant les propriétés suivantes:

- $E$ et l'ensemble vide appartiennent à $T$;

- $T$ est stable par intersection finie: Pour tout $U_{1} \in T$, $U_{2}\in T$, $\Rightarrow$ $\displaystyle U_1 \cap U_2 \in T$;

- $T$ est stable par la réunion quelconque: Pour tout ensemble $I$ (fini ou infini) d'indices, pour tout $U_{i} \in T$ $\Rightarrow$ $\displaystyle \bigcup_{i \in I} U_i$.

Alors par définition, un sous-ensemble $U$ de $E$ est un $\textbf{ouvert}$ de $E$ pour la topologie $T$ si et seulement si $U$ appartient à $T$ (il en résulte que la topologie $T$ peut être définie comme l'ensemble des ouverts de $E$ selon $T$).

**Définition: (Espace fermé)**

Dans un espace topologique $E$, un $\textbf{fermé}$ est un sous-ensemble de $E$ dont le complémentaire est un ouvert.

**Définition: (Produit hermitien)**

Un produit hermitien sur un $\mathbb{C}$-espace vectoriel $H$ est une application:

:::{div}
:class: center
$\displaystyle (\mathbf{u},\mathbf{v}) \in H\times H \mapsto \langle \mathbf{u},\mathbf{v}\rangle \in \mathbb{C}$
:::

- $\textbf{sesquilinéaire:}$ $\mathbf{u} \mapsto \langle \mathbf{u},\mathbf{v}\rangle$ est anti-linéaire; $\mathbf{v} \mapsto \langle \mathbf{u},\mathbf{v}\rangle$ linéaire.

- $\textbf{hermitienne:}$ $\displaystyle \langle \mathbf{u},\mathbf{v}\rangle =    \overline{\langle \mathbf{v},\mathbf{u}\rangle}$ (en particulier $\displaystyle \langle \mathbf{u},\mathbf{u}\rangle$ est réel).

- $\textbf{positives:}$ $\displaystyle \langle \mathbf{u},\mathbf{u}\rangle > 0$ si $\mathbf{u} \neq 0$.

**Proposition:**

Un sous-espace fermé d'un espace de Hibert est un espace de Hilbert (pour la restriction du produit hermitien).

**Géométrie dans un espace de Hilbert:**

- **Inégalité de Cauchy-Schwarz:** l'inégalité de Cauchy-Schwarz s'écrit:

  :::{div}
  :class: center
  $\displaystyle |\langle x,y\rangle| \le ||x||.||y||$
  :::

- **L'égalité de la médiane:**

  :::{div}
  :class: center
  $\displaystyle || x -a ||^{2} + || x - b||^{2} = 2|| x - \frac{a+b}{2} ||^{2} + 2|| x - \frac{a-b}{2} ||^{2}$.
  :::

**Théorème:**

Une application linéaire entre deux espaces de Hilbert, $E$, $F$ est continue si et seulement si il existe une constante $C$ telle que pour tout $x$ de $E$ on a:

:::{div}
:class: center
$\displaystyle || u(x) ||_F \le C ||x||_E$.
:::

Si $F$ est un sous-espace quelconque de $H$, on pose:

:::{div}
:class: center
$\displaystyle F^{\perp} = \{ x \in H,  \forall y \in F, \langle x,y\rangle = 0 \}$.
:::

$\textbf{Théorème de décomposition:}$

Si $F$ est un sous-espace $fermé$, alors

:::{div}
:class: center
$\displaystyle H = F \bigoplus F^{\perp}$.
:::

$\textbf{Théorème de représentions de Riez:}$

Soit $u$ une forme continue sur un espace de Hilbert. Il existe un unique vecteur $a_u \in E$ tel que:

:::{div}
:class: center
$\displaystyle \forall x \in E, u(x) = \langle a_u,x\rangle$.
:::

$\textbf{Preuve:}$

On peut supposer $u \neq 0$. On choisit $b_u$ un vecteur unitaire orthogonal à $\displaystyle F = ker(u)$. ($b_u$ existe car $H = F \oplus F^{\perp}$ et $F \neq H$).

On a alors $\displaystyle u(x - u(x)\frac{b_u}{u(b_u)}) = 0$, donc $\displaystyle H = ker(u) \oplus \mathbb{C}b_u$. On vérifie alors que $\displaystyle u(x) = \langle u(b_u)b_u,x\rangle$, pour $x \in ker(u)$ puis $\displaystyle x \in \mathbb{C}b_u$. C'est donc vrai pour tout $x$, et la proposition est vérifié avec:

:::{div}
:class: center
$\displaystyle a_u = u(b_u)b_u.$
:::

### Noyaux et espaces de Hilbert à noyau reproduisant (RKHS)

Pour cette partie, nous représentons les données d'entrée $x_1, ...,x_n \in \mathbb{X}$ par une matrice carrée définie par $\displaystyle k_{ij} = k(x_i,x_j)$, où $\mathbb{X}$ est un espace pris arbitrairement, $\displaystyle k \in \mathbb{R}^{n \times n}$ une matrice de noyau et $k$ une fonction symétrique définie par  
$\displaystyle k: \mathbb{X} \times \mathbb{X} \rightarrow \mathbb{R}$ et $\forall \mathbf{x}, \mathbf{y} \in \mathbb{X}$,  $k(\mathbf{x},\mathbf{y}) = k(\mathbf{y},\mathbf{x}).$

Une notion assez importante à révéler ici est la $\textbf{condition de positivité}$ qui est donnée par:

:::{div}
:class: center
$\displaystyle \forall  x_1, ..., x_n \in \mathbb{X}$, la matrice de noyau $k$ est définie positive, c'est-à-dire,

$\displaystyle \forall \boldsymbol{\alpha} \in \mathbb{R}^n$, $\displaystyle \boldsymbol{\alpha}^{T} k \boldsymbol{\alpha} = \sum_{i,j = 1}^{n} \alpha_i \alpha_j k(x_i,x_j) \ge 0.$
:::

Les conditions de **positivité** et **symétricité** sont très importantes pour définir un kernel $k$ valide.

**Exemple:** $\displaystyle \mathbb{X} = \mathbb{R}^d$, $k(\mathbf{x},\mathbf{y}) = \mathbf{x}^{T}\mathbf{y}$. Pour tout $\mathbf{x}$ et $\mathbf{y}$ $\in \mathbb{X}$, nous avons $k(\mathbf{x},\mathbf{y})=k(\mathbf{y},\mathbf{x})$, ceci implique que $k$ est symétrique. De plus, $\forall \boldsymbol{\alpha} \in \mathbb{R}^{n}$, $\boldsymbol{\alpha}^{T}k \boldsymbol{\alpha} = \sum_{i,j=1}^{n} \alpha_{i}k(x_{i}, x_{j}) \alpha_{j} =\sum_{i,j=1}^{n}\langle \alpha_{i}x_{i},\alpha_{j}x_{j} \rangle \geq 0$. Donc, puisque $k$ est positif et symétrique, alors c'est un kernel valide.

$\textbf{Théorème: (Aronszajn, 1950)}$

(explicit-implicit)=
Un noyau $k$ est défini positif si et seulement s'il existe un espace de Hilbert $\mathbb{F}$ et un 'feature map' $\displaystyle \Phi: \mathbb{X} \rightarrow \mathbb{F}$ tels que:

:::{div}
:class: center
$\displaystyle k(\mathbf{x},\mathbf{y}) = \langle \Phi(\mathbf{x}),\Phi(\mathbf{y})\rangle_{\mathbb{F}}$
:::

**Opérations sur les noyaux définis positifs (d.p)**

- Structure de cône:

  - $k$ noyau d.p, $\displaystyle \lambda \geqslant 0 \Rightarrow \lambda k$ noyau d.p.

  - $k_1, k_2$ noyau d.p. $\Rightarrow k_1 + k_2$ noyau d.p.

- $k_1, k_2$ noyaux d.p. $\Rightarrow k_1k_2$ noyau d.p.

**Noyau polynomial en dimension p\>1**

Le noyau polynomial en dimension $p>1$, est donné par l'expression suivante:

:::{div}
:class: center
$\displaystyle k(\mathbf{x},\mathbf{y}) = (1 + \mathbf{x}^{T}\mathbf{y})^d$
:::

Il y a deux possibilités d'expandre cette expression et ceci peut se faire de la façon suivante:

- $\textbf{Première expansion:}$

  :::{div}
  :class: center
  $\displaystyle k(\mathbf{x},\mathbf{y}) = \sum_{k=1}^{d+1} C^{k-1}_{d+1}(\mathbf{x}^{T}\mathbf{y})^{k+1}.$
  :::

- $\textbf{Deuxième expansion}$

  :::{div}
  :class: center
  $\displaystyle (\mathbf{x}^{T}\mathbf{y})^{k} = (\sum^{d}_{i=1}x_iy_i)^k = \sum_{i_1 + i_2 + ... + i_d = k} \frac{k!}{i_1! ... i_d!} (x_1y_1)^{i_1} ... (x_d y_d)^{i_d}$
  :::

- $\Phi(\mathbf{x})$ contient tous les monômes (avec des poids) $x_{1}^{i_1} ... x_{d}^{i_d}$ avec $i_1 + ... + i_d \leqslant k.$

- Dimension de $\mathbb{F}:$ $C^{d}_{p+d}$ (grand!).

**Noyaux invariants par translation**

Les noyaux invariants par translation sont de la forme : $$k(\mathbf{x},\mathbf{y}) = q(\mathbf{x}-\mathbf{y}), q \in L^2(\mathbb{R}^p)\quad \text{continue}.$$

**Proposition:**

$k$ est défini positif si et seulement si la [transformée de Fourier](https://fr.wikipedia.org/wiki/Transformation_de_Fourier) $\mathbf{Q}(w)$ de $q$ est positive ou nulle pour tout $w \in \mathbb{R}^p.$

**Exemple:** Noyau Gaussien: $\displaystyle k(\mathbf{x},\mathbf{y}) = e^{-\alpha||\mathbf{x}-\mathbf{y}||^2}.$

Avant de continuer plus loin, faisons le point sur tout ce que nous avons vu jusqu'ici:

- On a vu qu'un noyau défini positif est équivalent à une matrice symétrique semi-définie positive.

- Lorsque la fonction $\Phi$ ('feature map') est connue au préalable (comme présenté dans le théorème {ref}`explicit-implicit` ) le noyaux $k$ s'exprime explicitement de la forme $\displaystyle k(\mathbf{x},\mathbf{y}) = \langle \Phi(\mathbf{x}),\Phi(\mathbf{y})\rangle_{\mathbb{F}}.$

- Contrairement, le noyaux $k$ sera déduite implicitement (exemple: Noyau Gaussien).

- Deux théories permettent de construire la fonction $\Phi$:

  - Espaces de Hilbert à noyaux reproduisant (RKHS).

  - Noyaux de Mercer.

$\textbf{Définition d'un RKHS}$

Soit $\mathcal{X}$ un ensemble quelconque et $\mathcal{F}$ un sous-espace de l'espace des fonctions de $\mathcal{X}$ dans $\mathbb{R}$, qui est muni d'un produit scalaire Hilbertien.

$\mathcal{F}$ est un RKHS avec noyau reproduisant $\displaystyle k: \mathcal{X} \times \mathcal{X} \rightarrow \mathbb{R}$ si et seulement si:

- $\mathcal{F}$ contient toutes les fonctions de la forme:

  :::{div}
  :class: center
  $\displaystyle k(\mathbf{x},.): \mathbf{y} \rightarrow k(\mathbf{x},\mathbf{y})$
  :::

- $\displaystyle \forall \mathbf{x} \in \mathcal{X}$ et $f \in \mathcal{F}$,

  :::{div}
  :class: center
  $\displaystyle f(\mathbf{x}) = \langle f,k(.,\mathbf{x})\rangle_{\mathcal{F}}$
  :::

  (c'est-à-dire $k(.,\mathbf{x})$ correspond au 'Dirac' en $\mathbf{x}$ ).

$\textbf{Propriétés des RKHS}$

- $\textbf{Unicité:}$ s'il existe un noyau reproduisant, il est unique.

- $\textbf{Existence:}$ un noyau reproduisant existe si et seulement $\displaystyle \forall x \in \mathcal{X}$, la forme linéaire $f \rightarrow f(x)$ est continue.

- Si $k$ est un noyau reproduisant, alors $k$ est un noyau défini positif.

- Si $k$ est un noyau défini positif, alors $k$ est un noyau reproduisant (pour un certain RKHS $\mathcal{F}$).

**Construction du RKHS pour un noyau d.p.**

Dans cette section nous donnons les étapes pour la construction du noyau sur un **RKHS**:

- Construction de $\mathcal{F}_0$ l'ensemble de combinaisons linéaires finies de fonctions $k(.,y)$, $y \in \mathcal{X}.$

- Définition du produit scalaire sur $\mathcal{F}_0$ de la manière suivante:

  :::{div}
  :class: center
  $\displaystyle \left(\sum_i \alpha_ik(.,x_i), \sum_j \beta_jk(.,y_j)\right)_{\mathcal{F}_0} = \sum_i\sum_j \alpha_i\beta_jk(x_i,y_j).$
  :::

- Interprétation de la norme $||f||^{2}_{\mathcal{F}}$

  - La norme contrôle les variations de $f$.

  - $f$ est une fonction lipschitzienne c'est a dire: $\displaystyle |f(x) - f(y)| = |\langle f, k(.,x) - k(.,y)\rangle_{\mathcal{F}}| \le ||f||_{\mathcal{F}}||k(.,x) - k(.,y)||_{\mathcal{F}}$

  - La norme du RKHS contrôle la constante de Lipschitz de $f$ pour la métrique $\displaystyle d_k(x,y) = ||k(.,x) - k(.,y)||_{\mathcal{F}}.$

**Noyaux de Mercer**

- Construction semi-explicite d'un 'feature space' égale à l'ensemble des suites de réels.

- **Hypothèses:** $\mathcal{X}$ espace métrique compact muni d'une mesure $\nu$, noyau $k$ noyau d.p. continu.

- **Théorème de Mercer:** il existe une base Hilbertienne de $L^{2}(\mathcal{X})$ de fonctions continues ($\Psi_i$ est une suite décroissante ($\lambda_i$) tendant vers zéros, telle que:

  :::{div}
  :class: center
  $\displaystyle \forall x, y \in \mathcal{X}$, $\displaystyle k(x,y) = \sum^{\infty}_{i=1} \lambda_i\Psi_i(x)\Psi_i(y).$
  :::

Faisons un point de ce que nous avons vu jusqu'ici:

Resume

- Noyaux définis positifs = produits scalaires de 'features'

  :::{div}
  :class: center
  $\displaystyle k(x,y) = \langle \Phi(x),\Phi(y) \rangle$
  :::

- **Noyaux de Mercer:** 'feature map' obtenu à partir de l'opérateur de convolution.

- **RKHS:** construction explicite sans hypothèses.

- Interprétation de la norme du RKHS en terme de régularité des fonctions.

- **Noyaux classiques:** linéaires, polynomiaux, Gaussiens.

## Le Noyau: définitions et propriétés

### Méthodes à noyaux générales

#### Astuce du noyau (Kernel Trick) et théorème du représentant

- **Astuce du noyau**

  - Un noyau défini positif correspond à des "features" potentiellement nombreux et souvent implicites;

  - **Principe:** tout algorithme sur des vecteurs de dimension finie n'utilisant que des produits scalaires peut être utilisé en remplaçant le produit scalaire par n'importe quel noyau défini positif;

  - Il existe de nombreuses applications pour les astuces du noyau.

- $\textbf{Théorème du représentant}$

  - Soient $\mathcal{X}$ un ensemble, $k$ un noyau d.p., et $F$ son RKHS associé, et $x_1, ..., x_n$, $n$ points dans $\mathcal{X}$.

  - Soit $\displaystyle J: \mathbb{R}^{n+1} \longrightarrow \mathbb{R}$ strictement croissante par rapport à la dernière variable

  - Toute solution du problème d'optimisation suivant:

    :::{div}
    :class: center
    $\displaystyle \min_{\mathcal{F}} ~~ J(f(x_1), ..., f(x_n),||f||_{\mathcal{F}}).$
    :::

    s'écrit de la forme $\displaystyle f = \sum^{n}_{i=1} \alpha_ik(.,x_i)$

  - De manière classique on a:

    :::{div}
    :class: center
    $\displaystyle \min_{f \in \mathcal{F}} \sum^{n}_{i=1} l_i(f(x_i)) + \lambda||f||^{2}_{\mathcal{F}}.$
    :::

### Ridge regression (Régression de Ridge), Kernel ridge regression

**Ridge regression**

L'algorithme le plus élémentaire qui peut être kernelisé est probablement le Ridge regression. Ici, l'idée est de trouver une fonction linéaire qui modélise les dépendances entre les covariables $\{x_i\}$ et les variables de réponse $\{y_i\}$, toutes deux continues. La manière classique de le faire est de minimiser le coût quadratique:

$$\begin{equation}
                                     C(\mathbf{W}) = \frac{1}{2} \sum_i (y_i - \mathbf{W}^Tx_i)^2.
\end{equation}$$

Cependant, si nous allons travailler dans l'espace des fonctionnalités ('features space'), où nous remplaçons $x_i \longrightarrow \Phi(x_i)$, il existe un danger évident que nous sur-ajustions (overfitting). Par conséquent, nous devons régulariser.

Un moyen simple mais efficace de régulariser est de pénaliser la norme de $\mathbf{W}$. Ceci est parfois appelé «perte de poids» ('weight decay'). Il reste à déterminer comment choisir $\lambda$. L'algorithme le plus utilisé consiste à utiliser des estimations de validation croisée ('cross-validation') ou de non-participation ('leave-one-out estimates'). La fonction de coût total devient donc,

$$\begin{equation}
                                      C(w) = \frac{1}{2} \sum_i (y_i - w^Tx_i)^2 + \frac{1}{2}\lambda ||w||^2
\end{equation}$$

qui doit être minimisé. Prendre des dérivées et les assimiler à zéro donne,

$$\begin{equation}
                                      \sum_i (y_i - w^Tx_i)x_i = \lambda w ~~ \Longrightarrow ~~ w = (\lambda I + \sum_i x_ix^{T}_{i})^{-1} (\sum_j y_jx_j).
\end{equation}$$

**Kernel ridge regression**

Nous remplaçons maintenant tous les cas de données par leur vecteur de caractéristiques: $x_i \longrightarrow \Phi_i = \Phi(x_i)$. Dans ce cas, le nombre de dimensions peut être bien supérieur, voire infiniment supérieur, au nombre de cas de données. Il y a une astuce qui nous permet d'effectuer l'inverse ci-dessus dans le plus petit espace des deux possibilités, soit la dimension de l'espace des fonctionnalités, soit le nombre de cas de données. L'astuce est donnée par l'identité suivante:

$$\begin{equation}
                            (P^{-1} + B^{T}R^{-1}B)^{-1}B^{T}R^{-1} = PB^{T}(BPB^{T} + R)^{-1}.
\end{equation}$$

Notez maintenant que si $B$ n'est pas carrée, l'inverse est effectué dans des espaces de dimensionnalité différente. Pour appliquer cela à notre cas, nous définissons $\Phi  = \Phi_{ai}$ et $y = y_i$. La solution est alors donnée par:

$$\begin{equation}
                            w = (\lambda \mathbf{I}_d + \Phi \Phi^{T})^{-1}\Phi y = \Phi(\Phi^{T}\Phi + \lambda \mathbf{I}_n)^{-1}y.
\end{equation}$$

Cette équation peut être réécrite comme suit:

$$\begin{equation}
                            w = \sum_i \alpha_i \Phi(x_i),
\end{equation}$$

avec    $\alpha = (\Phi^{T} \Phi + \lambda \mathbf{I}_n)^{-1}y.$

C'est une équation qui sera un thème récurrent et qui peut être interprétée comme: La solution $w$ doit se situer dans l'étendue des cas de données, même si la dimensionnalité de l'espace d'entités est beaucoup plus grande que le nombre de cas de données. Intuitivement, cet algorithme est linéaire dans l'espace des fonctionnalités ('features space').

Nous devons enfin montrer que nous n'avons jamais réellement besoin d'accéder aux vecteurs de caractéristiques, qui pourraient être infiniment longs (ce qui serait plutôt peu pratique). Ce dont nous avons besoin en pratique, c'est de la valeur prédite pour un nouveau point de test, x. Ceci est calculé en le projetant sur la solution $w$,

$$\begin{equation}
                            y = w^T \Phi(x) = y^T(\Phi^T\Phi + \lambda \mathbf{I}_n)^{-1} \Phi^T\Phi(x) = y^T(K + \lambda \mathbf{I}_n)^{-1}\kappa(x)
\end{equation}$$

où $K(x_i, x_j) = \Phi(x_i)^T\Phi(x_j)\ et\ \kappa(x) = K(x_i,x).$

Le message important ici est bien sûr que nous n'avons besoin que d'accéder au noyau $K$.

Nous pouvons maintenant ajouter un biais à toute l'histoire en ajoutant une autre caractéristique constante à $\Phi: \Phi_0 = 1$. La valeur de $w_0$ représente alors le biais puisque,

$$\begin{equation}
                            w^{T}\Phi = \sum_a w_a\Phi_ai + w_0.
\end{equation}$$

En récapitulatif, reformulons tout ceci sous un problème d'optimisation:

- Considérons les données $x_1, ..., x_n \in \mathcal{X}$ , $k$ un noyau défini positif , et $y_1, ..., y_n \in \mathbb{R}$

- En utilisant la méthode des moindres carrés on a la formulation suivante:

  :::{div}
  :class: center
  $\displaystyle \min_{\mathcal{F}} \frac{1}{n} \sum^{n}_{i=1}(y_i - f(x_i))^{2} + \lambda||f||^{2}_{\mathcal{F}}.$
  :::

- Théorème du représentant implique que $\displaystyle f = \sum^{n}_{i=1}\alpha_ik(.,x_i)$

  - Ceci est équivalent à:

    :::{div}
    :class: center
    $\displaystyle \min_{\alpha \in \mathbb{R}^n} \frac{1}{n}\sum^{n}_{i=1}(y_i - (K\alpha)_i)^{2} + \lambda\alpha^{T}K\alpha$
    :::

  - La solution est égale à $\displaystyle \alpha = (K + n\lambda I)^{-1}y + \varepsilon$, avec $K\varepsilon = 0$

  - Cette solution $f$ est unique!

### Méthodes à noyaux et optimisation convexe

#### Rappels d'optimisation convexe

Un problème d'optimisation de manière générale consiste à minimiser (ou maximiser) une fonction objectif $f$ qui est soit soumise à des contraintes d'égalités et/ou des contraintes d'inégalités. Dans le cas où nous avons une fonction objectif convexe, des contraintes d'inégalités convexes et contraintes d'égalité affines, nous sommes en présence d'un problème d'optimisation convexe.

Le problème général est défini par:

$$\begin{align}
 \label{opt}
          \nonumber
               \text{$\min_{\mathbf{x}}$ ~~~} &  f(\mathbf{x}) \\ 
               \text{soumis \`a ~~~} & h_i(\mathbf{x}) = 0, \forall i = 1, ...,m\\
             \nonumber
               \text{~~~~~~~~ et/ou ~~~} & g_j(\mathbf{x}) \le 0, \forall j = 1, ..., p.
\end{align}$$

Avec $g_j, h_i$ des fonctions quelconques, et $\displaystyle f^{\ast} \in \ ]-\infty, +\infty[ \cup \{-\infty, +\infty\}$ le minimum global.

Pour résoudre le problème d'optimisation {eq}`opt`, nous calculons sa dérivée et l'égalons à zèro. Cependant, lorsque les contraintes (d'égalité et d'inégalité ) sont nombreuses, il dévient complexe de le résoudre via cette technique d'égalisation de la dérivée a zéro. C'est la raison pour laquelle il est préférable d'utiliser la méthode de Lagrange afin de résoudre ce type problème dans un sens plus général. A cet effet, appliquons cette méthode au problème d'optimisation {eq}`opt` énoncé plus haut.

En effet, le Lagrangien du problème {eq}`opt` est donné par:

$$\displaystyle \mathcal{L}(\mathbf{x},\lambda,\mu) = f(\mathbf{x}) + \sum_i\lambda_ih_i(\mathbf{x}) + \sum_j\mu_jg_j(\mathbf{x})$$

avec $\displaystyle \lambda \in \mathbb{R}^{m}$, $\mu \in \mathbb{R}^{p}_{+}$ les coefficients du Lagrangien.

La fonction duale associée est la suivante:

:::{div}
:class: center
$\displaystyle q(\lambda,\mu) = \inf_{\mathbf{x} \in \mathcal{X}}\mathcal{L}(\mathbf{x},\lambda,\mu) = \inf_{\mathbf{x} \in \mathcal{X}}\left(f(\mathbf{x}) + \sum_i\lambda_ih_i(\mathbf{x}) + \sum_j\mu_jg_j(\mathbf{x})\right)$
:::

 

On a donc le problème dual (toujours concave):

:::{div}
:class: center
$\displaystyle \max_{\lambda \in \mathbb{R}^{m}, \mu \in \mathbb{R}^{p}_{+}}q(\lambda,\mu)$
:::

$\textbf{Dualité}$

- On pose $\mathbf{d^{\ast}}$ le maximum global du problème dual

- On parle de dualité faible (toujours vraie) si $\displaystyle \mathbf{d^{\ast}} \le \mathbf{f^{\ast}}$

- On parle de dualité forte, i.e $\mathbf{d^{\ast}} = \mathbf{f^{\ast}}$ si:

  - $h_i$ sont affines, $g_j$ sont convexes, et $f$ est convexe

  - Conditions de Slater (il existe une solution $\mathbf{x^*}$ pour laquelle les contraintes d'inégalités sont strictes) est satisfaite.

  - Conditions nécessaires et suffisantes d'optimalité:

    - $\mathbf{x^{\ast}}$ minimises $\mathcal{L}(\mathbf{x},\lambda^{\ast},\mu^{\ast})$

    - \"complementary slackness\": $\displaystyle \forall i, j; \lambda^{\ast}_{j}h_j(\mathbf{x^{\ast}}) = 0$, $\displaystyle \mu^{\ast}_{i}h_i(\mathbf{x^{\ast}}) = 0$

## Exemples de noyaux

Dans cette section, nous allons présenter quelques exemples de méthodes à noyau fréquemment utilisées en apprentissage automatique.

### Noyau linéaire

Le noyau linéaire est le plus simple et son équation est la suivante:

:::{div}
:class: center
$\displaystyle k(\mathbf{x},\mathbf{y}) = \mathbf{x^T}\mathbf{y}$
:::

### Noyau polynomial

Ce noyau est beaucoup utilisé dans le traitement d'image et il est donné par l'équation suivante:

:::{div}
:class: center
$\displaystyle k(\mathbf{x},\mathbf{y}) = (\mathbf{x^T}\mathbf{y} + 1)^d$
:::

Dans le cas où $d=1$, nous retrouvons un Noyau linéaire ($1+\mathbf{x^T}\mathbf{y}$)

### Noyau de Laplace RBF

C'est un noyau à usage général; utilisé lorsqu'il n'y a aucune connaissance préalable sur les données. La formule est: $$\begin{equation*}
        k(\mathbf{x},\mathbf{y}) = \exp\left(-\frac{|| \mathbf{x} - \mathbf{y} ||_{\ell_1}}{\sigma} \right)
\end{equation*}$$

### Noyau Gaussien

C'est un noyau à usage général; utilisé lorsqu'il n'y a aucune connaissance préalable sur les données. La formule est la suivante:

:::{div}
:class: center
$\displaystyle k(\mathbf{x},\mathbf{y}) = \exp \left(-\frac{|| \mathbf{x} - \mathbf{y} ||^2}{2\sigma^2}\right)$
:::

### Noyau hyperbolique tangent (Noyau Sigmoid)

Il est généralement utilisé dans les réseaux de neurones. Son expression est la suivante:

:::{div}
:class: center
$\displaystyle k(\mathbf{x},\mathbf{y}) = \tanh(\kappa \mathbf{x}.\mathbf{y} + c)$,
:::

pour certaines (pas toutes) valeurs de $\kappa > 0$, et $c > 0$.

## Travaux pratiques/méthodes à noyau

### Tutoriel: première session

### Tutoriel: deuxième session
