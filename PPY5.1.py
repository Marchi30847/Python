from enum import Enum, auto

"""
class Animal:

    def show_race(self):
        print("Fox")


a = Animal()
a.show_race()
b = Animal()

print(a==a)

class Animal:
    def __init__(self, race, age):
        self.race = race
        self.age = age

a = Animal("Fox", 2)
print(a.race, a.age)
a.legs=4
print(a.legs)

print(a)

class Animal:
    animals = {}
    def __init__(self, race, age,speed):
        self.race = race
        self.age = age
        self.max_speed=speed
        if race in Animal.animals:
            Animal.animals[race] +=1
        else:
            Animal.animals[race] = 1
    def calcualte_distance(self,time):
        print(time*self.max_speed)
    @staticmethod
    def print_animals():
        print(Animal.animals)
    def __str__(self):
        return(self.race+" is "+str(self.age)+" years old and can run up to "+str(self.max_speed)+" km/h")



a=Animal("Fox", 2,4)
b=Animal("Fox", 3,4)
c=Animal("Wolf", 4,7)

a.calcualte_distance(10)
c.calcualte_distance(10)
Animal.print_animals()

print(a)
print(a.__str__())

class Bird(Animal):
    def __init__(self,race,age,speed,max_speed,place):
        super().__init__(race,age,speed)
        self.max_speed=max_speed
        self.place=place
    def move(self):
        if self.place == "cage":
            self.place="outside"
        else:
            self.place="cage"
    def calculate_distance(self,time):
        print((time*self.max_speed)/2)

p=Bird("Chicken",3,4,4,"cage")

a.calcualte_distance(10)
p.calculate_distance(10)
"""


class Article:
    products = []

    def __init__(self, name, price, manufacturer, category, expiration_date):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.category = category
        self.expiration_date = expiration_date

        Article.products.append(self)

    def __str__(self):
        return self.name + " " + str(
            self.price) + " " + self.manufacturer + " " + self.category.__str__() + " " + self.expiration_date

    @staticmethod
    def display_articles():
        for article in Article.products:
            print(article.__str__())

    @staticmethod
    def add_new_product():
        name = input("Enter a product name: ")
        price = input("Enter a product price: ")
        manufacturer = input("Enter a product manufacturer: ")

        category = None
        while category not in Category.values():
            print("Please enter a valid category")
            print(Category.values())
            category = input("Enter a product category: ")

        expiration_date = input("Enter a product expiration date: ")

        new_product = Article(name, price, manufacturer, category, expiration_date)
        print(new_product)


class Category(Enum):
    FRUITS = "Fruits"
    VEGETABLES = "Vegetables"
    DAIRY = "Dairy"
    MEAT = "Meat"
    SEAFOOD = "Seafood"
    BAKERY = "Bakery"
    BEVERAGES = "Beverages"
    SNACKS = "Snacks"
    SWEETS = "Sweets"

    def __str__(self):
        return self.value

    @staticmethod
    def values():
        categories = [c.value for c in Category]
        return categories


class Customer:
    customers = []

    def __init__(self, first_name, last_name, address, age, purchased_products, money):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.age = age
        self.purchased_products = purchased_products
        self.money = money

        Customer.customers.append(self)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.address + " " + str(self.age) + " " + str(
            self.purchased_products) + " " + str(self.money)

    @staticmethod
    def display_customers():
        for customer in Customer.customers:
            print(customer.__str__())

    def add_purchased_product(self, product):
        if self.money < product.price:
            print("Not enough money")
            return
        self.purchased_products.append(product)
        self.money -= product.price


a1 = Article("Apple", 1.5, "FreshFarms", Category.FRUITS, "2025-01-10")
a2 = Article("Milk", 2.0, "DairyCo", Category.DAIRY, "2024-06-15")
a3 = Article("Bread", 1.0, "BakeryHouse", Category.BAKERY, "2024-04-05")
a4 = Article("Salmon", 10.0, "SeaFresh", Category.SEAFOOD, "2024-05-20")
a5 = Article("Chocolate", 3.5, "SweetDelight", Category.SWEETS, "2025-02-14")

Article.display_articles()

# Article.add_new_product()

# Article.display_articles()

c1 = Customer("Bob", "Robertson", "aboba", 41, [], 1)
c1.add_purchased_product(a1)
c1.add_purchased_product(a2)

print(c1.__str__())


def calculate_dijkstra(graph, start):
    distances = {}
    visited = []

    for node in graph:
        distances[node] = float("inf")
    distances[start] = 0

    while len(visited) < len(graph):
        min_node = None

        for node in graph:
            if node in visited:
                continue
            if min_node is None or distances[node] < distances[min_node]:
                min_node = node

        for neighbor in graph[min_node]:
            new_distance = distances[min_node] + graph[min_node][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        visited.append(min_node)

    return distances


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'C': 1},
    'C': {'D': 1},
    'D': {}
}
start = 'A'

result = calculate_dijkstra(graph, start)

for node in result:
    print("The closest path from", start, "to", node, "is", result[node])


class Person:
    people = []

    def __init__(self, name, surname, gender, date_of_birth):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth

        Person.people.append(self)

    def __str__(self):
        return self.name + " " + self.surname + " " + self.gender + " " + self.date_of_birth

    def display_info(self, display_type='list'):
        data = {
            "Name": self.name,
            "Surname": self.surname,
            "Gender": self.gender,
            "Date of Birth": self.date_of_birth
        }
        if display_type == 'list':
            return list(data.values())
        if display_type == 'dict':
            return data
        if display_type == 'tuple':
            return tuple(data.values())
        else:
            return None

    @staticmethod
    def display_people():
        data = {}
        for i, person in enumerate(Person.people):
            data[f"Person{i}"] = person.display_info(display_type='dict')

        return data


class Player(Person):
    class Type(Enum):
        NPC = "NPC"
        Human = "Human"

        def __str__(self):
            return self.value

        @staticmethod
        def values():
            types = [t.value for t in Player.Type]
            return types

    players = []

    def __init__(self, name, surname, gender, date_of_birth, nickname, type, email):
        Person.__init__(self, name, surname, gender, date_of_birth)
        self.nickname = nickname
        self.type = type
        self.email = email

        Player.players.append(self)

    def display_info(self, display_type='list'):
        data = {}
        for key, value in super().display_info(display_type='dict').items():
            data[key] = value

        data["Nickname"] = self.nickname
        data["Type"] = self.type.value
        data["Email"] = self.email

        if display_type == 'list':
            return list(data.values())
        if display_type == 'dict':
            return data
        if display_type == 'tuple':
            return tuple(data.values())
        else:
            return None

    @staticmethod
    def display_players():
        data = {}
        for i, player in enumerate(Player.players):
            data[f"Player{i}"] = player.display_info(display_type='dict')

        return data




person1 = Person("A", "a", "Female", "1990-01-01")
person2 = Person("B", "b", "Male", "1985-12-12")
person3 = Person("C", "c", "Male", "2000-03-05")

player1 = Player("D", "d", "Male", "1992-08-08", "aboba", Player.Type.Human, "d@ex.com")
player2 = Player("E", "e", "Female", "1988-04-11", "denbol", Player.Type.NPC, "e@ex.com")

print("People Info:")
people_info = Person.display_people()
for key, value in people_info.items():
    print(f"{key}: {value}")

print("\nPlayers Info:")
players_info = Player.display_players()
for key, value in players_info.items():
    print(f"{key}: {value}")

print("\nPerson1 Display Info (List):")
print(person1.display_info(display_type='list'))

print("\nPerson1 Display Info (Tuple):")
print(person1.display_info(display_type='tuple'))

print("\nPlayer1 Display Info (Dict):")
print(player1.display_info(display_type='dict'))

print("\nPlayer1 Display Info (List):")
print(player1.display_info(display_type='list'))


