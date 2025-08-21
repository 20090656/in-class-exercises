# 01. Variables and expressions. 

# 1
user_name = input("Hi! What is your name? ")
print("It's great to meet you " + user_name + ", How are you today?")

# 2
first_number = int(input("Please give me a number you'd like to add to something: "))
second_number = int(input("Great! Now what is the other number you'd like to add? "))
print(first_number + second_number)
print("Wow thats a cool new number!")

# 3
print("How about we practice some subtraction!")
first_number = int(input("What is the number you'd like to subtrack from? "))
second_number = int(input("Great! And now how much would you like to subtract? "))
answer = first_number - second_number
print(str(answer) + ". Thats a cool number!")

# 4
print("It's mighty morphin' multiplication time!")
first_number = int(input("Pick a number: "))
second_number = int(input("Now multiply that by this number: "))
answer = first_number * second_number
print(str(answer) + ". Kowabunga dude!")

# 5
print("Division!")
first_number = int(input("Pick a number: "))
second_number = int(input("And what would you like to divide by? "))
answer = first_number / second_number
print(str(answer) + ". Here's your number!")

# 6
print("Let's calculate the area of a rectangle.")
print("Remember: Make sure you're working in the same units! eg. Don't mix metres and centimetres!")
rect_length = int(input("What is the length of the rectangle? "))
rect_width = int(input("What is the width of the rectangle? "))
rect_area = rect_length * rect_width
print("The area is: " + str(rect_area))

# 7
import time
print("Celsius to Fahrenheit converter")
celsius = int(input("What temperature would you like to convert into freedom units? "))
fahrenheit_output = (celsius * 9 / 5) + 32
print("...running program... ")
time.sleep(1)
print("...converting to freedom units...")
time.sleep(1.5)
print("...removing actual freedoms...")
time.sleep(2)
print(str(fahrenheit_output) + " Fahrenheit")

# 8
print("KM to M converter program")
user_km = float(input("Please enter distance in km to convert: "))
out_miles = user_km * 0.621371
out_miles = str(out_miles)
print(out_miles + " Miles")

# 9
print("Simple Intrest Calculator")
principal = float(input("How much money are you starting with? "))
rate = float(input("What is the intrest rate? Please write as a percentage number: "))
time = float(input("How long in years? "))
#calulate intrest amount and total
intrest = (principal * rate * time) / 100
total_money = principal + intrest
#output intrest amount, and total money afterwards
print("That is $" + str(intrest) + " in intrest.")
print("And $" + str(total_money) + " that will be in the account after the given time.")

# 10
print("How about we square a number?")
user_number = int(input("What number would you like to square? "))
squared_number = user_number ** 2
squared_number = str(squared_number)
print(str(user_number) + " squared is " + squared_number)

# 11
print("Lets find the cube of a number")
user_number = int(input("What number would you like to cube? "))
cubed_number = user_number ** 3
cubed_number = str(cubed_number)
print(str(user_number) + " cubed is " + cubed_number)

# 12
print("Please give me 3 numbers to average for you")
first_num = int(input("What is the first number? "))
second_num = int(input("What is the second number? "))
third_num = int(input("What is the third number? "))
average = (first_num + second_num + third_num) / 3
print("The average of those numbers is " + str(average))

# 13 - Swap two variables
first_num = int(input("A number please: "))
second_num = int(input("Another number: "))
swap_num = first_num
first_num = second_num
second_num = swap_num
print("Aha! I have swapped them!")
print(first_num)
print(second_num)

# 14
first_num = int(input("Please input a number: "))
second_num = int(input("Now give another number, to check if they are equal: "))
if first_num == second_num:
    print("They are equal")
else:
    print("They are not equal")

# 15
first_num = int(input("Please input a number: "))
second_num = int(input("Now give another number, I will check which is greatest: "))
if first_num == second_num:
    print("those are actually equal! you didn't follow the instructions.")
elif first_num > second_num:
    print("The first number was greater.")
else:
    print("the second number was greater.")

# 16
print("I will check if a number is positive")
user_number = int(input("What is the number you'd like to check? "))
if user_number == 0:
    print("zero is actually neutral, nice try")
elif user_number > 0:
    print("That's a positive number")
else:
    print("That is a negative number.")

17 + 18 have been done all together in 16. I didnt realise until I go to the next question

# 19
print("Let's play a game called IS IT BIGGER THAN 100")
user_num = int(input("Please give me a number to check: "))
if user_num == 100:
    print("That exactly 100, so it's technically not bigger. The answer is no")
elif user_num > 100:
    print("Yep, thats bigger")
else:
    print("Sorry, that's not bigger")

# 20
print("Do you want to check if a number is equally divisible by another number? Well you've come to the right program.")
start_num = int(input("Please give a number to divide: "))
div_num = int(input("Now please provide a number to divide by: "))
remainder = start_num % div_num
# print(remainder)
if remainder == 0:
    print("Yes, " + str(start_num) + " is equally divisible by " + str(div_num))
else:
    print("No that is not equally divisable")