#!/usr/bin/env bash


[[ -e flight.db ]] && rm flight.db
virtualenv flight_info_venv
source flight_info_venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
