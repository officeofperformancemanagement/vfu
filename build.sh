#!/bin/sh -e

# wipe away any previous builds
rm -fr dist vfu.egg-info

# make sure libraries used for publishing are up to date
python3 -m pip install --upgrade setuptools wheel twine
python3 -m pip install --upgrade twine

python3 setup.py sdist
