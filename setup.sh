#!/usr/bin/env bash

# exit when any command fails
set -o errexit

## Install dependencies via pipls
pip install -r dependencies.txt

## Run migration just in case
python manage.py migrate