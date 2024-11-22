from graphix import Window, Rectangle, Circle, Point

# Constants
SCREEN = 500
TILE = 100
RADIUS = 50
SMALL_TILE = 20
SMALL_RADIUS = 10

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
    
def draw_tiled_rectangles_with_circles():
    win = Window("Tiled Rectangles with Circles",SCREEN, SCREEN)
    for Y in range(0, SCREEN, TILE):
        for X in range(0, SCREEN, TILE):
            # Draw rectangle
            p1 = Point(X, Y)
            p2 = Point(X + TILE, Y + TILE)
            draw_rectangle(win, p1, p2, "blue")
            # Draw circle
            center = Point(X + RADIUS, Y + RADIUS)
            draw_circle(win, center, RADIUS, "red")
    
    win.get_mouse()
    win.close()

draw_tiled_rectangles_with_circles()