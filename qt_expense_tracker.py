import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
from project import add_user, add_transaction, get_transactions, get_expenses, get_income

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Expense Tracker")

        self.user_id = None

        self.username_label = QLabel("Username")
        self.username_input = QLineEdit()

        self.title_label = QLabel("Transaction Title")
        self.title_input = QLineEdit()

        self.amount_label = QLabel("Amount")
        self.amount_input = QLineEdit()

        self.is_income_label = QLabel("Is Income (True/False)")
        self.is_income_input = QLineEdit()

        self.add_user_button = QPushButton("Add User")
        self.add_user_button.clicked.connect(self.add_user)

        self.add_transaction_button = QPushButton("Add Transaction")
        self.add_transaction_button.clicked.connect(self.add_transaction)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.add_user_button)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.title_input)
        self.layout.addWidget(self.amount_label)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.is_income_label)
        self.layout.addWidget(self.is_income_input)
        self.layout.addWidget(self.add_transaction_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def add_user(self):
        username = self.username_input.text()
        self.user_id, message = add_user(username)
        print(message)

    def add_transaction(self):
        if self.user_id is None:
            print("Please add a user first.")
            return

        title = self.title_input.text()
        amount = float(self.amount_input.text())
        is_income = self.is_income_input.text().lower() == 'true'

        add_transaction(self.user_id, amount, is_income, title)
        print("Transaction added successfully.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
