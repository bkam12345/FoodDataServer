#!/bin/bash

sudo apt install python3 python3-pip python3-venv redis-server openssl screen -y

openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout key.pem -out cert.pem -subj "/CN=localhost"

redis-server

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate
python3 manage.py collectstatic --noinput