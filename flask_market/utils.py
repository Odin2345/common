import json
import logging


def get_data(filename):
    try:
        with open(filename) as json_file:
            return json.load(json_file)
    except ValueError:
        logging.critical("File 'data.json' contains not valid data")
    except FileNotFoundError:
        logging.critical("File 'data.json' not found")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in \
           {'txt', 'pdf', 'png', 'jpg', 'JPG', 'jpeg', 'gif'}
