from graphix import Window, Circle, Point
from pract6 import calculate_grade
from pract5 import distance_between_points, draw_brown_eye
import time

def hello_while():
    i = 0
    while i < 10:
        print("i is now", i)
        i = i + 1


def countdown():
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")


def mystery_loop():
    i = 1
    # Be careful! This loop will run forever!
    while i < 1000:
        print(i)
        i = i * 2


def add_up_numbers1():
    total = 0
    more_numbers = "y"
    while more_numbers == "y":
        number = int(input("Enter a number: "))
        total = total + number
        more_numbers = input("Any more numbers? (y/n) ")
    print("The total is", total)


def add_up_numbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)


def add_up_numbers3():
    total = 0
    n_str = input("Number (hit enter to stop): ")
    while n_str != "":
        number = int(n_str)
        total += number
        n_str = input("Number (hit enter to stop): ")
    print("The total is", total)


def add_up_numbers4():
    total = 0
    while True:
        n_str = input("Number (anything else to stop): ")
        if not n_str.isdigit():
            break  # Exit the loop if the input is not a number
        number = int(n_str)
        total += number
    print("The total is", total)


# Note: msg == "" needs to appear twice
def get_string1():
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg


def get_string2():
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg


def can_apply_for_job(degree, experience):
    if (degree == "1st" or degree == "2:1") and experience >= 1:
        return True
    elif degree == "2:2" and experience >= 2:
        return True
    else:
        return False


def can_vote1():
    age = int(input("How old are you? "))
    while age <= 18:
        print("Wait until you are 18!")
        age = int(input("How old are you? "))


def can_vote2():
    while True:
        age = int(input("How old are you? "))
        if age > 18:
            break
        print("Wait until you are 18!")


#  For question 2
def traffic_lights():
    win = Window()
    red = Circle(Point(100, 50), 20)
    red.fill_colour = "red"
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.fill_colour = "black"
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.fill_colour = "black"
    green.draw(win)
    while True:
        pass
        # remove the `pass` and add your code here


# For question 6
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


# Solutions to the programming exercises:

# Exercise 1
def get_name():
    name = input("Enter your name: ")
    while name.isalpha() == False:
        print("Name can only be letters.")
        name = input("Enter your name: ")
    return(name)


# Exercise 2
def traffic_lights():
    win = Window()
    red = Circle(Point(100, 50), 20)
    red.fill_colour = "red"
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.fill_colour = "black"
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.fill_colour = "black"
    green.draw(win)
    while True:
        amber.fill_colour = "orange"
        time.sleep(1)
        red.fill_colour = "black"
        amber.fill_colour = "black"
        green.fill_colour = "green"
        time.sleep(1)
        green.fill_colour = "black"
        amber.fill_colour = "orange"
        time.sleep(1)
        amber.fill_colour = "black"
        red.fill_colour = "red"
        time.sleep(1)


# Exercise 3
def grade_coursework():
    while True:
        mark = input("Enter a mark: ")
        if (mark.isdigit() == False) or mark > 20 or mark < 0:
            print("Mark has to be between 0 and 20.")
        elif mark <= 20 and mark >= 0:
            break
       
    calculate_grade(mark)


# Exercise 4
def order_price():
	price =
	quantity =
	while cont != "y":
		while True:
			price = input("Enter product price: ")
			if price.isdigit() == True and price > 0:
				break
			print("Price has to be positive number.")
		while True:
			quantity = input("Enter product quantity: ")
			if quantity.isdigit() = True and quantity > 0:
				break
			print("Quantity has to be positive number.")
		while True:
			cont = input("Continue? Enter 'y or 'n': ")
			if cont == "y" or cont == "n":
				break
			print("Invalid input. Enter 'y' or 'n'.")
		
		
# Exercise 5
def clickable_eye():
	win = Window("")
	centre = Point(win.height/2, win.width/2)
	radius = 100
	draw_brown_eye(win, centre, radius)
	labels = ["pupil"]