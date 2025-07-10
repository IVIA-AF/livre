# ivia-af.github.io

- pip install git+https://github.com/d2l-ai/d2l-book
- conda install pandoc
- conda install librsvg
- sudo apt-get install texlive-full

d2lbook build html

<!-- Let’s clear and build again. -->

rm -rf \_build && d2lbook build html

d2lbook build pdf
d2lbook deploy html pdf

<!-- convert latex to md -->
pandoc -s ch1.tex -o ch1.md
