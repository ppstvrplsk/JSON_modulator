from typing import Union
import json
import os

class JSON_modulator:
    def __init__(self, json):
        self.json = json

    def key_remove(self, position: str, key:str) -> bool:
        pass

    def subjson_add(self, position: str, subjson:dict) -> bool:
        pass

    def listitem_append(self, position: str, item: Union[str | int | float]) -> bool:
        pass

    def listitem_delete(self, position: str, item) -> bool:
        pass

    def key_rename(self, position: str, key) -> bool:
        pass

    def value_rename(self, position: str, key_value: dict) -> bool:
        pass






if '__main__' == __name__:
    path = os.path.join('examples','example1.json')
    with open(path, mode='r', encoding='utf-8') as f:
        json_obj = json.load(f)
    mymod=JSON_modulator(json_obj)
    mymod.key_remove('glossary^GlossDiv^GlossList', 'ID')

    my_dict = {
        'my_key1':'value1',
        'my_key2': {
            'my_key3': [2,3,2]
        }
    }
    mymod.subjson_add('glossary^GlossDiv^GlossList', my_dict)
    mymod.listitem_append('glossary^GlossDiv^GlossList^GlossEntry^GlossDef^GlossSeeAlso', "ABC")
    mymod.listitem_delete('glossary^GlossDiv^GlossList^GlossEntry^GlossDef^GlossSeeAlso', "GML")
    mymod.key_rename('glossary^GlossDiv^GlossList', 'new_key')
    mymod.value_rename('glossary^GlossDiv^GlossList', 'new_value')

