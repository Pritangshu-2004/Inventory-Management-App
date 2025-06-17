from PySide6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout,
                               QComboBox, QLineEdit, QPushButton, QMessageBox)
from models import Product, Sale

class SalesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales Form")
        self.resize(400, 300)
        self.setup_ui()

    def setup_ui(self):
        v = QVBoxLayout(self)
        f = QFormLayout()
        v.addLayout(f)

        self.product_cb = QComboBox(); self.product_cb.addItems([f"{p.id}-{p.product_name}" for p in Product.select()])
        f.addRow("Product:", self.product_cb)

        self.customer = QLineEdit(); f.addRow("Customer:", self.customer)
        self.qty = QLineEdit(); f.addRow("Quantity:", self.qty)
        self.unit = QLineEdit(); f.addRow("Unit:", self.unit)
        self.rate = QLineEdit(); f.addRow("Unit Rate:", self.rate)
        self.tax = QLineEdit(); f.addRow("Tax %:", self.tax)

        btn = QPushButton("Save")
        btn.clicked.connect(self.save)
        v.addWidget(btn)

    def save(self):
        try:
            pid = int(self.product_cb.currentText().split("-")[0])
            quantity, rate, tax = map(float, [self.qty.text(), self.rate.text(), self.tax.text()])
            total = quantity * rate
            Sale.create(product=pid, customer=self.customer.text(),
                        quantity=quantity, unit=self.unit.text(),
                        rate=rate, total_rate=total, tax=tax)
            QMessageBox.information(self, "Saved", "Sale Recorded")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
