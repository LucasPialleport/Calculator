import tkinter as tk

#---Function---
def center_window(width, height):

    # get screen width et height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calcule position x et y
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

def insert1():
    if int(display.get()) == 0:
        print("test")
        displayEntry.delete(0, 'end')
        displayEntry.insert(0, "1")
    else :
        displayEntry.insert('end', "1")
def insert2():
    if int(display.get()) == 0:
        displayEntry.delete(0, 'end')
        displayEntry.insert(0, "2")
    else :
        displayEntry.insert('end', "2")
def insert3():
    if int(display.get()) == 0:
        displayEntry.delete(0, 'end')
        displayEntry.insert(0, "3")
    else :
        displayEntry.insert('end', "3")
def insert4():
    if int(display.get()) == 0:
        displayEntry.delete(0, 'end')
        displayEntry.insert(0, "4")
    else :
        displayEntry.insert('end', "4")
def insert5():
    if int(display.get()) == 0:
        displayEntry.delete(0, 'end')
        displayEntry.insert(0, "5")
    else :
        displayEntry.insert('end', "5")
def insert6():
    if int(display.get()) == 0:
        displayEntry.delete(0, 'end')
        displayEntry.insert(0, "6")
    else :
        displayEntry.insert('end', "6")
def insert7():
    if int(display.get()) == 0:
        displayEntry.delete(0, 'end')
        displayEntry.insert(0, "7")
    else :
        displayEntry.insert('end', "7")
def insert8():
    if int(display.get()) == 0:
        displayEntry.delete(0, 'end')
        displayEntry.insert(0, "8")
    else :
        displayEntry.insert('end', "8")
def insert9():
    if int(display.get()) == 0:
        displayEntry.delete(0, 'end')
        displayEntry.insert(0, "9")
    else :
        displayEntry.insert('end', "9")
def insert0():
    if display != 0:
        displayEntry.insert('end', "0")

def C():
    displayEntry.delete(0, 'end')
    displayEntry.insert(0, "0")

def sign_change():
    if int(display.get()) > 0:
        displayEntry.insert(0, "-")
    elif int(display.get()) < 0:
        displayEntry.delete(0, 1)

def rien():
    pass

#---Tkinter---
#Variables
ColorFont = "black"
ColorBackground = "#e6e6e6"
ColorButton = "#f2f2f2"
ColorButtonClick = "#a2a2a2"

#Initialization :
window = tk.Tk()
window.title("Calculatrice")
center_window(350,420)
window.resizable(0, 0)
window.configure(bg=ColorBackground)

#display bar
display = tk.StringVar(window)
displayEntry = tk.Entry(window, textvariable=display, bg=ColorBackground, fg=ColorFont, bd=0, font=('Bahnschrift SemiBold', 20), state='normal', justify = tk.RIGHT)
displayEntry.place(x=10, y=10, width=330, height=100)
displayEntry.insert(0, "0")

#Numbers button
zero_button = tk.Button(window, text="0", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=insert0)
zero_button.place(x=10, y=360, width=160, height=50)

one_button = tk.Button(window, text="1", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=insert1)
one_button.place(x=10, y=300, width=75, height=50)

two_button = tk.Button(window, text="2", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=insert2)
two_button.place(x=95, y=300, width=75, height=50)

three_button = tk.Button(window, text="3", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=insert3)
three_button.place(x=180, y=300, width=75, height=50)

four_button = tk.Button(window, text="4", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=insert4)
four_button.place(x=10, y=240, width=75, height=50)

five_button = tk.Button(window, text="5", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=insert5)
five_button.place(x=95, y=240, width=75, height=50)

six_button = tk.Button(window, text="6", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=insert6)
six_button.place(x=180, y=240, width=75, height=50)

seven_button = tk.Button(window, text="7", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=insert7)
seven_button.place(x=10, y=180, width=75, height=50)

eight_button = tk.Button(window, text="8", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=insert8)
eight_button.place(x=95, y=180, width=75, height=50)

nine_button = tk.Button(window, text="9", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=insert9)
nine_button.place(x=180, y=180, width=75, height=50)

#Operation button
divide_button = tk.Button(window, text="÷", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
divide_button.place(x=265, y=120, width=75, height=50)

multiply_button = tk.Button(window, text="×", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
multiply_button.place(x=265, y=180, width=75, height=50)

subtract_button = tk.Button(window, text="-", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
subtract_button.place(x=265, y=240, width=75, height=50)

add_button = tk.Button(window, text="+", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
add_button.place(x=265, y=300, width=75, height=50)

equal_button = tk.Button(window, text="=", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
equal_button.place(x=265, y=360, width=75, height=50)

#Other button
dot_button = tk.Button(window, text=".", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
dot_button.place(x=180, y=360, width=75, height=50)

C_button = tk.Button(window, text="C", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=C)
C_button.place(x=10, y=120, width=75, height=50)

sign_button = tk.Button(window, text="+/-", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=sign_change)
sign_button.place(x=95, y=120, width=75, height=50)

square_button = tk.Button(window, text="x²", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
square_button.place(x=180, y=120, width=75, height=50)

#Display of the window.
window.mainloop()