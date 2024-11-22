from graphix import Window, Circle, Point
import math
# Remember to update the line above if you are using other Graphix objects


def greet(name):
    print("Hello", name + ".")
    if len(name) > 20:
        print("That's a long name!")


def can_you_vote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")


def get_degree_class(mark):
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"


# We will simplify this function later in the term
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31


def overly_complex_days_in_month(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28


def count_down():
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")


def numbered_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# For exercises 8 & 11
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)


# For exercise 8
def draw_coloured_eye(win, centre, radius, colour):
    colours = ["white", colour, "black"]
    for i in range(3):
        draw_circle(win, centre, radius, colours[i])
        radius = round(radius / 2)


##############################################################################
# Exercise 1
def fast_food_order_price():
    price = float(input("Enter the order price: £"))
    if price < 20:
        price += 2.5
    print(f"Your order price with delivery is: £{price:.2f}")


# Exercise 2
def what_to_do_today():
    temp = float(input("Enter today's temperature: "))
    if temp > 25:
        print("You should swim in the sea!")
    elif temp >= 10 or temp <=25:
        print("You should go shopping in Gunwharf Quays!")
    else:
        print("You should watch a film at home!")


# Exercise 3
def display_square_roots(start, end):
    for num in range (start, end + 1):
        sqrt = math.sqrt(num)
        print(f"The square root of {num} is {sqrt:.3f}")


# Exercise 4
def calculate_grade(mark):
    if mark > 20 or mark < 0:
        return("X")
    elif mark >= 16:
        return("A")
    elif mark >= 12:
        return("B")
    elif mark >= 8:
        return("C")
    else:
        return("F")


# Exercise 5
def peas_in_a_pod():
    peas = int(input("How many peas: "))
    win = Window("", peas * 100, 100)
    centre_x = 50
    for pea in range(peas):
        centre = Point(centre_x, 50)
        draw_circle(win, centre, 50, "green")
        centre_x += 100
    
    win.get_mouse()
    win.close()


# Exercise 6
def ticket_price(distance, age):
    price = 10 + (distance * 0.15)
    if age <= 15 or age >= 60:
        price *= 0.6
    return(price)


# Exercise 7
def numbered_square(n):
    for line in range(n):
        for num in range(n):
            print(n-line+num, end="")
        print()


# Exercise 8
def eye_picker():
    win = Window("Eye Picker")
    # Create variables for loops
    colours = ["blue", "grey", "green", "brown"]
    colour = ""
    centre_x = -1
    centre_y = -1
    # Loop for centre coordinates input
    while (centre_x < 0 or centre_x > 400) or (centre_y < 0 or centre_y > 400 ):
        coords = input("Enter eye centre in format x,y: ").split(",")
        centre_x = int(coords[0])
        centre_y = int(coords[1])
        if (centre_x < 0 or centre_x > 400) or (centre_y < 0 or centre_y > 400 ):
            print("Eye centre not in 400x400 window")
    centre = Point(centre_x, centre_y)
    # Loop for colour input
    while colour not in colours:
        colour = input("Enter an eye colour: ")
        if colour not in colours:
            print("Eye colour not valid")
    draw_coloured_eye(win, centre, 50, colour)
   
    win.get_mouse()
    win.close()


# Exercise 9
def draw_patch_window():
    win = Window("", 200, 200)