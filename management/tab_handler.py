from menu import products

def calculate_tab(mesa: list):
    sum = 0

    for product in mesa:
        find_product = [prod for prod in products if prod["_id"] == product["_id"]]

        print(find_product)

        sum += find_product[0]["price"] * product["amount"]

    return {'subtotal': f"${round(sum, 2)}"}