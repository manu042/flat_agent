import json

JSON_FILE = "real_estate.json"


def save_expose_details(expose_details):
    new_expose = False
    json_data = read_json_file()

    expose_link = expose_details["expose_link"]
    expose_no = expose_link.split("/")[-1]

    if expose_no not in json_data:
        new_expose = True
        json_data[expose_no] = expose_details

        with open("real_estate.json", "w") as fp:
            json.dump(json_data, fp, ensure_ascii=False)

    return new_expose


def read_json_file():
    try:
        with open(JSON_FILE, "r") as fp:
            data = json.load(fp)
    except:
        data = {}

    return data