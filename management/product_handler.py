from menu import products
from .utils import get_most_commom_type, get_avg_price, id_generate, check_key

def id_generate(menu):
    if len(menu) > 0:
        return max(product['_id'] for product in menu) + 1
    else:
        return 1


def get_product_by_id(id: int):
    if type(id) != int:
        raise TypeError("product id must be an int")

    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(types: str):
    if type(types) != str:
        raise TypeError("product type must be a str")

    return [product for product in products if product["type"] == types]


def add_product(menu: list, **product):
    check_key(product, "description", "price", "rating", "title", "type")

    product['_id'] = id_generate(menu)

    new_product = product.copy()
    menu.append(new_product)

    return new_product



def menu_report():
    preco_medio = get_avg_price()
    tipo_mais_comum = get_most_commom_type()
    contagem_de_produtos = len(products)

    return f"Products Count: {contagem_de_produtos} - Average Price: ${preco_medio} - Most Common Type: {tipo_mais_comum}"

