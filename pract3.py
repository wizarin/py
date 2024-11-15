from graphix import Window, Circle, Line, Point, Rectangle, Text, Entry
import math

def draw_stick_figure():
    win = Window()
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

    message = Text(Point(200, 50), "Click anywhere to quit")
    message.draw(win)
    win.get_mouse() #Prevents the graphix window closing until user interacts
    win.close()


def draw_circle():
    win = Window()
    centre = Point(int(win.width/2), int(win.height/2))
    radius = int(input("Choose radius of circle:"))
    circle = Circle(centre, radius)
    circle.draw(win)

    message = Text(Point(200, 50), "Click anywhere to quit")
    message.draw(win)
    win.get_mouse() #Prevents the graphix window closing until user interacts
    win.close()


def draw_archery_target():
    win = Window("Click window to close")
    centre = Point(int(win.width/2), int(win.height/2))
    radius = int(input("Choose radius of circle:"))
    
    blue_circle = Circle(centre, radius * 3)
    blue_circle.draw(win)
    blue_circle.fill_colour = "blue"

    red_circle = Circle(centre, radius * 2)
    red_circle.draw(win)
    red_circle.fill_colour = "red"

    yellow_circle = Circle(centre, radius)
    yellow_circle.draw(win)
    yellow_circle.fill_colour = "yellow"

    message = Text(Point(200, 50), "Click anywhere to quit")
    message.draw(win)
    win.get_mouse() #Prevents the graphix window closing until user interacts
    win.close()


def draw_rectangle():
    win = Window("Click window to close")
    height = int(input("Enter the height of your rectangle: "))
    width = int(input("Enter the width of your rectangle: "))
    p1_x = round(200 - (width / 2))
    p2_x = round(200 + (width / 2))
    p1_y = round(200 - (height / 2)) 
    p2_y = round(200 + (height / 2))

    rectangle = Rectangle(Point(p1_x, p1_y), Point(p2_x, p2_y))
    rectangle.draw(win)

    message = Text(Point(200, 50), "Click anywhere to quit")
    message.draw(win)
    win.get_mouse() #Prevents the graphix window closing until user interacts
    win.close()


def blue_circle():
    win = Window("Click window to close")
    centre = win.get_mouse()
    circle = Circle(centre, 100)
    circle.draw(win)
    circle.fill_colour = "blue"

    message = Text(Point(200, 50), "Click anywhere to quit")
    message.draw(win)
    win.get_mouse() #Prevents the graphix window closing until user interacts
    win.close()


def ten_lines():
    win = Window()
    message = Text(Point(200, 50), "")
    message.draw(win)
    for i in range(10):
        message.text = "Click on first point"
        p1 = win.get_mouse()
        message.text = "Click on second point"
        p2 = win.get_mouse()
        line = Line(p1, p2)
        line.draw(win)

    message.text = "Click anywhere to quit"
    win.get_mouse()
    win.close()
    

def ten_strings():
    win = Window()
    message = Text(Point(200, 50), "Enter a string and click to place it")
    input_box = Entry(Point(200,100), 20)
    message.draw(win)
    input_box.draw(win)  
    for i in range(10):
        click = win.get_mouse()
        user_string = Text(click, input_box.text)
        user_string.draw(win)
        input_box.text = ""

    message.text = "Click anywhere to quit"
    win.get_mouse()
    win.close()


def ten_coloured_rectangles():
    win = Window()
    message = Text(Point(200, 20), "")
    colour_input = Entry(Point(200, 60), 20)
    message.draw(win)
    colour_input.draw(win)
    colour_input.text = "blue"
    for i in range(10):
        message.text = "Click on first corner"
        p1 = win.get_mouse()
        message.text = "Click on second corner"
        p2 = win.get_mouse()   
        rectangle = Rectangle(p1, p2)
        rectangle.fill_colour = colour_input.text
        rectangle.draw(win)


    message.text = "Click anywhere to quit"
    win.get_mouse() #Prevents the graphix window closing until user interacts
    win.close()


def five_click_stick_figure():
    win = Window()
    message = Text(Point(200, 20), "Click for head position")
    message.draw(win)
    head_centre = win.get_mouse()
    head_centre.draw(win)
    #Head
    message.text = "Click for head size"
    head_size = win.get_mouse()
    radius = round(math.sqrt(pow((head_centre.x) - (head_size.x), 2) + 
                             pow((head_centre.y) - (head_size.y), 2)))
    head = Circle(head_centre, radius)
    head.draw(win)
    #Torso
    message.text = "Click for torso length"
    torso_bottom = win.get_mouse()
    torso_bottom = Point(head_centre.x, torso_bottom.y)
    torso_top = head_centre.y + radius
    torso_top = Point(head_centre.x, torso_top)
    torso = Line(torso_top, torso_bottom)
    torso.draw(win)
    #Arms
    message.text = "Click for arm height and length"
    arm_start = win.get_mouse()
    arm_start_y = arm_start.y
    if arm_start_y < torso_top.y:
        arm_start_y = torso_top.y
    if arm_start_y > torso_bottom.y:
        arm_start_y = torso_bottom.y
    arm_length = torso_top.x - arm_start.x
    arm_end = Point(torso_top.x + arm_length, arm_start_y)
    arm = Line(Point(arm_start.x, arm_start_y), arm_end)
    arm.draw(win)
    #Legs
    message.text = "Click for leg height and length"
    leg1_end = win.get_mouse()
    leg1 = Line(torso_bottom, leg1_end)
    leg_dist = torso_top.x - leg1_end.x
    leg2_end = Point(torso_top.x + leg_dist, leg1_end.y)
    leg2 = Line(torso_bottom, leg2_end)
    leg1.draw(win)
    leg2.draw(win)

    message.text = "Click anywhere to quit"
    win.get_mouse() #Prevents the graphix window closing until user interacts
    win.close()
    

