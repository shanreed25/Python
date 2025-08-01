from turtle import Screen, Turtle


screen = Screen()

# TODO: Get x and y values when you click on the screen
def get_mouse_click_cor(x,y):
    print(x,y)

# when the screen is clicked, it returns the x and y coordinates
screen.onscreenclick(get_mouse_click_cor)