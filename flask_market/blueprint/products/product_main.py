import os
from flask import Blueprint, render_template, request, flash, session
from werkzeug.utils import secure_filename, redirect
from forms import AddProductForm, FilterForm
from utils import get_data, allowed_file, add_data

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
            if float(elem['price']) == float(str(
                    request.args.getlist('price')[0])):
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


@products.route('/submit_product', methods=['POST'])
def add_product():
    data = get_data("products.json")
    form = AddProductForm()
    img_file = request.files['image']
    if form.price.data and form.description.data and form.name.data:
        if form.price.data > 0 and len(form.description.data) > 1 and\
                len(form.name.data) > 1 and allowed_file(img_file.filename):

            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join(products.static_folder, filename))
            product_info = {'id': f'{form.id}{form.name.data}',
                            'name': form.name.data,
                            'description': form.description.data,
                            'img_name': img_file.filename,
                            'price': str(form.price.data)}
            data.append(product_info)
            add_data(data, "products.json")
            return render_template('all_products.html',
                                   title='Products',
                                   data=get_data("products.json"),
                                   form=FilterForm())
    flash('The data is not correct. Try input again')
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
