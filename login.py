from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)
from ui.dashboard import DashboardWindow

from database.db import save_user
from config.token_manager import save_token

class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Desktop Tracker Login")
        self.setGeometry(300, 200, 400, 250)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        title = QLabel("Desktop Tracker")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter Email")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")

        self.password_input.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("Login")

        login_button.clicked.connect(self.login)

        layout.addWidget(title)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def login(self):

        email = self.email_input.text()
        password = self.password_input.text()

        if not email or not password:

            QMessageBox.warning(
                self,
                "Error",
                "Please enter Email and Password"
            )
            return

        user_name = email.split("@")[0]

        token = "mock_token_123456"

        save_user(
            user_name,
            email,
            token
        )

        save_token(token)

        self.dashboard = DashboardWindow(
            user_name
        )

        self.dashboard.show()

        self.close()