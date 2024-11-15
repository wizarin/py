import math
from graphix import Window, Circle


def greet(name):
    return f"Hello, {name}!"


def product(a, b):
    return a * b


def divide(a, b):
    return a / b


def divide_and_product(a, b):
    product_result = product(a, b)
    divide_result = divide(a, b)
    return product_result, divide_result


def main():
    my_name = input("What is your name? ")
    greeting = greet(my_name)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    product_result, divide_result = divide_and_product(num1, num2)
    print(f"{num1} * {num2} = {product_result}")
    print(f"{num1} / {num2} = {divide_result}")


def calc_future_value(amount, years):
    interest_rate = 0.065
    for year in range(years):
        amount = amount * (1 + interest_rate)
    return amount


def future_value():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calc_future_value(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)


# For exercises 1 and 2
def area_of_circle(radius):
    return math.pi * radius ** 2


# For exercise 3
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)


def draw_brown_eye_in_centre():
    window = Window()
    # Add your code here


# For exercise 5
def draw_brown_eye(win, centre, radius):
    pass
    # Remove pass and add your code here


def circ_of_circle(radius):
	return math.pi * (radius * 2)

 
def circle_info():
	radius = int(input("Enter a circle radius: "))
	area = area_of_circle(radius)
	circ = circ_of_circle(radius)
	print(f"A circle with radius {radius} has an area of {area} and a circumference of {circ}.")


def draw_brown_eye_in_centre():
	win = Window()
	centre = Point(200,200)
	radius = [120, 60, 30]
	colour = ["white", "brown", "black"]
	for i in range(len(radius)):
		draw_circle(win, centre, radius[i], colour[i]) 


def draw_block_of_stars(width, height):
	for line in height:
		print("*" * width)


def draw_letter_e():
	draw_block_of_stars(8, 2)
	draw_block_of_stars(2, 2)
	draw_block_of_stars(5, 2)
	draw_block_of_stars(2, 2)
	draw_block_of_stars(8, 2)


def draw_brown_eye(win, centre, radius):
        colour = ["white", "brown", "black"]
        for i in range(3):
                draw_circle(win, centre, radius, colour[i])
		radius /= 2


def draw_pair_of_brown_eyes():
	win = Window()
	centre = Point(200,200)
	radius = 120

