import os
import shutil
from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                               QTextEdit, QGridLayout, QFileDialog, QMessageBox, QComboBox)
from models import Product, db
from PIL import Image

class ProductMasterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Master Form")
        self.resize(600, 400)

        self.image_path = None
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout(self)

        fields = [
            ("Barcode", "barcode"),
            ("SKU ID", "sku"),
            ("Category", "category"),
            ("Subcategory", "subcategory"),
            ("Name", "name"),
            ("Description", "desc"),
            ("Tax (%)", "tax"),
            ("Price", "price"),
            ("Unit", "unit"),
        ]

        self.inputs = {}
        for i, (label, key) in enumerate(fields):
            layout.addWidget(QLabel(label + ":"), i, 0)
            if key == "desc":
                widget = QTextEdit()
            else:
                widget = QLineEdit()
            self.inputs[key] = widget
            layout.addWidget(widget, i, 1)

        img_btn = QPushButton("Upload Image")
        img_btn.clicked.connect(self.upload_image)
        layout.addWidget(img_btn, len(fields), 0, 1, 2)

        save_btn = QPushButton("Save Product")
        save_btn.clicked.connect(self.save_product)
        layout.addWidget(save_btn, len(fields)+1, 0, 1, 2)

    def upload_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Choose Product Image", "", "Images (*.png *.jpg)")
        if path:
            self.image_path = path
            QMessageBox.information(self, "Uploaded", os.path.basename(path))

    def save_product(self):
        data = {k: self.inputs[k].text() for k in self.inputs}
        try:
            prod = Product.create(
                barcode=data["barcode"], sku_id=data["sku"],
                category=data["category"], subcategory=data["subcategory"],
                product_image="", product_name=data["name"],
                description=self.inputs["desc"].toPlainText(),
                tax=float(data["tax"]), price=float(data["price"]),
                unit=data["unit"]
            )
            if self.image_path:
                assets = os.path.join(os.getcwd(), "assets")
                os.makedirs(assets, exist_ok=True)
                ext = os.path.splitext(self.image_path)[1]
                out = os.path.join(assets, f"prod_{prod.id}{ext}")
                shutil.copy(self.image_path, out)
                prod.product_image = out
                prod.save()
            QMessageBox.information(self, "Success", "Product saved.")
            self.clear_inputs()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def clear_inputs(self):
        for widget in self.inputs.values():
            if isinstance(widget, QLineEdit):
                widget.clear()
            else:
                widget.clear()
        self.image_path = None
