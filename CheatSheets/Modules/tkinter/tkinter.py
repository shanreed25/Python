from tkinter import *


window = Tk()
window.title("Cheatsheet")
window.config(padx=50, pady=50)

def my_func():
    pass

#TODO: Canvas()
canvas = Canvas(width=300, height=414)

#TODO: PhotoImage()
my_img = PhotoImage(file="image.png")
canvas.create_image(150, 207, image=my_img)
my_text = canvas.create_text(150, 207, width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

#TODO: Change canvas create_text
canvas.itemconfig(my_text, text="new text")

#TODO: Button()
my_button = Button(image=my_img, highlightthickness=0, command=my_func)
my_button.grid(row=1, column=0)

my_button = Button(image=my_img, text="known", command=my_func)
my_button.config( relief="flat", borderwidth=0, highlightthickness=0)
my_button.grid(row=1, column=1)



window.mainloop()