#!/bin/bash
VENV_DIR=venv
python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate
pip install --upgrade pip --no-cache-dir
pip install -r requirements.txt --no-cache-dir
cd urlabridge
python manage.py migrate
echo "Please create a super user account"
python manage.py createsuperuser
