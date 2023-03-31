import string
import random
# choose a random character from lower case letters
for i in range(100):
    num = random.randint(5, 10)
    for n in range(num):
    char = random.choice(string.ascii_lowercase)
    print(char)