"""
def add(a, b):
    return a + b

def func1(a):
    print(a)
    def func2():
        print(a*2)
    func2()

func1(1)

def count(el1, el2):
    print(el1 * el2)

x=count
x(5, 10)

a = 5
if a < 5:
    def foo():
        print("A is less than 5")
else:
    def foo():
        print("A is greater than or equals 5")

foo()

def show(a, b, c):
    print(a, b, c)

show(1, 2, 3)

show(a = 1, b = 2, c = 3)

def show2(a, b = 4, c = 8):
    print(a, b, c)

show2(a = 1)

# tuple
def write(*arg):
    print(arg)

write(1, 2, 3)

# dictionary
def write2(**args):
    print(args)

write2(a = 1, b = 2, c = 3)

l = lambda a, b, c: print(a, b, c)
l(1, 2, 3)

list1 = [(lambda a:a*2), (lambda a:a*4), (lambda a:a*6)]
for i in list1:
    print(i(4))
print(list1[0])
print(list1[0](10))

def myFunction():
    yield "hello"
    yield "world"
    yield 5

print(myFunction())
print(list(myFunction()))
for i in myFunction():
    print(i)

print(next(myFunction()))
x = myFunction()
print(next(x))
print(next(x))
print(next(x))

# to reset
x = myFunction()
print(next(x))
print(next(x))
print(next(x))
"""
import math


# Task1
def perfect_numbers(*arg):
    def divisors_sum(number):
        divisors = []
        for div in range(1, number):
            if number % div == 0:
                divisors.append(div)

        return sum(divisors)

    p_numbers = {}
    for num in arg:
        p_numbers[num] = num == divisors_sum(num)
    return p_numbers


print(perfect_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Task2
def first_prime_numbers(first_primes=100):
    def prime_numbers_in_range(lim=200):
        prime_candidates = list(range(2, lim + 1))

        for div in range(2, int(math.sqrt(lim)) + 1):
            for num in prime_candidates:
                if num == div: continue
                if num % div == 0:
                    prime_candidates.remove(num)

        if len(prime_candidates) < first_primes:
            return prime_numbers_in_range(lim * 2)
        else:
            return prime_candidates[:first_primes]

    return prime_numbers_in_range()

print(first_prime_numbers(100))


# Task3
def filter_collection(collection, ascending=True):
    divisible = lambda num: num % 2 == 0 and num % 3 != 0

    collection = list(filter(divisible, collection))

    if ascending:
        collection = sorted(collection)
    else:
        collection = sorted(collection, reverse=True)

    return collection


print(filter_collection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False))
