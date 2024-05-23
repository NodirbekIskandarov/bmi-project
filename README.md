## Getting started

## How to run project locally bash script (Linux, Mac)

### install requirements

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.text
```

### create .env file

```bash
cp .env.example .env
```

### create database

```bash
sudo -u postgres psql
CREATE DATABASE azbo
CREATE USER azbo WITH PASSWORD 'azbo';
ALTER ROLE azbo SET client_encoding TO 'utf8';
ALTER ROLE azbo SET default_transaction_isolation TO 'read committed';
ALTER ROLE azbo SET timezone TO 'Asia/Tashkent';
GRANT ALL PRIVILEGES ON DATABASE azbo TO azbo;
\q
```

### set up .env file with your database credentials

```bash
nano .env
```

### run migrations

```bash
python manage.py migrate
```

### run server

```bash
python manage.py runserver
```
