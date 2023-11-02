#!/bin/sh
./wait-for-it.sh postgres:5432 -t 10 -- echo "postgres is up"
cd src
alembic upgrade head
python3 initial_data.py
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

