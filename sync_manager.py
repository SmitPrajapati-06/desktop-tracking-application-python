import json
from datetime import datetime

SYNC_FILE = "config/sync.json"


def update_last_sync():

    data = {
        "last_sync":
        datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
    }

    with open(
        SYNC_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def get_last_sync():

    try:

        with open(
            SYNC_FILE,
            "r"
        ) as file:

            data = json.load(file)

            return data.get(
                "last_sync",
                "Never"
            )

    except:

        return "Never"