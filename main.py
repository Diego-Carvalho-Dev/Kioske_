from management import menu_report, add_product, calculate_tab
from management.product_handler import get_product_by_id, get_products_by_type

if __name__ == "__main__":
    menu_report()
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "description": "Sanduiche de Python",
        "type": "fast-food",
        "rating": 5
    }
    new_list = []
    add_product([], **new_product)
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    calculate_tab(table_1)

    product_id = 1
    product = get_product_by_id(product_id)
    print(product)

    product_type = "fast-food"
    products = get_products_by_type(product_type)
    print(products)
