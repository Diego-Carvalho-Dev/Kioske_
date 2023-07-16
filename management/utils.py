from menu import products

def get_most_commom_type():
    types_list = [product['type'] for product in products]

    type_name = ''
    count = 0

    for type in types_list:
        new_count = types_list.count(type)
        
        
        if new_count > count:
            count = new_count
            type_name = type

    return type_name

def get_avg_price():
    sum = 0

    for product in products:
        sum += product['price']

    avg = round((sum / len(products)), 2)

    return avg

def id_generate(products):
    id = 1

    if len(products) > 0:

        _ids = [product['_id'] for product in products]

        while id < len(_ids):
            if not _ids.count(id):
                return id
            else:
                id += 1
    else:
        return 1
        
    return id + 1

def check_key(dict: dict, *keys: str):

    dict_keys = list(dict.keys())

    for key in keys:
        if not dict_keys.count(key):
            raise KeyError(f'field {key} is required')
        
