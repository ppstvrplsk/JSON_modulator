from typing import Union
import json
import os

class JSON_modulator:
    def __init__(self, json):
        self.json = json
        self.temp = self.json

    def key_remove(self, position, key):
        self.temp = self.json
        tags = position.split("^")
        for tag in tags:
            self.temp = self.temp[tag]
        self.temp.pop(key)
        print(json.dumps(self.json,indent=4))



path = os.path.join('examples','example1.json')
with open(path, mode='r', encoding='utf-8') as f:
    json_obj = json.load(f)
mymod=JSON_modulator(json_obj)
mymod.key_remove('glossary^GlossDiv^GlossList', 'GlossEntry')
