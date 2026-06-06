# django-project-1

Django clothing catalog site (PostgreSQL locally, SQLite in GitHub Codespaces).

## Run locally (Windows + PostgreSQL)

1. Start PostgreSQL:
   ```bat
   start_postgres.bat
   ```
2. Install dependencies and seed data (first time only):
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py seed_data --per-file 3
   ```
3. Run the server:
   ```bash
   python manage.py runserver
   ```
4. Open: http://127.0.0.1:8000/

## Run in GitHub Codespaces

1. Open the repo on GitHub → **Code** → **Codespaces** → **Create codespace**
2. Wait for the post-create setup (install, migrate, seed)
3. In the terminal:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
4. Go to the **Ports** tab → port **8000** → set visibility to **Public** → open the forwarded URL

## Environment variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `USE_LOCAL_DB` | `true` | Use local PostgreSQL when `true` |
| `POSTGRES_DB` | `tshirtpowvc_db` | Database name |
| `POSTGRES_USER` | `postgres` | Database user |
| `POSTGRES_PASSWORD` | `postgres` | Database password |
| `POSTGRES_HOST` | `localhost` | Database host |
| `POSTGRES_PORT` | `5432` | Database port |

In Codespaces, `CODESPACES=true` is set automatically and SQLite is used instead.
