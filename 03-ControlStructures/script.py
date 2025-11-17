###
# # Credit card payment 
# #
# account_balance = 500
# total_payment = int(input("Provide payment in $: "))

# if total_payment <= account_balance:
#     print('Payment completed')
# else:
#     print('No funds')

###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
# #
# total_tasks = 20
# tasks_ok = int(input("Provide the amount of tasks done:"));
# test_passed = False

# if tasks_ok >= (total_tasks / 2):
#     test_passed = True

# if test_passed:
#     print('Congratulations! You passed the test.')
# else:
#     print('Unfortunately, you failed the test.')


###
# Checking whether the number
# entered from the keyboard is even or odd 
# #
# number = int(input('Enter number: '))

# if number % 2  == 0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')


###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
# basic_salary = 5000
# total_salary = 0
# bonus = 0.15 # 15%
# is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'


# if is_bonus:
#     total_salary = basic_salary +  basic_salary * bonus;


# print('Basic salary: %d' % (basic_salary))
# print('Bonus included? %s' % (is_bonus))
# print('Total salary: %f' % (total_salary))


###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
# #
# size = input('Enter size symbol: ')

# if size == 'S':
#     print('S: Small size')
# elif size == 'M':
#     print('M: medium size')

# elif size == 'XL':
#     print("XL: extra large")
# else:
#     print("Incorect value")


###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
# driving_mode = input('Enter driving mode (A/M/E):')
# distance = int(input('Enter distance in km'))

# fuel_consumption = 6;
# if driving_mode == 'A':
#     fuel_consumption = 7;
    
# elif driving_mode == 'M':
#     fuel_consumption = 9;


# total_consumption = fuel_consumption  * distance / 100;
# print('Total fuel consumption over a distance of %d km in driving mode %s is %s liters' % (distance, driving_mode, total_consumption))


###
# Checks whether at least one number entered
# from the keyboard is not negative
# # 
# x = int(input('Enter first number: '))
# y = int(input('Enter 2nd number: '))

# if (x < 0 and y > 0) or (x > 0 and y < 0):
#     print(f'At least one of the numbers {x} and {y} is not negative')

###
# Calculates the number of days in a month
# #
# month = int(input('Enter month number (1..12)'))

# if month in [1,3,5,7,8,10,12] :
#     days = 31 ## months with 31 days
# elif month in [4,6,9,11] :
#     days = 30 ## months with 30 days
# elif month == 2:
#     days = 28;
# else:
#     print("%i is not  a number of month")
# ## February 28 days 

# print(f"Month {month} has {days} days");

##
# Checks if the given day number of the month is correct

# month = int(input('Enter month number (1..12): '))
# day = int(input('Enter the day number of the month: '))
# day_ok = False



# if (day < 1):
#     day_ok = False;

# if month in [1,3,5,7,8,10,12]: 
#     if day <= 31:
#         day_ok = True;

# if month in [4,6,9,11]: 
#     if day <= 30:
#         day_ok = True;

# if month == 2:
#     if day <= 28:
#         day_ok = True;



# message = f'Day {day} for the month {month}';
# if day_ok:
#      print(f'{message} is correct');
# else:
#      print(f"{message} is not correct");



###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
# university = 'Krakow University of Economics'
# university_expanded = ''

# for char in university:
#     university_expanded = university_expanded +  " " + char + " ";

# print(university) # original university name
# print(university_expanded);


###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#


# plain_text = 'The early bird catches the worm';


# encrypted_text = ''

# for char in plain_text:
#     # read the character's code (use ord())

#     # print(ord(char));

#     order = ord(char);

#     # add one to the character's code
#     order+=1;
#     # replace new character code with its
#     # print(chr(ord(char)+1))

#     # corresponding character (use chr())
#     # add encrypted character to encrypted text
#     encrypted_text+=chr(order);

# print(plain_text)
# print(encrypted_text)



# 4.6
###
# Calculates the sum of even numbers from 1 to a given number N
#
# N = 10
# sum_even = 0

# Calculate the sum of even numbers
# for i in range(1, N + 1):
#     if i % 2 == 0:
#         sum_even += i

# currentNum = 1;
# while currentNum <= N:
#     if(currentNum % 2 == 0): sum_even+=currentNum;

#     currentNum+=1;





# print(f"The sum of even numbers from 1 to {N} is: {sum_even}")

# 6.3

###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
# light_switch1 = True # False - switch off, True - switch on
# light_switch2 = True
# bulbs_on = 0
# if light_switch1:
#     bulbs_on += 1
# if light_switch2:
#     bulbs_on += 2;
# print(bulbs_on)

###
# Password validator
# New password is at least 12 characters long
# #
# new_password = input('Enter new password: ')
# if len(new_password) < 12:
#    print('Password too short (min. 12 chars)') 

###
# Program that simulates the operation of an electronic thermometer.
# 33, 30, 8, 0, -2

# statements = ["extreamly hot", "hot", "warm", "a warning. Frost!" ]


# text = "It is ";
# temperature = 32
# if temperature > 35:
    
# elif temperature > 30:
#     print ...
# elif 