import os
from graphix import Window, Point, Text, Rectangle
import random as rand

def student_info():
    course = input("What's your course? ")
    student_id = input("What's your ID number? ")
    print("Welcome to:\t" + course)
    print("\n" * 2 + "Your ID number is:\t" + student_id[2:])


def personal_details():
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    height = float(input("What's your height? "))
    #print("name:\t{:>10}\nage:\t{:>10}\nheight:\t{:>10.2f}".format(name, age, height))
    print(f"name:\t{name:>10}\nage:\t{age:>10}\nheight:\t{height:>10.2f}")


def read_quote():
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))
    # Change directory to the folder containing quotation.txt
    os.chdir("text_files")
    # Checking if quotation.txt is in the current directory:
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))

    input_file = open("quotation.txt", "r")

    # You can use `read()` to read the whole file into a single string
    content = input_file.read()
    print(content)


def write_quote():
    os.chdir("text_files")
    output_file = open("my_quotation.txt", "w")

    # You can use `write()` to write a single string
    print("I love Python!", file=output_file)
    print("(Matthew Poole)", file=output_file)

    # Or write both lines in one go separated by a newline character ('\n')
    # content = "I love Python!\n(Matthew Poole)"
    # output_file.write(content)


# Solutions below:


def personal_greeting():
    user_name = input("Enter your name: ")
    print(f"Hello {user_name}, nice to see you!")


def formal_name():
    first_name = input("Enter your first name: ")
    second_name = input("Enter your surname: ")
    first_letter = first_name[:1]
    print(f"Hello {first_letter}. {second_name}, nice to see you!")


def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
    print(f"{kilos:.2f} kilos is equal to {ounces:.2f} ounces")


def generate_email():
    forename = input("Enter your forename: ")
    surname = input("Enter your surname: ")
    year = input("Enter the year you entered university: ")
    first_letter = forename[:1].lower()
    short_surname = surname[:4].lower()
    short_year = int(year[-2:])
    print("Your email is: ")
    print(f"{short_surname}.{first_letter}.{short_year}@myport.ac.uk")


def grade_test():
    num_grade = int(input("Enter your grade from 0 to 10: "))
    letter_grade = ["F", "F", "F", "F", "C", "C", "B", "B", "A", "A", "A"]
    grade = letter_grade[num_grade]
    print(f"Number grade {num_grade} is equivalent to grade {grade}")


def graphics_letters():
    win = Window()
    word = input("Enter a word: ")
    message = Text(Point(200,20), "Click to place a letter of your word")
    message.draw(win)
    for i in range(len(word)):
        click = win.get_mouse()
        letter = word[i]
        placed_letter = Text(click, letter)
        placed_letter.size = rand.randint(5,35)
        placed_letter.draw(win)
    
    message.text = "Click anywhere to quit"
    win.get_mouse()
    win.close()#Prevents the graphix window closing until user interacts


def sing_a_song():
    word = input("Enter the word for your song: ")
    line_count = int(input("Enter how many lines: "))
    rep_count = int(input("Enter number of words per line: "))
    for i in range(line_count):
        print(f"{word} "* rep_count, "\n")


def exchange_table():
    euro = range(20)
    exchange = 1.17
    pound = []
    print("\t  Euro\t\t Pound ")
    for i in range(len(euro)):
        pound.append(euro[i] * exchange)
        print(f"\t {euro[i]:>5}\t\t {pound[i]:>5.2f}")
    

def make_initialism():
    phrase = input("Enter a phrase: ")
    word_list = phrase.split()
    initialism =""
    for i in range(len(word_list)):
        word = word_list[i]
        initialism += word[0]
    print ("The initials of the phrase are: ", initialism.upper())


def file_in_caps():
    file_name = input("Enter the name of a text file: ") + ".txt"
    file = open(file_name, "r")
    file = file.read().upper()
    print("\n", file)


def total_spending():
    with open("spending.txt") as input_file:
        week_spend = input_file.readlines()
        total = 0
        for i in range(len(week_spend)):  
            total += float(week_spend[i])
        print(f"You have spent a total of £{total:.2f} this week.")


def name_to_number():
    name = input("Enter your name: ")
    value = 0
    for letter in range(len(name)):
        value += int(ord(name[letter]))
    print(f"The numerical value of your name is {value}")


def rainfall_chart():
    with open("rainfall.txt") as input_file:
        records = input_file.readlines()
        for record in records:
            city, rainfall = record.split()
            print(f"{city}","*" * int(rainfall))


def rainfall_graphics():
    win = Window("Rainfall chart")
    colour = ["red", "blue", "yellow", "green", "purple", "brown", "orange"]
    bar_width = 15
    length_multiplier = 5
    chart_top = 100
    with open("rainfall.txt") as input_file:
        records = input_file.readlines()
        for record in records:
            city, rainfall = record.split()
            #Coordinates for bar
            bar_length = int(rainfall) * length_multiplier
            c1 = Point(100, chart_top)
            chart_top += 15
            c2 = Point((150 + bar_length), (c1.y + bar_width))
            #Label for bar
            label = Text(Point(50, c1.y + (int(bar_width/2))), city)
            label.size = 10
            label.draw(win)
            #Bar in graph
            bar = Rectangle(c1, c2)
            rand_colour = int(rand.randint(0, (len(colour))-1))
            bar.fill_colour = colour[rand_colour]
            bar.draw(win)
    message = Text(Point(200, 50), "Click anywhere to quit")
    message.draw(win)
    win.get_mouse() #Prevents the graphix window closing until user interacts
    win.close()

def rainfall_in_inches():
    with open("rainfall.txt") as rain_file:
        with open("rainfallInches.txt", "w") as inch_file:
            records = rain_file.readlines()
            for record in records:
                city, rain_mm = record.split()
                inch = float(rain_mm) * 25.4 
                print(f"{city} {inch:.2f}", file=inch_file)


def wc():
    file_name = (input("Enter the name of a text file: ") + ".txt")
    print(file_name)
    with open(file_name, "r") as input_file: 
        records = input_file.readlines()
        total_lines = len(records)
        total_words = 0
        total_chr = 0
        for record  in records:
            words = record.split()
            total_words += len(words)
            for word in words:
                total_chr += len(word)
        print(f"Lines = {total_lines}, Words = {total_words}, Characters = {total_chr}")



