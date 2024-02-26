#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from jsonschema import validate


if __name__ == "__main__":
    schema = {
        "type": "object",
        "properties": {
            "name_of_product": {"type": "string"},
            "name_of_market": {"type": "string"},
            "value": {"type": "number"},
        },
    }

    with open("products.json", "r", encoding="utf-8") as fin:
        a = json.load(fin)
        for i in a:
            validate(instance=i, schema=schema)
