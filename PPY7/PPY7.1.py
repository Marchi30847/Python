import tkinter as tk
from tkinter import messagebox
from datetime import date, timedelta


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
        return f"{self.name} - ${self.price:.2f} ({self.category})"

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


class ShoppingApp:
    def __init__(self, master):
        ShoppingApp.initialize_database()
        self.products = ArticleRepository.read_articles()
        self.balance = 75.0
        self.cart = []

        self.master = master
        master.title("Food Shop")
        master.configure(bg="#e8f5e9")
        master.state('zoomed')

        self.setup_ui()

    def setup_ui(self):
        self.balance_var = tk.StringVar()
        self.update_balance_label()

        title = tk.Label(self.master, text="Welcome to the Food Shop", font=("Segoe UI", 24, "bold"),
                         bg="#e8f5e9", fg="#2e7d32")
        title.pack(pady=10)

        tk.Label(self.master, textvariable=self.balance_var, font=("Segoe UI", 16),
                 bg="#e8f5e9", fg="#2e7d32").pack(pady=5)

        frame = tk.Frame(self.master, bg="#e8f5e9")
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        prod_frame = tk.Frame(frame, bg="#c8e6c9", bd=2, relief=tk.RIDGE)
        prod_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        tk.Label(prod_frame, text="Available Products:", font=("Segoe UI", 14, "bold"),
                 bg="#c8e6c9", fg="#1b5e20").pack()

        prod_list_frame = tk.Frame(prod_frame)
        prod_list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.lst_products = tk.Listbox(prod_list_frame, font=("Segoe UI", 14, "bold"),
                                       bg="white", fg="black", height=20, width=40,
                                       selectbackground="#c5e1a5", selectforeground="black")
        self.lst_products.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        prod_scroll = tk.Scrollbar(prod_list_frame, orient=tk.VERTICAL, command=self.lst_products.yview)
        prod_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lst_products.config(yscrollcommand=prod_scroll.set)

        for p in self.products:
            self.lst_products.insert(tk.END, str(p))

        btn_frame = tk.Frame(frame, bg="#e8f5e9")
        btn_frame.pack(side=tk.LEFT, padx=20)
        tk.Button(btn_frame, text="Add ->", font=("Segoe UI", 12), width=12,
                  bg="#aed581", fg="black", activebackground="#9ccc65",
                  command=self.add_to_cart).pack(pady=10)
        tk.Button(btn_frame, text="<- Remove", font=("Segoe UI", 12), width=12,
                  bg="#ff8a65", fg="black", activebackground="#ff7043",
                  command=self.remove_from_cart).pack(pady=10)

        cart_frame = tk.Frame(frame, bg="#c8e6c9", bd=2, relief=tk.RIDGE)
        cart_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        tk.Label(cart_frame, text="Your Cart:", font=("Segoe UI", 14, "bold"),
                 bg="#c8e6c9", fg="#1b5e20").pack()

        cart_list_frame = tk.Frame(cart_frame)
        cart_list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.lst_cart = tk.Listbox(cart_list_frame, font=("Segoe UI", 14, "bold"),
                                   bg="white", fg="black", height=20, width=40,
                                   selectbackground="#ffe082", selectforeground="black")
        self.lst_cart.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        cart_scroll = tk.Scrollbar(cart_list_frame, orient=tk.VERTICAL, command=self.lst_cart.yview)
        cart_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lst_cart.config(yscrollcommand=cart_scroll.set)

        tk.Button(self.master, text="Checkout", font=("Segoe UI", 14, "bold"),
                  bg="#81c784", fg="black", activebackground="#66bb6a",
                  command=self.checkout).pack(pady=20)

    @staticmethod
    def initialize_database():
        example = [
            Article(Article.generate_id(), "Milk", 2.5, "DairyCo", "Dairy", str(date.today() + timedelta(days=10))),
            Article(Article.generate_id(), "Apple", 0.8, "FruitFarm", "Fruits", str(date.today() + timedelta(days=5))),
            Article(Article.generate_id(), "Bread", 1.5, "Bakers Ltd.", "Bakery", str(date.today() + timedelta(days=3))),
            Article(Article.generate_id(), "Cheese", 4.0, "CheeseWorks", "Dairy", str(date.today() + timedelta(days=15))),
            Article(Article.generate_id(), "Banana", 1.0, "TropiFruits", "Fruits", str(date.today() + timedelta(days=6))),
            Article(Article.generate_id(), "Orange", 1.2, "CitrusFarm", "Fruits", str(date.today() + timedelta(days=7))),
            Article(Article.generate_id(), "Yogurt", 1.8, "DairyLife", "Dairy", str(date.today() + timedelta(days=8))),
            Article(Article.generate_id(), "Tomato", 0.9, "Greenhouse", "Vegetables", str(date.today() + timedelta(days=4))),
            Article(Article.generate_id(), "Cucumber", 0.7, "Greenhouse", "Vegetables", str(date.today() + timedelta(days=4))),
            Article(Article.generate_id(), "Chips", 2.0, "Snacky", "Snacks", str(date.today() + timedelta(days=60))),
            Article(Article.generate_id(), "Juice", 3.5, "FreshPress", "Drinks", str(date.today() + timedelta(days=30))),
            Article(Article.generate_id(), "Water", 0.5, "AquaPure", "Drinks", str(date.today() + timedelta(days=100)))
        ]

        with open(ArticleRepository.FILE, "w") as f:
            pass

        for art in example:
            ArticleRepository.persist_article(art)

    def update_balance_label(self):
        self.balance_var.set(f"Balance: ${self.balance:.2f}")

    def add_to_cart(self):
        sel = self.lst_products.curselection()
        if not sel:
            return
        prod = self.products[sel[0]]
        self.cart.append(prod)
        self.lst_cart.insert(tk.END, str(prod))

    def remove_from_cart(self):
        sel = self.lst_cart.curselection()
        if not sel:
            return
        self.cart.pop(sel[0])
        self.lst_cart.delete(sel[0])

    def checkout(self):
        total = sum(p.price for p in self.cart)
        if total > self.balance:
            messagebox.showwarning("Insufficient Funds", "Not enough balance.")
            return
        self.balance -= total
        self.update_balance_label()
        messagebox.showinfo("Success", f"Purchased for ${total:.2f}")
        self.cart.clear()
        self.lst_cart.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()
