from acme import Product
import random


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(num_products=30):
    product_list = []
    for n in range(num_products):
        adjective = random.choice(ADJECTIVES)
        noun = random.choice(NOUNS)
        name = adjective + " " + noun
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        product_list.append(Product(name, price, weight, flammability))

    return product_list


def inventory_report(product_list):
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")

    # Get unique name count by casting to a set and getting the length:
    names_count = len(set([product.name for product in product_list]))
    print("Unique product names:", names_count)

    # Find average price, weight and flammability
    # (would be easier with math library but whatever)
    price_sum = 0
    weight_sum = 0
    flammability_sum = 0
    for product in product_list:
        price_sum += product.price
        weight_sum += product.weight
        flammability_sum += product.flammability
    price_average = price_sum / len(product_list)
    weight_average = flammability_sum / len(product_list)
    flammability_average = flammability_sum / len(product_list)

    print("Average price:", price_average)
    print("Average weight:", weight_average)
    print("Average flammability:", flammability_average)


if __name__ == '__main__':
    inventory_report(generate_products())
