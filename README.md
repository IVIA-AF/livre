# IVIA-AF: Initiative pour la Vulgarisation de l'Intelligence Artificielle en Afrique Francophone

## 🚀 Déploiement sur Vercel avec Analytics Simple

Ce projet est maintenant configuré pour être déployé sur Vercel avec un système d'analytics simple pour suivre les consultations du livre.

d2lbook is built on Sphinx, a Python-based documentation generator


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

check the /Users/kabongo/Workstation/Projects/Book/IVIA.AFRICA/livre project when I run the "d2lbook build html" the produce hltml doesn't rellay mention the equation number correctly when referenced in the document and the citation reference doesn't work 

Different Reference Styles:
:numref: - Shows "Fig. 1" (recommended)
:ref: - Shows the full caption
:cite: - For bibliography references
This is exactly how the d2lbook sample books work, and now your figures have the same professional, clickable references!


✅ What Gets Converted:
LaTeX	d2lbook Markdown
\cite{key}	:cite:key``
\citet{key}	:citet:key``
Fig.~\ref{fig}	:numref:fig_fig_1``
\begin{figure}...\end{figure}	![caption](image.jpg){width="80%"}\n:label:fig_label_1``
\chapter{Title}	# Title
\section{Title}	## Title
\item[•] Text	- • Text
\textbf{text}	**text**
\begin{verbatim}...\end{verbatim}	Code blocks



./quick_convert.sh tex/chapter1.tex content/chapter1.md
./convert_with_pandoc_filter.sh tex/chapter3.tex content/chapter3.md

pandoc -s tex/chapter1.tex -o content/chapter1.md


bash build-with-analytics.sh  

export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

file -bi test.tex

pandoc --from=latex \
       --to=markdown+tex_math_dollars \
       --wrap=none \
       --lua-filter="d2lbook-pandoc-filter.lua" \
       -o test.md test.tex


iconv -f WINDOWS-1252 -t UTF-8 test.tex > test.utf8.tex 

pandoc --from=latex \
    --to=markdown+tex_math_dollars \
    --mathjax \
    --wrap=none \
    --markdown-headings=atx \
    -o content/chapter2.md tex/chapter2.tex


<!-- This fix the issue with '' arround math eq -->
pandoc tex/chapter2.tex \
  -f latex \
  -t commonmark_x+tex_math_dollars \
  --wrap=none \
  --citeproc \
  --metadata=link-citations=true \
  --bibliography=references.bib \
  --filter pandoc-crossref \
  -o content/chapter2.md

pandoc tex/chapter1.tex \
  -f latex \
  -t commonmark_x+tex_math_dollars \
  --wrap=none \
  --citeproc \
  --metadata=link-citations=true \
  --bibliography=references.bib \
  --filter pandoc-crossref \
  -o content/chapter1.md


<!-- Available with pip -->
pandoc 2.12
Compiled with pandoc-types 1.22, texmath 0.12.1.1, skylighting 0.10.4,
citeproc 0.3.0.8, ipynb 0.1.0.1
User data directory: /Users/kabongo/.local/share/pandoc
Copyright (C) 2006-2021 John MacFarlane. Web:  https://pandoc.org
This is free software; see the source for copying conditions. There is no

<!-- Latest  -->
pandoc 3.8
Features: +server +lua
Scripting engine: Lua 5.4
User data directory: /Users/kabongo/.local/share/pandoc
Copyright (C) 2006-2025 John MacFarlane. Web:  https://pandoc.org
This is free software; see the source for copying conditions. There is no
warranty, not even for merchantability or fitness for a particular purpose.



## Issue with latex format 

% \[
% \begin{aligned}
%     \mu_p:\quad &V\rightarrow{\mathbb{R}_+}\\
%     &\mathbf{u}\mapsto \bigg{(}\sum_{i=1}^{n}|u_i|^p\bigg{)}^{\frac{1}{p}}
% \end{aligned}
% \]

\[
\begin{aligned}
    \mu_p:\quad &V\rightarrow{\mathbb{R}_+}\\
    &\mathbf{u}\mapsto \left(\sum_{i=1}^{n}|u_i|^p\right)^{\frac{1}{p}}
\end{aligned}
\]

<!-- parts/comments.html -->
<p>FOOTER OK</p>
<script src="https://utteranc.es/client.js"
        repo="IVIA-AF/livre"
        issue-term="title"
        label="comments"
        theme="preferred-color-scheme"
        crossorigin="anonymous"
        async></script>