#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf8') as s:
        return json.dump(my_obj, s)
