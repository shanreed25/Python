from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()


#END**********************************************************



#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# checked_state = IntVar()
    # variable to hold on to checked state, 0 is off, 1 is on.
    # it is a class defined by the tkinter module
    # we add itg to keep track of the value of the component
# variable=checked_state: attaches the checkbox to a the variable




#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()



# Text: entry box that allows you to use multiple lines of text
# Scale: slider that you can move alone its axis and change the value
# Spinbox: sort of a counter which lets you go up and down
# Checkbox: which can be on or off
# Radio Buttons:
# List Box: list of choices you can choose from


#****************************************************************************************************************************
from tkinter import *
import turtle

def button_clicked():
    # Using bracket notation
    # my_label["text"] = my_input.get()
    #***********************************
    # using config method
    new_text = my_input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My TK Window")
window.minsize(width=500, height=300)#
# Adding Padding to the window
window.config(padx=50, pady=50)


# Label********************************************************
my_label = Label(text="I am a label", font=("Arial", 12, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)

# Entry is an input field******************************************************
my_input = Entry(width=10)
# my_input.pack()
# my_input.get()# returns the input as a string
my_input.grid(column=3, row=2)

my_Button = Button(text="BUTTON")
# my_Button.pack()
my_Button.grid(column=1, row=1)
# Adds padding inside the button
my_Button.config(padx=10, pady=10)

button_1 = Button(text="New Button")
button_1.grid(column=2, row=0)


window.mainloop()