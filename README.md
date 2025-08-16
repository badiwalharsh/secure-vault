# 🔐 SecureVault – Password Generator & Manager
A minimal desktop app in Python (PySide6) to generate strong passwords and save them by category.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![GUI](https://img.shields.io/badge/GUI-PySide6-informational)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features
- Generate strong random passwords
- Save passwords by category/application
- View all saved passwords in a table
- 100% local storage (SQLite)

## 📸 Screenshots

| Main Window | Generate Password | Saved Passwords |
|-------------|-------------------|-----------------|
| ![Main](screenshots/main_window.png) | ![Generate](screenshots/generate.png) | ![Saved](screenshots/saved.png) |

## 🧰 Tech Stack
- Python 3.10+
- PySide6 (Qt for Python)
- SQLite (built-in)

## 📂 Project Structure
secure_vault/
├─ main.py
├─ core/
│  ├─ __init__.py
│  ├─ password_generator.py
│  └─ password_manager.py
├─ ui/
│  ├─ __init__.py
│  └─ main_window.py
└─ data/
   └─ passwords.db  (auto-created)

## ✅ Prerequisites
- Python 3.10 or newer
- Check your version:
```bash
python --version.

## Installation
- Use fenced code blocks so GitHub shows a **copy** button automatically.

```md
## ⚙️ Installation
```bash
# 1) Clone
git clone https://github.com/<your-username>/secure-vault.git
cd secure-vault

# 2) Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3) Install dependency
pip install PySide6

## Run the app

```md
## ▶️ Run
```bash
python main.py
