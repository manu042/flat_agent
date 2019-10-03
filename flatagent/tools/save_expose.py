import os
import json
from tools.settings import settings


json_dir_path = os.path.dirname(settings.JSON_FILE_PATH)
if not os.path.exists(json_dir_path):
    os.makedirs(json_dir_path)


def save_expose_details(expose_details):
    new_expose = False
    json_data = read_json_file()

    expose_link = expose_details["expose_link"]
    expose_no = expose_link.split("/")[-1]

    if expose_no not in json_data:
        new_expose = True
        json_data[expose_no] = expose_details

        with open(settings.JSON_FILE_PATH, "w") as fp:
            json.dump(json_data, fp, ensure_ascii=False)

    return new_expose


def read_json_file():
    try:
        with open(settings.JSON_FILE_PATH, "r") as fp:
            data = json.load(fp)
    except:
        data = {}

    return data
