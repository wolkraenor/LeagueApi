#!/bin/bash

python --version
export PYTHONPATH=/var/www/

python /var/www/app.py db upgrade
python /var/www/app.py runserver --host 0.0.0.0 --port 80 -d