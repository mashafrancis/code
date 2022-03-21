#!/bin/bash

git clone https://github.com/mashafrancis/code.git
cd code
git clone -b mkdocs --single-branch https://github.com/mashafrancis/code.git mkdocs
git clone -b scripts --single-branch https://github.com/mashafrancis/code.git scripts

python3 scripts/main.py --mock

cp README.md mkdocs/docs/preface.md
cp STYLEGUIDE.md mkdocs/docs/styleguide.md

cd mkdocs
mkdocs serve
