import logging
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app import db
from app.models import Product
from app.forms import ProductForm

product_controller = Blueprint("product_controller", __name__)


@product_controller.route("/product")
@login_required
def index():
    product = Product.query.all()
    return render_template("product/list.html", key="product", products=product)


@product_controller.route("/product/<int:id>")
@login_required
def show(id):
    form = ProductForm()
    product = Product.query.get(id)
    return render_template(
        "product/show.html", key="product", product=product, form=form
    )


@product_controller.route("/product/add", methods=["GET", "POST"])
@login_required
def store():
    form = ProductForm()

    if form.validate_on_submit():
        new_product = Product(
            product_name=form.product_name.data,
            product_description=form.product_description.data,
            product_stock=form.product_stock.data,
            product_price=form.product_price.data,
            product_image=form.product_image.data,
        )

        db.session.add(new_product)
        db.session.commit()

        flash("product added successfully")
        return redirect(url_for("product_controller.index"))

    return render_template("product/add.html", key="product", form=form)


@product_controller.route("/product-update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
    product = Product.query.get(id)
    form = ProductForm(obj=product)

    if request.method == "POST" and form.validate_on_submit():
        product.product_name = form.product_name.data
        product.product_description = form.product_description.data
        product.product_stock = form.product_stock.data
        product.product_price = form.product_price.data
        product.product_image = form.product_image.data

        db.session.commit()

        flash("Product updated successfully")
        return redirect(url_for("product_controller.index"))

    return render_template(
        "product/edit.html", key="product", product=product, form=form
    )


@product_controller.route("/product/delete/<int:id>", methods=["GET", "POST"])
@login_required
def destroy(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    flash("product deleted successfully")
    return redirect(url_for("product_controller.index"))
