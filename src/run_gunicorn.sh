#!/usr/bin/env bash

gunicorn --bind 0.0.0.0:8888 --workers 3 --access-logfile=- --log-level=debug --log-file=- wsgi