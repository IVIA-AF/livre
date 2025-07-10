# ivia-af.github.io

- pip install git+https://github.com/d2l-ai/d2l-book
- conda install pandoc librsvg
- sudo apt-get install texlive-full

d2lbook build html

<!-- Let’s clear and build again. -->

d2lbook build pdf

rm -rf \_build && d2lbook build pdf

rm -rf \_build && d2lbook build html && d2lbook build pdf

rm -rf \_build && d2lbook build html && d2lbook build pdf && d2lbook deploy html pdf

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