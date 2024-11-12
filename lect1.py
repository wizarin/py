from graphix import Window, Rectangle, Circle, Point

# Constants
SCREEN = 500
TILE = 100
RADIUS = 50

# Function to draw a rectangle with specified parameters
def draw_rectangle(win, point1, point2, colour):
    rect = Rectangle(point1, point2)
    rect.fill_colour = colour
    rect.draw(win)

# Function to draw a circle with specified parameters
def draw_circle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.fill_colour = colour
    circle.draw(win)

def ex2():
	win = Window("", SCREEN, SCREEN)
	flag = True
	for Y in range(0, SCREEN, TILE):
		for X in range(0, SCREEN, TILE):
			if flag == True:
				tl = Point(X, Y)
				br = Point(X + TILE, Y + TILE)
				draw_rectangle(win, tl, br,"yellow")
			else:
				center = Point(X +(TILE/2), Y +(TILE/2))
				draw_circle(win, center, RADIUS, "red")
			flag = not flag



def ex3():
	win = Window("", SCREEN, SCREEN)
        #flag = True
	lst = [(0,0), (SCREEN -TILE,0), (0,SCREEN-TILE), (SCREEN-TILE,SCREEN-TILE)]
        for Y in range(0, SCREEN, TILE):
                for X in range(0, SCREEN, TILE):
			tl = Point(X, Y)
                        br = Point(X + TILE, Y >
                        draw_rectangle(win, tl,>

			if (X,Y) in lst:
                                center = Point(X +(TILE>
                                draw_circle(win, center>


def ex3():
        win = Window("", SCREEN, SCREEN)
        #flag = True
        lst = [(0,0), (SCREEN -TILE,0), (0,SCREEN-TILE)>
        for Y in range(0, SCREEN, TILE):
                for X in range(0, SCREEN, TILE):
                        tl = Point(X, Y)
                        br = Point(X + TILE, Y >
                        draw_rectangle(win, tl,>

                        if (X == Y) or (X + Y) =
                                center = Point(X + RADIUS, Y + RADIUS)
				draw_circle(win, center, RADIUS, "red")
