# Flask API Starter

## Descripción

Starter para generar una API con Flask y Python.

## Setup

``` bash
python -m virtualenv venv
pip install -r requirements.txt
```

## Desarrollo

``` bash
python src/app.py
```

## Producción

``` bash
pip install waitress
waitress-serve --port 5000 --host 0.0.0.0 --call "app:create_app"
```
