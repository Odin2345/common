import os
import json
from flask import Blueprint, render_template, request, flash, session
from werkzeug.utils import secure_filename, redirect
from forms import AddMarketForm, FilterMarketForm
from utils import get_data, allowed_file


supermarket = Blueprint('supermarket',
                        __name__,
                        template_folder='supermarket_templates',
                        static_folder='supermarket_static',
                        static_url_path=
                        '/blueprint/supermarket/supermarket_static')




@supermarket.route('/supermarket', methods=['GET'])
def get_all_supermarkets():
    data = get_data("supermarkets.json")
    form = FilterMarketForm()
    if request.args.getlist('location'):
        filtered_data = []
        for elem in data:
            if elem['location'] == str(request.args.getlist('location')[0]):
                filtered_data.append(elem)
        return render_template('all_supermarkets.html',
                               title='Supermarkets',
                               data=filtered_data,
                               form=form)
    else:
        for elem in data:
            print(elem['name'])
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
        if elem['location'] == str(form.location.data):
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


@supermarket.route('/add_supermarket', methods=['POST'])
def add_supermarket():
    form = AddMarketForm()
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(supermarket.static_folder, filename)
        file.save(path)

        with open("supermarkets.json", 'r') as json_file_read:
            json_file = json.load(json_file_read)
        with open("supermarkets.json", 'w') as json_file_write:
            jf_target = json_file
            market_info = {'id': f'{form.id}{form.name.data}',
                           'name': form.name.data,
                           'location': form.location.data,
                           'img_name': file.filename}
            jf_target.append(market_info)
            json.dump(json_file, json_file_write)

        if form.validate_on_submit():
            flash(f'Add supermarket: name – {form.name.data},'
                  f' location – {form.location.data},'
                  f' image uploaded successfully – {file.filename}')
        return render_template("add_supermarket.html",
                               title="Add supermarket",
                               form=form)
    else:
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
