from app import db


class Product(db.Model):
    __tablename__ = "product"

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64))
    product_description = db.Column(db.String(64))
    product_stock = db.Column(db.Integer)
    product_price = db.Column(db.Float)
    product_image = db.Column(db.String(64), nullable=True)

    def __init__(
        self,
        product_name,
        product_description,
        product_stock,
        product_price,
        product_image,
    ):
        self.product_name = product_name
        self.product_description = product_description
        self.product_stock = product_stock
        self.product_price = product_price
        self.product_image = product_image
