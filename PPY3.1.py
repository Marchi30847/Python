# Task1
def cesar_encode(to_cipher, shift):
    ciphered = ""
    for letter in to_cipher:
        if letter.islower():
            ciphered += chr(((ord(letter) - 97 + shift) % 26) + 97)
        elif letter.isupper():
            ciphered += chr(((ord(letter) - 65 + shift) % 26) + 65)

    return ciphered


def cesar_decode(from_cipher, shift):
    deciphered = ""
    for letter in from_cipher:
        if letter.islower():
            deciphered += chr(((ord(letter) - 97 - shift) % 26) + 97)
        elif letter.isupper():
            deciphered += chr(((ord(letter) - 65 - shift) % 26) + 65)

    return deciphered


#print(cesar_decode(cesar_encode("Alex", 12), 12))

#Task2
def store():
    stores = ["Store1", "Store2", "Store3", "Store4", "Store5", "Store6", "Store7"]

    products = [
        {
            "Product name": "Cookies",
            "Manufacturer": "Sweet Treats Inc.",
            "Expiration date": "2025-09-30",
            "Category": "Sweets",
        },
        {
            "Product name": "Apples",
            "Manufacturer": "Fresh Farms",
            "Expiration date": "2025-08-30",
            "Category": "Fruits",
        },
        {
            "Product name": "Milk",
            "Manufacturer": "Dairy Delight",
            "Expiration date": "2025-06-15",
            "Category": "Dairy",
        },
        {
            "Product name": "Bread",
            "Manufacturer": "Baker's Choice",
            "Expiration date": "2025-07-10",
            "Category": "Bakery",
        },
        {
            "Product name": "Chicken",
            "Manufacturer": "Farm Fresh Meats",
            "Expiration date": "2025-05-20",
            "Category": "Meat",
        },
        {
            "Product name": "Orange Juice",
            "Manufacturer": "Citrus Delight",
            "Expiration date": "2025-10-05",
            "Category": "Beverages",
        }
    ]

    prices = [10, 15, 5, 8, 12, 6]

    customers = ["Alex", "Ivan", "Den", "Emily", "Sophia", "Michael", "John"]

    purchased_products = ["Cookies", "Apples", "Milk", "Bread", "Chicken", "Orange Juice"]

    store_product_tuples = []

    for i in range(len(stores)):
        if i % 2 != 0:
            store_product_tuples.append(stores[i])
    for j in range(len(products)):
        if j % 6 == 0:
            store_product_tuples.append(products[j])
    print(store_product_tuples)

    customer_products = {}
    for i in range(len(customers)):
        product_list = []
        if i > 0:
            for j in range(len(products)):
                if j % i == 0:
                    product_list.append(products[j])
        customer_products[customers[i]] = product_list
    print(customer_products)

    product_prices = {}
    if len(products) == len(prices):
        for product, price in zip(products, prices[::-1]):
            product_prices[product["Product name"]] = price
    print(product_prices)

#store()

#Task3
import random

_lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
_uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_lowercase():
    letters = []
    for index, letter in enumerate(_lowercase_letters):
        if index % 2 == 0 or index % 5 == 0:
            letters.append(letter)

    return letters


def get_uppercase():
    letters = []
    for index, letter in enumerate(_uppercase_letters):
        if index % 2 == 0 and index % 3 == 0:
            letters.append(letter)

    return letters


def get_digits():
    digits = []
    for index, letter in enumerate(_digits):
        if index % 2 == 0:
            digits.append(letter)
    for index, letter in enumerate(_digits[::-1]):
        if index % 2 != 0:
            digits.append(letter)

    return digits


def generate_passwords(num_passwords, complexity):
    lowercase = get_lowercase()
    uppercase = get_uppercase()
    digits = get_digits()

    passwords = []
    for _ in range(num_passwords):
        if complexity == 'easy':
            choice_pool = random.choice([lowercase, uppercase, digits])
        elif complexity == 'medium':
            choice_pool = lowercase + uppercase + digits
        elif complexity == 'difficult':
            choice_pool = lowercase + uppercase + digits
        else:
            raise ValueError("Invalid complexity level")

        password = ''
        for _ in range(12):
            password += random.choice(choice_pool)

        passwords.append(password)

    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")


complexity_level = input("Enter password complexity (easy, medium, difficult): ").lower()
generate_passwords(10, complexity_level)
