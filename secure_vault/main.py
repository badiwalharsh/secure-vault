import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from core.password_manager import init_db


if __name__ == "__main__":
    init_db()  # Make sure database is ready

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
