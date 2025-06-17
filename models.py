from peewee import *
from database import db

class BaseModel(Model):
    class Meta:
        database = db

class Operator(BaseModel):
    username = CharField(unique=True)
    password = CharField()

class Product(BaseModel):
    barcode = CharField()
    sku_id = CharField()
    category = CharField()
    subcategory = CharField()
    product_image = CharField(null=True)
    product_name = CharField()
    description = TextField()
    tax = FloatField()
    price = FloatField()
    unit = CharField()

class GoodsReceiving(BaseModel):
    product = ForeignKeyField(Product, backref='received')
    supplier = CharField()
    quantity = FloatField()
    unit = CharField()
    rate = FloatField()
    total_rate = FloatField()
    tax = FloatField()

class Sale(BaseModel):
    product = ForeignKeyField(Product, backref='sales')
    customer = CharField()
    quantity = FloatField()
    unit = CharField()
    rate = FloatField()
    total_rate = FloatField()
    tax = FloatField()

def initialize_db():
    db.connect()
    db.create_tables([Operator, Product, GoodsReceiving, Sale], safe=True)
    if Operator.select().count() == 0:
        Operator.create(username="operator1", password="pass123")
        Operator.create(username="operator2", password="pass456")
        print("Inserted default operators.")

if __name__ == "__main__":
    initialize_db()
