# 02 Loops and Conditionals 
# Practice sheets

# # 1 - Check if a number is odd or even
user_number = int(input("Please give a number: "))
check_number = user_number % 2
if check_number == 0:
    print("That is an even number.")
else:
    print("That is an odd number")

# 2 Check largest of Three numbers - Overthinking this 

print("Please enter numbers, and i'll work out which is the biggest.")
x = int(input("First number : "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x > y:
    if x > z:
        print(str(x) + " is the biggest")
    else:
        print(str(z) + " is the biggest")
elif y > x:
    if y > z:
        print(str(y) + " it the biggest")


# 3 - Grade Calculator

# Funtction to grade score 
def grade(user_score):
    if user_score > 100:
        return "Sorry that is not a valid score, it must be from 0-100"
    elif user_score >= 90:
        return "A" 
    elif user_score >= 80:
        return "B" 
    elif user_score >= 70: 
        return "C"
    elif user_score >= 60:
        return "D"
    else:
        return "F"

user_score = int(input("Add score to calculate grade: "))

print(grade(user_score))


# 4 - Password Checker

password = "123password"

print("Please enter password. You only have 3 attempts.")

for i in range(3):
    user_input = input(">>>")
    if user_input == "123password":
            print("Password Accepted.")
    else:
            print("Please try again.")

# 5 - Count from 1 to 10

for number in range(1,11):
    print(number)

# 6 - Count down from 10

for number in range(10, 0, -1):
    print(number)

# 7 - Print even numbers 1 to 20
for number in range(1, 21):
    if number % 2 == 0:
        print(number)

# 8 - Sum of first 10 Numbers

sum = 0

for number in range(1,11):
    sum = sum + number
print(sum)

# 9 - Multiplication table
user_num = int(input("Please give a number for the multiplicaiton table: "))
for i in range(1,13):
    sum = user_num * i
    print(str(i) + " x " + str(user_num) + " = " + str(sum))

# 10 - Factorial Calculator _ STILL UNSURE HOW TO DO THIS

user_num = -1
print("Please give me a number to calculate it's factorial: ")
while user_num < 0:
    user_num = int(input(">>>"))
    if user_num < 0:
        print("Cannot calculate negative factorials. Try again.")

factorial = 0

for i in range(user_num, 0, -1):
    print(i)

# 11 - print each character in a word on a new line

user_word = input("Please give me a word\n>>>")

for each_letter in user_word:
    print(each_letter)

# 12 Draw a triangle
tri_height = int(input("How tall should the triangle be?\n>"))

x = 0

for i in range(tri_height):
    x += 1
    print("*" * x)

13 - Number Guessing Game
import random
secret_num = random.randint(1,20)

# guess = 0

print("Welcome to the guessing game")
while guess != secret_num:
    guess = int(input("Whats your guess?\n>"))
    if guess < secret_num:
        print("Thats too low, try again.")
    elif guess > secret_num:
        print("Too high! try again.")
print("Congratulations! You got it!")

# 14 - Count Vowels in a Word

vowels = "aeiouAEIOU"

user_word = input("Give word, and I'll return the number of vowels:\n>")

count = 0

for each_letter in user_word:
    if each_letter in vowels:
        count += 1
print(count)

#15 - Print prime numbers from 1-50

# my thinking to solve:
# first need a loop to check if a number is prime. if it is print.
# then this is nested in a for loop which goes from the numbers 1 to 50
# for i in range(1, 50):

# 16 - FizzBuzz
for num in range (1,51):
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 17 - Sum of Digits

user_num = input("Please give a number, with more than one digit:\n>")

numbers = []

for each_number in user_num:
    num = int(each_number)
    numbers.append(num)

total = sum(numbers)
print(total)

# 18 - How many times does a letter appear

user_word = input("Please give a word:\n>")
letter = input("Please give a letter:\n>")

count = 0

for each_letter in user_word:
    if each_letter == letter:
        count += 1
print(letter + " appears " + str(count) + " times!")