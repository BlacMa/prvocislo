# Program to check if a number is prime or not

#import random
# num = 29
#num = random.randint(0, 100)
# input
num = int(input())
  
print
print
print
print
print(num)
# output



# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "je prvočíslo")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "není prvočíslo")
    else:
        print(num, "je1
         prvočíslo")
