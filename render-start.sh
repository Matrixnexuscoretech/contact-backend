#!/usr/bin/env bash
# Start Gunicorn server
gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
