from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from core.password_generator import generate_password
from core.password_manager import save_password, get_passwords


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure Vault - Basic")
        self.resize(600, 400)
        self._build_ui()

    def _build_ui(self):
        container = QWidget()
        layout = QVBoxLayout()

        # Category
        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("Enter category (e.g., Gmail)")
        layout.addWidget(QLabel("Category:"))
        layout.addWidget(self.category_input)

        # Username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username/email")
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)

        # Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Generated password will appear here")
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)

        # Buttons
        btn_generate = QPushButton("Generate Password")
        btn_generate.clicked.connect(self.handle_generate)
        layout.addWidget(btn_generate)

        btn_save = QPushButton("Save Password")
        btn_save.clicked.connect(self.handle_save)
        layout.addWidget(btn_save)

        btn_load = QPushButton("Show All Passwords")
        btn_load.clicked.connect(self.handle_load)
        layout.addWidget(btn_load)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Category", "Username", "Password"])
        layout.addWidget(self.table)

        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_generate(self):
        password = generate_password(12)
        self.password_input.setText(password)

    def handle_save(self):
        category = self.category_input.text().strip()
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not category or not username or not password:
            QMessageBox.warning(self, "Error", "All fields are required!")
            return

        save_password(category, username, password)
        QMessageBox.information(self, "Success", "Password saved successfully!")

        self.category_input.clear()
        self.username_input.clear()
        self.password_input.clear()

    def handle_load(self):
        data = get_passwords()
        self.table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(value))
