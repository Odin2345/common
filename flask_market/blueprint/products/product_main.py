import os
import json
from flask import Blueprint, render_template, request, flash, session
from werkzeug.utils import secure_filename, redirect
from forms import AddProductForm, FilterForm
from utils import get_data, allowed_file

products = Blueprint('products',
                     __name__,
                     template_folder='product_templates',
                     static_folder='product_static',
                     static_url_path='/blueprint/products/product_static', )




@products.route('/product', methods=['GET'])
def get_all_products():
    data = get_data("products.json")
    form = FilterForm()
    if request.args.getlist('price'):
        filtered_data = []
        for elem in data:
            if elem['price'] == str(request.args.getlist('price')[0]):
                filtered_data.append(elem)
        return render_template('all_products.html',
                               title='Products',
                               data=filtered_data,
                               form=form)
    else:
        return render_template('all_products.html',
                               title='Products',
                               data=data,
                               form=form)


@products.route('/product', methods=['POST'])
def search_products_by_price():
    data = get_data("products.json")
    form = FilterForm()
    filtered_data = []
    for elem in data:
        if elem['price'] == str(form.price.data):
            filtered_data.append(elem)
    return render_template('all_products.html',
                           title='Products',
                           data=filtered_data,
                           form=form)


@products.route('/add_product', methods=['GET'])
def get_form_to_add_product():
    form = AddProductForm()
    return render_template('add_product.html',
                           title='Add product',
                           form=form)


@products.route('/add_product', methods=['POST'])
def add_product():
    form = AddProductForm()
    img_file = request.files['file']
    if img_file and allowed_file(img_file.filename):
        filename = secure_filename(img_file.filename)
        path = os.path.join(products.static_folder, filename)
        img_file.save(path)

        with open("products.json", 'r') as json_file_read:
            json_file = json.load(json_file_read)
        with open("products.json", 'w') as json_file_write:
            jf_target = json_file
            product_info = {'id': f'{form.id}{form.name.data}',
                            'name': form.name.data,
                            'description': form.description.data,
                            'img_name': img_file.filename,
                            'price': str(form.price.data)}
            jf_target.append(product_info)
            json.dump(json_file, json_file_write)

        if form.validate_on_submit():
            flash(f'Add product: name – {form.name.data},'
                  f' description – {form.description.data},'
                  f' price – {form.price.data} $,'
                  f' photo uploaded successfully – {img_file.filename}')
        return render_template("add_product.html",
                               title="Add product",
                               form=form)
    else:
        return redirect('add_product')


@products.route('/product/<id_product>', methods=['GET'])
def get_product(id_product):
    for elem in get_data("products.json"):
        if elem['id'] == id_product:
            session[elem['id']] = True
            return render_template('product_page.html',
                                   id=elem['id'],
                                   title=elem['name'],
                                   src_img=elem['img_name'],
                                   description=elem['description'],
                                   price=elem['price'])
    return redirect('get_error_page')
