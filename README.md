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

