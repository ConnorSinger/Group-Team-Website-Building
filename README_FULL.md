# Cook-Up (Phase 1) — Complete Setup & Usage

Cook-Up is a Flask web application for posting, searching, and browsing recipes with a MySQL backend. This README includes step-by-step, cross-platform instructions (Linux, macOS, Windows) so anyone — beginner or expert — can run the project locally.

## What you'll find in this repository

- `app.py` — Flask application and route handlers
- `database/` — Database utilities, `setup_database.sh`, and sample SQL
- `database/recipes/` — Python helpers for recipe CRUD and interactive scripts
- `templates/` — HTML templates used by Flask
- `static/` — Static assets (CSS, images)
- `requirements.txt` — Python dependencies
- `tests/` — pytest unit tests

---

## System requirements (summary)

Minimum (for local development):
- CPU: 1 core
- RAM: 2 GB (4 GB recommended)
- Disk: 200 MB free + space for MySQL data

Software (cross-platform):
- Python 3.10+ (3.11 recommended)
- pip
- MySQL or MariaDB server (MySQL 5.7+ / 8.0+ recommended)
- Git (optional)

Notes:
- On Windows, install Python from python.org and enable "Add Python to PATH".
- On macOS, Homebrew users can install Python and MySQL via `brew`.

---

## Step-by-step setup (for any skill level)

Follow these numbered steps. Commands are shown for Linux/macOS; Windows notes follow each section.

### 1) Get the project files

If you already have the folder, skip this; otherwise:

```bash
git clone <repo-url> cookup
cd cookup
```

Windows: use Git Bash or PowerShell.

### 2) Install Python and pip

Linux (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
```

macOS (Homebrew):

```bash
brew install python
```

Windows: download Python 3.10+ from https://python.org and enable "Add Python to PATH".

Verify:

```bash
python3 --version
pip3 --version
```

If your system uses `python`/`pip` instead of `python3`/`pip3`, use those commands.

### 3) Install and start MySQL

Linux (Ubuntu):

```bash
sudo apt install -y mysql-server
sudo systemctl enable --now mysql
```

macOS (Homebrew):

```bash
brew install mysql
brew services start mysql
```

Windows: install MySQL via the MySQL Installer or XAMPP and start the MySQL service from the Services panel or XAMPP control panel.

Check MySQL is running:

```bash
# Linux/macOS
sudo systemctl status mysql
pgrep -x mysqld || echo "mysqld not running"
```

Windows: confirm the MySQL service is running in Services or XAMPP.

### 4) Create the database and a DB user (recommended)

The app currently uses a database named `fall2025_482cook` and the DB user `connorsinger`. You can either create that user or edit `app.py` to use different credentials.

Open a MySQL shell as root (or a user with privileges):

```bash
sudo mysql
```

Then run these SQL statements (replace `YOUR_PASSWORD`):

```sql
CREATE DATABASE IF NOT EXISTS fall2025_482cook;
CREATE USER IF NOT EXISTS 'connorsinger'@'localhost' IDENTIFIED BY 'YOUR_PASSWORD';
GRANT ALL PRIVILEGES ON fall2025_482cook.* TO 'connorsinger'@'localhost';
FLUSH PRIVILEGES;
```

If you prefer a different username/password, update the DB connection parameters in `app.py` and in `database/setup_database.sh` if you use the helper script.

### 5) (Optional) Load sample data with the included script

From the project root:

```bash
cd database
bash setup_database.sh samples
```

This runs `scripts/add_sample_recipes.sql` to populate sample recipes. The script expects the database and a `connorsinger` user (or adjust the script for your credentials).

Windows: use Git Bash or WSL to run the bash script, or manually run the SQL file in MySQL Workbench.

### 6) Create and activate a Python virtual environment

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

When the venv is active, your prompt will include `(.venv)`.

### 7) Install Python dependencies

With the virtualenv active, run:

```bash
pip install -r requirements.txt
```

If you see an error about pip, first run:

```bash
pip install --upgrade pip
```

### 8) Configure application secrets and DB credentials (recommended)

By default `app.py` contains DB credentials for a local user `connorsinger`. You can edit `app.py` to use environment variables. A quick approach:

Linux/macOS:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
export DB_USER=connorsinger
export DB_NAME=fall2025_482cook
# or set a custom password if you added one
```

Windows (PowerShell):

```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
```

You can also add a `.env` and use `python-dotenv` to load variables automatically (the `requirements.txt` includes `python-dotenv`).

Also set a secure Flask secret key in `app.py` or via environment variable before running in any environment where session integrity matters.

### 9) Start the Flask application

Recommended (development):

```bash
flask run --host=127.0.0.1 --port=5000
```

Or run with Python directly if you prefer the module runner:

```bash
python -m flask run
```

Open your browser: http://127.0.0.1:5000

### 10) Create an account and use the app

- Visit `/register` or use the "Create Account" link to register a new user.
- Log in from the main page. Posting recipes requires a logged-in session.
- Use the search, favorites, and recipe pages from the UI.

---

## Running tests

The repository includes pytest tests. With the virtual environment active:

```bash
pytest -q
```

If tests fail due to DB connectivity, ensure MySQL is running and the test DB configuration is available.

---

## Troubleshooting (common issues)

- Can't connect to MySQL: Verify MySQL service is running and credentials match. Try:

```bash
mysql -u connorsinger -p -D fall2025_482cook
```

- ModuleNotFoundError for mysql: Ensure dependencies were installed inside the active virtualenv: `pip install -r requirements.txt`.
- Port 5000 already in use: change port with `flask run --port 5001` or stop the conflicting process.
- Permission denied running `setup_database.sh`: ensure script is executable (`chmod +x database/setup_database.sh`) and run in a shell that supports bash.

---

## Security notes

- Passwords are currently stored in plain text in the sample app. For production, always hash passwords (e.g. `werkzeug.security.generate_password_hash`) and never store raw passwords.
- Do not expose this app to the public internet without HTTPS, proper authentication hardening and input validation.

---

## Recommended next steps (low-risk improvements I can implement)

1. Move DB credentials into environment variables and update `app.py` to read them.
2. Add a `.env.example` showing the environment variables to set.
3. Add a small `run.sh` helper to set environment variables and start Flask.

If you want, I can apply any of the above changes now.

---

**Files added/updated by this step:**
- `README_FULL.md` (this file)
- `requirements.txt` (created/updated)

**Last updated:** October 2025
