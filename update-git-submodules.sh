#!/usr/bin/env bash

# update git

git submodule foreach git pull
git commit -a -m "Commit from update-git-submodule.sh at $(date)"
git push

