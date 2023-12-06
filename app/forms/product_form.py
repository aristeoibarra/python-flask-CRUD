from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, FloatField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Length


class ProductForm(FlaskForm):
    product_name = StringField(
        "Name",
        validators=[
            DataRequired(),
            Length(min=1, max=64, message="Name must be between 1 and 64 characters"),
        ],
    )
    product_description = StringField(
        "Description",
        validators=[
            DataRequired(),
            Length(
                min=1, max=64, message="Description must be between 1 and 64 characters"
            ),
        ],
    )
    product_stock = IntegerField(
        "Stock",
        validators=[
            DataRequired(),
            NumberRange(min=1, message="Stock must be at least 1"),
        ],
    )
    product_price = DecimalField(
        "Price",
        validators=[
            DataRequired(),
            NumberRange(min=1, message="Price must be at least 1"),
        ],
    )
    product_image = FileField("Image")
