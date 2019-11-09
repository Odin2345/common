import os
from flask import Blueprint, render_template, request, flash, session
from werkzeug.utils import secure_filename, redirect
from forms import AddMarketForm, FilterMarketForm
from utils import get_data, allowed_file, add_data

supermarket = Blueprint('supermarket',
                        __name__,
                        template_folder='supermarket_templates',
                        static_folder='supermarket_static',
                        static_url_path='/blueprint/supermarket/'
                                        'supermarket_static')


@supermarket.route('/supermarket', methods=['GET'])
def get_all_supermarkets():
    data = get_data("supermarkets.json")
    form = FilterMarketForm()
    if request.args.getlist('location'):
        filtered_data = []
        for elem in data:
            if elem['location'].lower() == \
                    str(request.args.getlist('location')[0]).lower():
                filtered_data.append(elem)
        return render_template('all_supermarkets.html',
                               title='Supermarkets',
                               data=filtered_data,
                               form=form)
    else:
        return render_template('all_supermarkets.html',
                               title='Supermarkets',
                               data=data,
                               form=form)


@supermarket.route('/supermarket', methods=['POST'])
def search_for_supermarkets_by_location():
    data = get_data("supermarkets.json")
    form = FilterMarketForm()
    filtered_data = []
    for elem in data:
        if elem['location'].lower() == str(form.location.data).lower():
            filtered_data.append(elem)
    return render_template('all_supermarkets.html',
                           title='Supermarkets',
                           data=filtered_data,
                           form=form)


@supermarket.route('/add_supermarket', methods=['GET'])
def get_form_to_add_supermarket():
    form = AddMarketForm()
    return render_template('add_supermarket.html',
                           title='Add Supermarket',
                           form=form)


@supermarket.route('/submit_market', methods=['POST'])
def add_supermarket():
    data = get_data("supermarkets.json")
    form = AddMarketForm()
    img_file = request.files['image']

    if form.location.data and form.name.data:
        if len(form.location.data) > 1 and len(form.name.data) > 1 and \
                allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join(supermarket.static_folder, filename))
            supermarket_info = {'id': f'{form.id}{form.name.data}',
                                'name': form.name.data,
                                'location': form.location.data,
                                'img_name': img_file.filename}
            data.append(supermarket_info)
            add_data(data, "supermarkets.json")
            return render_template('all_supermarkets.html',
                                   title='Supermarkets',
                                   data=get_data("supermarkets.json"),
                                   form=FilterMarketForm())

    flash('The data is not correct. Try input again')
    return redirect('add_supermarket')


@supermarket.route('/supermarket/<id_market>', methods=['GET'])
def get_supermarket(id_market):
    for elem in get_data("supermarkets.json"):
        if elem['id'] == id_market:
            session[elem['id']] = True
            return render_template('supermarket_page.html',
                                   id=elem['id'],
                                   title=elem['name'],
                                   src_img=elem['img_name'],
                                   location=elem['location'])
    return redirect('get_error_page')
