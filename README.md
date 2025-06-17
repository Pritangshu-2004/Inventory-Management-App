# 📦 Inventory Manager — Desktop Application

**Inventory Manager** is a PySide6-based desktop inventory management application designed for internal use at India. It allows operators to manage product details, log goods receiving and sales entries, all backed by a local SQLite database. The application includes operator login and is fully functional as a standalone `.exe`.

---

## 🔧 Tech Stack

- **Frontend/UI**: PySide6 (Qt for Python)
- **Backend ORM**: Peewee (SQLite ORM)
- **Database**: SQLite (default, can switch to MySQL)
- **Image Handling**: Pillow
- **Packaging**: PyInstaller for `.exe` creation

---

## 🧩 Features

### ✅ Operator Login
- Secure login interface with two preset operators:
  - `operator1 / pass123`
  - `operator2 / pass456`

### ✅ Product Master Form
- Add and update product data:
  - Barcode, SKU ID, Product Name
  - Category, Subcategory
  - Description, Unit, Price, Tax (%)
  - Product Image (stored in `/assets`)
- Records saved in `Product` table

### ✅ Goods Receiving Form
- Track received goods with:
  - Product, Supplier, Quantity, Unit, Rate
  - Auto-calculated Total, Tax
- Entries saved with timestamp

### ✅ Sales Form
- Log customer product sales:
  - Customer Name, Product, Quantity, Unit, Rate, Tax
  - Total auto-calculated
- Entries saved in `Sale` table

---

## 📁 Project Structure
Inventory-Management-App/
├── assets/ # Folder for uploaded product images
├── database.py # Database connection and setup
├── goods_receiving_form.py # Goods Receiving form UI and logic
├── inventory.db # SQLite database file (generated on first run)
├── login.py # Operator login form and validation
├── main.py # Application entry point
├── models.py # ORM models for Product, Sale, GoodsReceiving
├── product_master_form.py # Product Master form UI and logic
├── requirements.txt # Python dependencies
├── sales_form.py # Sales form UI and logic
└── README.md # Project documentation (this file)



---

## ▶️ How to Run the App

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python main.py
```
### 3. Login Credentials
operator1 / pass123
operator2 / pass456
