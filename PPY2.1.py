def task1():
    name = input("What is your name?")
    date = input("What is your birth date?")
    email = input("What is your email address?")
    phone = input("What is your phone number?")

    list = [name, date, email, phone]
    print(list)
    tuple = (name, date, email, phone)
    print(tuple)
    dict = {"Name": name, "Date": date, "Email": email, "Phone": phone}
    print(dict)


def task2():
    list = []
    for i in range(20):
        list.append(i + 5)
        if is_prime(i):
            print("index:", i, "element:", list[i])


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def task3():
    user_letters = input("Enter uppercase letters: ")
    list_letters = user_letters.split(" ")

    user_digits = input("Enter digits: ")
    list_digits = user_digits.split(" ")
    #  list_digits = list(user_digits.split(" "))

    correct_input = True
    for letter in list_letters:
        if letter.islower():
            correct_input = False
            break

    for digit in list_digits:
        if not digit.isdigit():
            correct_input = False
            break

    if len(list_letters) != len(list_digits):
        correct_input = False

    if correct_input:
        dict = {}
        for i in range(len(list_letters)):
            dict[list_letters[i]] = int(list_digits[i])
        print(dict)
    else:
        print("Please enter a valid input.")

words = ['banana', 'apple', 'cherry']
morefive = list(filter(lambda word: len(word) > 5, words))
sorted_words = sorted(words, key=lambda word: len(word))
sorted_words.sort(key=lambda word: len(word))
print(sorted_words)  # ['apple', 'banana', 'cherry']

for word in words[:]:
    if len(word) > 5:
        words.remove(word)
print(words)

prev, cur = 0, 1
prev, cur = cur, prev + 1

arr = [x for x in range(1, 5)]
print(arr)

def task4(nums, words):
    ar = []
    for num, word in zip(nums, words):
        ar.append(tuple([num, word]))

    rt = tuple(ar)
    return rt

print(task4([1, 2, 3], ["a", "b", "c"]))
