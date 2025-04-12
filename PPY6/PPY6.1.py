"""
from types import NoneType

import numpy

a=numpy.array([1,2,3],dtype="int8")
b=numpy.array([[1,2,3],[4,5,6]])

for i in a:
    print(i)

print(a.dtype)
print(a.size)

import pandas as pd
people_data=[
    ["John","Smith",2000,29],
    ["Kate","Smith",3000,28]
]
df1=pd.DataFrame(people_data)
print(df1)
people_data_headers=["name","surname","salary","age"]
df2=pd.DataFrame(people_data,columns=people_data_headers)
print(df2)

f=open("test.txt","r")
print(f.read())
f=open("test.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
f=open("test.txt","r")
for i in f:
    print(i,end="")
f.close()
f=open("test.txt","a")
f.write("\nSomething")
f=open("test.txt","r")
print(f.read())
f.close()
f=open("test.txt","w")
f.write("I deleted whole content")
f=open("test.txt","r")
print(f.read())

def asd():
    try:
        print("x")
        return 5
    except TypeError:
        print("Error2")
    except:
        print("Error1")
    finally:
        print("Finally")
print(asd())

import os

ph="./projects"
os.mkdir(ph)
"""


class Article:
    ID_GENERATOR = 1

    def __init__(self, id, name, price, manufacturer, category, expiration_date):
        self._id = id
        self._name = name
        self._price = price
        self._manufacturer = manufacturer
        self._category = category
        self._expiration_date = expiration_date

    def __str__(self):
        return f"{self.id} {self.name} {self.price} {self.manufacturer} {self.category} {self.expiration_date}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"name={repr(self.name)}, "
            f"price={self.price}, "
            f"manufacturer={repr(self.manufacturer)}, "
            f"category={repr(self.category)}, "
            f"expiration_date={repr(self.expiration_date)}"
            f")"
        )

    @staticmethod
    def generate_id():
        current_id = Article.ID_GENERATOR
        Article.ID_GENERATOR += 1
        return current_id

    @staticmethod
    def safe_generate_id(articles):
        article_id = Article.generate_id()
        while article_id in [a.id for a in articles]:
            article_id = Article.generate_id()

        return article_id


    @property
    def id(self): return self._id

    @id.setter
    def id(self, value): self._id = value

    @property
    def name(self): return self._name

    @name.setter
    def name(self, value): self._name = value

    @property
    def price(self): return self._price

    @price.setter
    def price(self, value): self._price = value

    @property
    def manufacturer(self): return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value): self._manufacturer = value

    @property
    def category(self): return self._category

    @category.setter
    def category(self, value): self._category = value

    @property
    def expiration_date(self): return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value): self._expiration_date = value


class ArticleRepository:
    FILE = "data.txt"

    @staticmethod
    def persist_article(article):
        article_ids = [a.id for a in ArticleRepository.read_articles()]

        if article.id in article_ids:
            raise ValueError("Unique id is required")

        with open(ArticleRepository.FILE, "a") as f:
            f.write(repr(article) + "\n")

    @staticmethod
    def read_articles():
        articles = []
        with open(ArticleRepository.FILE, "r") as f:
            for line in f.readlines():
                if line.strip():
                    try:
                        article = eval(line.strip())
                        articles.append(article)
                    except Exception as e:
                        print(f"Error using eval to create an object : {e}")
        return articles

    @staticmethod
    def delete_article(article):
        articles = ArticleRepository.read_articles()
        articles = [a for a in articles if a.id != article.id]
        with open(ArticleRepository.FILE, "w") as f:
            for a in articles:
                f.write(repr(a) + "\n")

    @staticmethod
    def update_article(article_id, new_article):
        articles = ArticleRepository.read_articles()
        for i, a in enumerate(articles):
            if a.id == article_id:
                new_article.id = article_id
                articles[i] = new_article
                break

        with open(ArticleRepository.FILE, "w") as f:
            for a in articles:
                f.write(repr(a) + "\n")


article1 = Article(
    id=Article.generate_id(),
    name="Milk",
    price=2.5,
    manufacturer="DairyCo",
    category="Dairy",
    expiration_date="2025-05-01"
)

article2 = Article(
    id=Article.generate_id(),
    name="Apple",
    price=0.8,
    manufacturer="FruitFarm",
    category="Fruits",
    expiration_date="2025-04-15"
)

article3 = Article(
    id=Article.generate_id(),
    name="Bread",
    price=1.5,
    manufacturer="Bakers Ltd.",
    category="Bakery",
    expiration_date="2025-04-10"
)

article4 = Article(
    id=None,
    name="Croissant",
    price=3,
    manufacturer="KyivChlib",
    category="Bakery",
    expiration_date="2025-04-11"
)

try:
    ArticleRepository.persist_article(article1)
except Exception as e:
    print(e)
try:
    ArticleRepository.persist_article(article2)
except Exception as e:
    print(e)
try:
    ArticleRepository.persist_article(article3)
except Exception as e:
    print(e)


for a in ArticleRepository.read_articles():
    print(a)

ArticleRepository.delete_article(article1)

print("\n")
for a in ArticleRepository.read_articles():
    print(a)

ArticleRepository.update_article(3, article4)

print("\n")
for a in ArticleRepository.read_articles():
    print(a)

# for a in ArticleRepository.read_articles():
#    ArticleRepository.delete_article(a)
