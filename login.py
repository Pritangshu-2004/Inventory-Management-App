from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QGridLayout, QLabel, QMessageBox
from models import Operator
from product_master_form import ProductMasterForm
from goods_receiving_form import GoodsReceivingForm
from sales_form import SalesForm

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operator Login")
        self.resize(300, 120)

        layout = QGridLayout(self)
        layout.addWidget(QLabel("Username:"), 0, 0)
        self.username_input = QLineEdit()
        layout.addWidget(self.username_input, 0, 1)

        layout.addWidget(QLabel("Password:"), 1, 0)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input, 1, 1)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.do_login)
        layout.addWidget(login_btn, 2, 0, 1, 2)

    def do_login(self):
        usr = self.username_input.text()
        pwd = self.password_input.text()
        op = Operator.get_or_none(Operator.username == usr, Operator.password == pwd)
        if op:
            self.navigate_to_main()
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")

    def navigate_to_main(self):
        self.main_widget = QWidget()
        self.main_widget.setWindowTitle("Infoware Inventory")
        layout = QGridLayout(self.main_widget)

        btn_pm = QPushButton("Product Master")
        btn_pm.clicked.connect(self.open_pm)
        layout.addWidget(btn_pm, 0, 0)

        btn_gr = QPushButton("Goods Receiving")
        btn_gr.clicked.connect(self.open_gr)
        layout.addWidget(btn_gr, 0, 1)

        btn_sale = QPushButton("Sales")
        btn_sale.clicked.connect(self.open_sale)
        layout.addWidget(btn_sale, 1, 0)

        self.main_widget.show()
        self.close()

    def open_pm(self):
        self.pm = ProductMasterForm(); self.pm.show()

    def open_gr(self):
        self.gr = GoodsReceivingForm(); self.gr.show()

    def open_sale(self):
        self.sale = SalesForm(); self.sale.show()
