import string
import random
file = open('scaler.txt', 'a')
for i in range(10000):
    num = random.randint(3, 10)
    char = random.choice(string.ascii_lowercase)
    for n in range(num): 
        print(char, end="")
        file.write(char)
file.close()



