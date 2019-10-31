import json
import logging


def get_data():
    try:
        with open("data.json") as file:
            return json.load(file)
    except ValueError:
        logging.critical("File 'data.json' contains not valid data")
    except FileNotFoundError:
        logging.critical("File 'data.json' not found")
