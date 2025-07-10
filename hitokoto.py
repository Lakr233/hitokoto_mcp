#!/usr/bin/env python3

import json
import os
import random

HITOKOTO_JSON_PATH = os.path.join(os.path.dirname(__file__), "hitokoto.json")
HITOKOTO_ITEMS = []


def load_hitokoto_items() -> None:
    global HITOKOTO_ITEMS
    if not HITOKOTO_ITEMS:
        try:
            with open(HITOKOTO_JSON_PATH, "r", encoding="utf-8") as f:
                HITOKOTO_ITEMS = json.load(f)
        except FileNotFoundError:
            print(f"[-] error: {HITOKOTO_JSON_PATH} not found.")
        except json.JSONDecodeError:
            print(f"[-] error: failed to decode JSON from {HITOKOTO_JSON_PATH}.")


def read_hitokoto() -> str:
    #
    # {
    #   "id": 1082,
    #   "uuid": "ab89b12e-359b-4cfe-b50d-de35a20bf928",
    #   "hitokoto": "众里寻他千百度，蓦然回首，那人却在，灯火阑珊处。",
    #   "type": "i",
    #   "from": "青玉案·元夕",
    #   "from_who": null,
    #   "creator": "131",
    #   "creator_uid": 146,
    #   "reviewer": 0,
    #   "commit_from": "web",
    #   "created_at": "1481559051",
    #   "length": 24
    # },
    #
    random_index = random.randint(0, len(HITOKOTO_ITEMS) - 1)
    item = HITOKOTO_ITEMS[random_index]
    hitokoto = item.get("hitokoto", "unavailable")
    return hitokoto


if __name__ == "__main__":
    load_hitokoto_items()
    print(read_hitokoto())
