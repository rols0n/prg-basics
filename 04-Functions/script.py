# ###
# # Program for testing built-in functions
# #
# max_number = max(7,5,6,3,8,2)
# print('Max number of 7,5,6,3,8,2 is', max_number)

# min_number = min(4,7,2,3,9,8)
# print('Min number of 4,7,2,3,9,8 is', min_number)

# str_length = len("computer science")
# print('The number of characters in "computer science" is', str_length)


# print(input());
# print(int("20303"))
# print(bin(304))
# print(hex(304))
# print(ascii("€"))

# print(abs(-17))

# 3.1

# import math;

# square_root = math.sqrt(7)
# print('A square root of 7 is', square_root)

# nat_log = math.log(5, math.e)
# print(nat_log);
# # print(math.pow(2.71, 5))

# sin90 = math.sin(90);
# print(sin90)

# 3. 2
# import random;

# print(random.randint(1, 6));


# 4.3
# import math;

# def traingle_area(a,b,c):
#     semi_par = (a + b + c) / 2;
    
#     formula = semi_par*(semi_par - a)*(semi_par - b)*(semi_par - c);

#     # print(formula);


#     return math.sqrt(formula);







# print(traingle_area(7,24,25))

# 4.4



# def sum_digits(number):

#     sum = 0;
#     number_str = str(abs(number));

#     for digit in number_str:
#         sum += int(digit);
    
#     return sum;

# any_number = int(input('Enter integer number: '))
# result = sum_digits(any_number)
# print(f'The sum of the digits in the number {any_number} is {result}')

# 4.5


###
# Calculates the final grade for a test based
# on the number of points obtained
#
# def pts_to_grade(points):
#     grade = ''
#     if points >= 18:
#         grade = 'Excellent'
#     elif points >=14:
#         grade = "Good";
#     elif points >= 10:
#         grade = "Satisfactory";
#     else: grade = "Fail";
#     return grade

# test_result = 15
# final_grade = pts_to_grade(test_result)
# print(f'You scored {test_result} points on the test. Your final grade is {final_grade}');


# 4.6

###
# Function that returns the full name of a day of the week
# based on its number
#

# Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday
# days = ['Monday', "Tuesday",  'Wednesday',  'Thursday',  'Friday', 'Saturday', 'Sunday']
# def day_name(day_number):
    
#     if(day_number < 1 or day_number > 7): return;

#     return days[day_number-1];
    

# # Function usage
# print('The name of day 5 in the week is', day_name(5))
# print('The name of day 3 in the week is', day_name(3))
# print('The name of day 7 in the week is', day_name(7))

# 4.8

# ERROR = "Wrong data format;"
# def time_string(hours, minutes, time_format):



#     time_str = f'{hours}:{minutes}';

 
#     if(int(time_format) == 12):
#         if(int(hours) >= 12): time_str +="pm";
#         else: time_str +="am";

#     print(time_str);






# time_string(15, 38, '24') 
# time_string('08', 3, '24') 
# time_string(0, 5, '24') 
# time_string(11, 15, '12') 
# time_string(0, 7, '12') 
# time_string(7, 30, '12') 
# time_string(12, 46, '12') 
# time_string(13, 10, '12') 
# time_string(19, '02', '12') 






# 5.3

###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
# import keyboard; # your own defined module


# import keyboard;

# first_name = keyboard.input_string("Enter name: ")
# last_name = keyboard.input_string("Last name: ")
# age = keyboard.input_integer("Age: ")
# salary = keyboard.input_real("Salary in PLN: ")
# is_sallary_hidden = keyboard.input_boolean("Hide salary? (y/n)");

# # Reads employee's data from keyboard
# # first_name = keyboard.('Enter name: ')
# # last_name = ...
# # age = ...
# # salary = ...
# # is_salary_hidden = input_boolean('Hide salary? (y/n)')

# # Prints employee's record
# print('DATA RECORD')
# print('===========')
# print('Name:', first_name)
# print('Surname: ', last_name);
# print('Age: ', age)

# if is_sallary_hidden:
#     print('Salary: ', salary);

#  5.4

import draw_figures, figures;


# draw_figures.draw_square(52);

###


# 6.5
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
# import ...
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   

## Draw figures

# draw_figures.draw_rectangle(pen, 100, 150);
draw_figures.draw_square(pen, 150)
pen.forward(200);
pen.color("red")
# draw_figures.draw_square(pen, 150)
draw_figures.draw_rectangle(pen, 100, 150);
# pen.color("black")

pen.forward(100);
pen.color("white")
draw_figures.draw_triangle(pen, 120)




# Hide the turtle and finish
pen.hideturtle()
window.mainloop()