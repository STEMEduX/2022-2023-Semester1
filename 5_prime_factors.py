# Program to check if a number is prime or not

num = 29

# To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
flag = False
a =[0]*2000
j = 0
# prime numbers are greater than 1
if num > 1:
    # check for factors

    for i in range(2, int(num/2)):
        print(i, "")
        if (num % i) == 0:
            # if factor is found, add the number to the array
            flag = True
            a[j] = num/i
            j = j + 1
        print(flag, "")
    print(flag, "")

# check if flag is True
if flag:
    print(num, "is not a prime number")
    for x in range(0, j):
      print(int(a[x]))
else:
    print(num, "is a prime number")