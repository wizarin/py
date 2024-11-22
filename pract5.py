import math
from graphix import Window, Circle, Point, Text, Line


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
    for line in range(height):
        print("*" * width)


def draw_letter_e():
    line_height = 2
    draw_block_of_stars(8, line_height)
    draw_block_of_stars(2, line_height)
    draw_block_of_stars(5, line_height)
    draw_block_of_stars(2, line_height)
    draw_block_of_stars(8, line_height)


def draw_brown_eye(win, centre, radius):
    colour = ["white", "brown", "black"]
    for i in range(3):
        draw_circle(win, centre, radius, colour[i])
        radius = round(radius / 2)


def draw_pair_of_brown_eyes():
    win = Window("", 800, 800)
    radius = 120
    eye1_centre = Point(120,200)
    eye2_centre = Point(eye1_centre.x + (radius * 2), 200)
    draw_brown_eye(win, eye1_centre, radius)
    draw_brown_eye(win, eye2_centre, radius)
    
    win.get_mouse()
    win.close()


def distance_between_points(p1, p2):
    return math.sqrt(pow((p1.x - p2.x), 2) + pow((p1.y - p2.y), 2))


def distance_calculator():
    win = Window()
    message = Text(Point(200, 60), "Click first point")
    message.draw(win)
    p1 = win.get_mouse()
    message.text = "Click second point"
    p2 = win.get_mouse()
    distance = str(distance_between_points(p1, p2))
    message.text = "The distance between the points is " + distance
    
    win.get_mouse()
    win.close()
    

def draw_blocks(space1, block1, space2, block2, height):
    for line in range(height):
        print((" " * space1) + ("*" * block1) + (" " * space2) + ("*" * block2))


def draw_letter_a():
    draw_blocks(1,8,0,0,2)
    draw_blocks(0,2,6,2,2)
    draw_blocks(0,10,0,0,2)
    draw_blocks(0,2,6,2,3)
    

def draw_four_pairs_of_brown_eyes():
    win = Window()
    message = Text(Point(200, 60), "Click for eye location and size")
    message.draw(win)
    for i in range(4):
        l_centre = win.get_mouse()
        size = win.get_mouse()
        radius = round(distance_between_points(l_centre, size))
        r_centre = Point(l_centre.x + (radius * 2), l_centre.y)
        #Draw eyes
        draw_brown_eye(win, l_centre, radius)
        draw_brown_eye(win, r_centre, radius)
        
    win.get_mouse()
    win.close()


def display_text_with_spaces(win, text, position, size):
    #First add spaces to string input and convert to uppercase
    spaced_text = ""
    for char in text:
        spaced_text += (char + " ")
    spaced_text = spaced_text.upper()
    #Draw message in the given window using given position and size 
    display = Text(position, text)
    display.size = size
    display.draw(win)


def construct_vision_chart():
    win = Window()
    total_lines = 6
    start_point = Point(200, 80)
    start_size = 34
    text_inputs = []
    for i in range(total_lines):
        text_inputs.append(input("Enter a string for line " + str(i + 1) + ": "))
        display_point = Point(start_point.x, start_point.y + (i * 50))
        display_size = round(start_size / (i + 1))
        display_text_with_spaces(win, text_inputs[i], display_point, display_size)


def draw_stick_figure(win, position, size):
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    hand = Line(Point(200, 160), Point (260, 240))
    hand.draw(win)
    hand2 = Line(Point(200, 160), Point (140, 240))
    hand2.draw(win)
    leg = hand = Line(Point(200, 240), Point (260, 300))
    leg.draw(win)
    leg2 = hand = Line(Point(200, 240), Point (140, 300))
    leg2.draw(win)
    
    
def draw_stick_figure_family():
    
    
