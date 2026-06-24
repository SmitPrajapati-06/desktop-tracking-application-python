import json


CONFIG_FILE = "config/config.json"


def save_token(token):

    data = {
        "token": token
    }

    with open(CONFIG_FILE, "w") as file:
        json.dump(data, file, indent=4)