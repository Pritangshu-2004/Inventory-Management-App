from PySide6.QtWidgets import QApplication
import sys
from database import db
from models import initialize_db
from login import LoginForm

if __name__ == "__main__":
    initialize_db()
    app = QApplication(sys.argv)
    login = LoginForm()
    login.show()
    sys.exit(app.exec())
