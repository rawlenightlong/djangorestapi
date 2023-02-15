#!/usr/bin/env bash

# exit an error
set -o errexit

# install dependencies
pip install -r dependencies.txt

# run migrations in case any migrations hadn't been run yet
python manage.py migrate