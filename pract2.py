import math

def speed_calculator():
    distance = float(input("How far did you travel in km: "))
    duration = float(input("How long did it take in hours: "))
    speed = round((distance / duration), 2)
    print(f"You traveled at {speed} km/h")


def circumference_of_circle():
    radius = float(input("Input the radius of your circle: "))
    circumference = 2 * math.pi * radius
    print(f"The circumference of a circle with radius {radius} is {circumference}")


def area_of_circle():
    radius = float(input("Input the radius of your circle: "))
    area = math.pi * radius ** 2
    print(f"The area of a circle with radius {radius} is {area}")


def cost_of_pizza():
    diameter = float(input("Input the diameter of your pizza: "))
    area = math.pi * ((diameter / 2) ** 2)
    cost = round(((area * 3.5) / 100), 2)
    print(f"The cost of a pizza with diameter of {diameter}cm is £{cost}")


def slope_of_line():
    point1 = input("Enter the x and y of the first point in format x,y: ")
    point2 = input("Enter the x and y of the second point in format x,y: ")
    p1 = point1.split(",")
    p2 = point2.split(",")

    slope = (float(p1[1]) - float(p2[1])) / (float(p1[0]) - float(p2[0]))
    print(f"The slope of your line is {slope}")


def distance_between_points():
    point1 = input("Enter the x and y of the first point in format x,y: ")
    point2 = input("Enter the x and y of the second point in format x,y: ")
    p1 = point1.split(",")
    p2 = point2.split(",")
    
    distance = math.sqrt(pow((float(p1[0]) - float(p2[0])), 2) + 
                         pow((float(p1[1]) - float(p2[1])), 2))
    print(f"The distance between the points is {distance}")


def travel_statistics():
    avg_speed = float(input("Enter your average speed in km/h: "))
    duration = float(input("Enter journey time in hours: "))
    distance = round((avg_speed * duration), 2)
    fuel_use = round((distance / 5), 2)

    print(f"You traveled {distance}km.")
    print(f"You used {fuel_use} litres of fuel.")


def sum_of_squares():
    num_last = int(input("Enter an integer for the sum of squares to stop at: ")) + 1
    total = 0
    for i in range(num_last):
        square = i**2
        total += square
    print(total)


def average_of_numbers():
    total_numbers = int(input("Total number of values to input: "))
    num = []
    for i in range(total_numbers):
        num.append(float(input("Enter a number: ")))
    
    total = 0
    for i in range(total_numbers):
        total += num[i]

    avg = total / total_numbers
    print(avg)


def fibonacci():
    position = int(input("Enter a position in the fibonacci sequence: "))

    pos1 = 0
    pos2 = 1
    pos3 = 0
    for i in range(1, position):
        pos3 = pos1 + pos2
        pos1 = pos2
        pos2 = pos3
    if position == 1:
        print(f"The number in position {position} is {pos2}")
    else:  
        print(f"The number in position {position} is {pos3}")


def select_coins():
    pennies = int(input("Enter how many pennies you have: "))

    two_pound = pennies // 200
    leftover = pennies % 200

    one_pound = leftover // 100
    leftover = leftover % 100

    fifty_p = leftover // 50
    leftover = leftover % 50

    twenty_p = leftover // 20
    leftover = leftover % 20

    ten_p = leftover // 10
    leftover = leftover % 10

    five_p = leftover // 5
    leftover = leftover % 5

    two_p = leftover // 2
    leftover = leftover % 2

    one_p = leftover // 1
    print(f"In coins this is: {two_pound} x £2, {one_pound} × £1, {fifty_p} × 50p, 
          {twenty_p} × 20p, {ten_p} × 10p, {five_p} × 5p, {two_p} × 2p, {one_p} × 1p")


def select_coins_2():
    pennies = int(input("Enter how many pennies you have: "))
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    
    total_coins = []
    for i in range(len(coins)):
        total_coins.append(pennies // coins[i])
        pennies = pennies % coins[i]

    print(f"In coins this is: {total_coins[0]} x £2, {total_coins[1]} × £1, 
          {total_coins[2]} × 50p, {total_coins[3]} × 20p, {total_coins[4]} × 10p, 
          {total_coins[5]} × 5p, {total_coins[6]} × 2p, {total_coins[7]} × 1p")


def hypotenuse():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))

    c = math.sqrt((a ** 2) + (b ** 2))
    print(f"The length of your hypotenuse is {c}")
