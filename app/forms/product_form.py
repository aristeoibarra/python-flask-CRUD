from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, FloatField, DecimalField
from wtforms.validators import DataRequired, NumberRange


class ProductForm(FlaskForm):
    product_name = StringField(
        "Name",
        validators=[DataRequired()],
    )
    product_description = StringField("Description", validators=[DataRequired()])
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
