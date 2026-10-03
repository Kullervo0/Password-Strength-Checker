import random
import string

print("This program will generate you a secure password!")

password = ""
length = int(input("how long do you want the password to be"))

letters = string.ascii_letters
numbers_special = string.digits + string.punctuation

for x in range(0, length, 5):
    group = []

    for y in range(4):
        group.append(random.choice(letters))

    group.append(random.choice(numbers_special))

    random.shuffle(group)

    password += "".join(group)

print(password)
