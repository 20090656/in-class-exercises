# 1 - greeting

def greet(name):
    print("Hello " + name + ", I hope you are well!")

names = ["Callum", "Natalie", "Harvey"]

for each_name in names:
    greet(each_name)

# 2 - Add two numbers

def add_numbers(first, second):
    return first + second

x = int(input("x = "))
y = int(input("y = "))

print(add_numbers(x, y))

# 3 - Check Even or Odd

def num_check(num):
    if num % 2 != 0:
        print("Odd")
    else:
        print("Even")

num = int(input("Check if a number is odd or even:\n>"))
num_check(num)
        
# 4 - Find the largest of Three - still can't work this out.
# a = 3
# b = 4
# c = 5


# if a > b:
#     if a > c:
#         print("a")
# elif b > a:
#     if b > c:
#         print("b")
# else:
#     print("c")

# 5 - Convert Celcius to Fahrenheit

def convert_temp(celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit

for temperature in range(20, 41):
    print(convert_temp(temperature))

# 6 - count vowels in a word

def count_vowels(word):
    count = 0
    for each_letter in word:
        if each_letter in "aeiouAEIOU":
            count += 1
    return count

user_word = ""
run_program = True

while run_program == True:
    user_word = input("please enter word or 'q' to quit:\n")
    if user_word == "q":
        run_program = False
    else:
        print(user_word + " has " + str(count_vowels(user_word)) + " vowels.")

# 7 - Multiplication table

def generate_table(x):
    for i in range(1, 13):
        sum = x * i
        print(str(i) + " x " + str(x) + " = " + str(sum))

user_num = int(input("Please give a number to generate multiplication-table:\n>"))

generate_table(user_num)

# 8 - FizzBuzz function

def fizzbuzz(n):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)

user_num = int(input("Check for fizz-buzz:\n>"))
fizzbuzz(user_num)

# 9 - Prime checker - Still can't figure out how to check for primes

def check_prime(n):
    if # check for prime
        return True
    else:
        return False

user_num = int(input("Check if Prime:\n>"))
check_prime(user_num)

# 10 - Factorial Calculator - Still can't figure out how to check

# 11 - Fibonacci sequence - Needed to look up help for calculating sequence
    
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        next_num = a + b
        a = b
        b = next_num
    return a

check_num = int(input("Check n-th fibonacci number:\n>>>"))
print(fibonacci(check_num))
