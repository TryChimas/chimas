#!/usr/bin/env bash

# i have a python 3 virtualenv relative to this repo at venv/

source venv/bin/activate

# update github

git submodule foreach git pull
git commit -a -m "Commit from make.sh at $(date)"
git push

# remove old builds

rm -rf build/
rm -rf chimas.egg-info/
rm -rf dist/

# build

python setup.py sdist bdist

#publish to pypi

twine upload dist/*
