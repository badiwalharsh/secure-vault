#🔐 SecureVault – Password Generator & Manager

SecureVault is a simple yet powerful Password Generator & Password Manager combo application built with Python and PySide6 (Qt for Python).
It allows you to generate strong passwords and store them securely by category (e.g., Social, Banking, Work).

✨ Features

✅ Generate strong random passwords

✅ Save and manage passwords by category/application

✅ View saved passwords in a table view

✅ SQLite database storage (data/passwords.db)

✅ User-friendly interface built with PySide6

✅ 100% local (no internet dependency)

📂 Project Structure
secure_vault/
│
├── main.py                   # Entry point of the app
│
├── core/                     # Backend logic
│   ├── __init__.py
│   ├── password_generator.py # Password generation logic
│   └── password_manager.py   # Database (SQLite) functions
│
├── ui/                       # User Interface
│   ├── __init__.py
│   └── main_window.py        # Main application window
│
└── data/
    └── passwords.db          # Local SQLite database

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/yourusername/secure-vault.git
cd secure-vault

2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install PySide6

4. Run the app
python main.py

🖥️ Usage

Start the application.

Generate a new password or add your own.

Save it with an application name (e.g., Gmail, Facebook, Bank).

Manage and view your stored passwords in the table.

