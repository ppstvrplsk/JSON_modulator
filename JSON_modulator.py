from typing import Union
import json
import os
import logging

class JSON_modulator:
    def __init__(self, json):
        self._json = json
        self._temp = self._json
    
    @staticmethod
    def _get_path(position, delimiter='^'):
        return position.split(delimiter) 

    def _find_position(self, position: str):
        self._temp = self._json
        position_list = JSON_modulator._get_path(position)

        for key in position_list:
            self._temp = self._temp.get(key)
            if None == self._temp:
                logging.warning(f"Your position '{position}' does not exist.\n\
                                There is not such a key: '{key}'.")
                return None
        return self._temp

    def key_remove(self, position: str, key:str) -> bool:    
        res = self._find_position(position)
        if None == res:
            logging.info(f"I couldn't perform the deletion!")
            return False
        res.pop(key)
        logging.info(f"The key '{key}' is removed from the position '{position}'!")
        return True


    def subjson_append(self, position: str, subjson:dict) -> bool:
        res = self._find_position(position)
        if None == res:
            logging.info(f"I couldn't perform the addition!")
            return False 
        res.update(subjson)
        logging.info(f"Your subjson has added to the position '{position}'!")
        

    def listitem_append(self, position: str, item: Union[str | int | float]) -> bool:
        res = self._find_position(position)
        if None == res:
            logging.info("I couldn't append the item!")
            return False
        res.append(item)
        logging.info(f"I append the item '{item}' to the position '{position}'!")

    def listitem_delete(self, position: str, item) -> bool:
        res = self._find_position(position)
        if None == res:
            logging.info("I couldn't delete the item!")
            return False
        
        positions = []
        for pos,e in enumerate(res): 
            if item == e:
                positions.append(pos)
        positions.reverse()
        for pos in positions:
            del(res[pos])
        
        logging.info(f"I delete the item '{item}' to the position '{position}'!")

    def key_rename(self, position: str, key) -> bool:
        res = self._find_position(position)
        temp = JSON_modulator._get_path(position)
        key_to_be_deleted = temp[-1]
        new_pos = "^".join(temp[:-1])

        if None == res:
            logging.info("I couldn't rename the key!")
            return False
        
        self.key_remove(new_pos, key_to_be_deleted)
        new_res = self._find_position(new_pos)
        new_res[key] = res
        return True
        

    def value_rename(self, position: str, value: Union[str|int|float]) -> bool:
        temp = JSON_modulator._get_path(position)
        target_key = temp[-1]
        new_pos = "^".join(temp[:-1])
        res = self._find_position(new_pos)
        if None == res:
            logging.info("I couldn't delete the item!")
            return False
        res[target_key] = value
        return True




if '__main__' == __name__:
    path = os.path.join('examples','example1.json')
    with open(path, mode='r', encoding='utf-8') as f:
        json_obj = json.load(f)
    

    mymod=JSON_modulator(json_obj)
    mymod.key_remove('glossary^GlossDiv^GlossList^GlossEntry', 'ID')


    my_dict = {
        'my_key1':'value1',
        'my_key2': {
            'my_key3': [2,3,2]
        }
    }
    mymod.subjson_append('glossary^GlossDiv^GlossList', my_dict)


    mymod.listitem_append('glossary^GlossDiv^GlossList^GlossEntry^GlossDef^GlossSeeAlso', "ABC")
    

    mymod.listitem_delete('glossary^GlossDiv^GlossList^GlossEntry^GlossDef^GlossSeeAlso', "GML")
    

    mymod.key_rename('glossary^GlossDiv^GlossList', 'new_GlossList')


    mymod.value_rename('glossary^GlossDiv^new_GlossList', 'new_value')


    print(json.dumps(mymod._json, indent=4))

