def say_hello():
    print("Hello World")


def say_bye():
    print("Goodbye Mars")


# A simple kilograms to ounces conversion program
# It asks for a weight in kilograms (for example 10)
# and converts it to ounces (352.74)
def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
    print("The weight in ounces is", ounces)


def count():
    for number in range(10):
        print("Number is now:", number)


# A simple euros to pounds conversion program
# It asks for a value in euros (for example 10)
# and converts it to pounds (8.7)
def euros_to_pounds():
    euros = float(input("Enter a value in euros: "))
    pounds = euros * 0.87
    print("The value in pounds is", pounds)


# Write your code here

def say_name():
    print("Hello my name is Rinalds.")


def say_hello_2():
    print("hello")
    print("world")


def dollars_to_pounds():
    dollars = float(input("Input the dollar value you want to convert:"))
    pounds = round((dollars * 1.35) , 2)
    print(f"${dollars} is equivalent to: £{pounds}")


def sum_and_difference():
    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number:"))
    sum = round((num1 + num2), 3)
    difference = round((num1 - num2), 3)
    print("The sum of your two numbers is:", sum)
    print("The difference between your two numbers is:", difference)


def change_counter():
    one_p = int(input("How many 1p coins do you have? "))
    two_p = int(input("How many 2p coins do you have? ")) * 2
    five_p = int(input("How many 5p coins do you have? ")) * 5
    total_p = one_p + two_p + five_p
    print("You have a total of", total_p, "pennies.")


def ten_hellos():
    for i in range(10):
        print("Hello World")


def zoom_zoom():
    zoom_range = int(input("Enter how many zooms you would like: "))
    for i in range(zoom_range):
        print("Zoom", i + 1)


def count_to():
    count_to = int(input("Enter a number to count to: ")) + 1
    for i in range(count_to):
        print(i)


def count_from_to():
    count_start = int(input("Enter a number to count from: "))
    count_end = int(input("Enter a number to count to: ")) + 1
    for i in range(count_start, count_end):
        print(i)


def weights_table():
    kilo_weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print ("    KG  ", "    Oz  ")
    for i in range(len(kilo_weights)):
        ounce_weight = kilo_weights[i] * 35.274
        print("   ", kilo_weights[i], "     ",  ounce_weight)


def future_value():
    investment = round((float(input("Input your initial investment: "))), 2)
    years = int(input("Enter how many years you are investing for: "))

    for i in range(years):
        investment = investment * 1.035
    
    print(f"After {years} years your investment will be worth:", round(investment, 2))

