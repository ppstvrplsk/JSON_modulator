# JSON_modulator


```python
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
```

# Extra
Support * wildcard for a term in position
```python
mymod.value_rename('glossary^*^GlossList', 'new_value')
mymod.value_rename('glossary^*^*^GlossList', 'new_value')
mymod.value_rename('glossary^**^GlossList', 'new_value')
```