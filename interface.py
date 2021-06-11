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

def rien():
    print("None")

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
displayEntry = tk.Entry(window, textvariable=display, bg="#232F4E", fg=ColorFont, bd=0, font=('Bahnschrift SemiBold', 20))
displayEntry.place(x=10, y=10, width=330, height=100)

#Numbers button
zero_button = tk.Button(window, text="0", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
zero_button.place(x=10, y=360, width=160, height=50)

one_button = tk.Button(window, text="1", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
one_button.place(x=10, y=300, width=75, height=50)

two_button = tk.Button(window, text="2", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
two_button.place(x=95, y=300, width=75, height=50)

three_button = tk.Button(window, text="3", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
three_button.place(x=180, y=300, width=75, height=50)

four_button = tk.Button(window, text="4", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
four_button.place(x=10, y=240, width=75, height=50)

five_button = tk.Button(window, text="5", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
five_button.place(x=95, y=240, width=75, height=50)

six_button = tk.Button(window, text="6", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
six_button.place(x=180, y=240, width=75, height=50)

seven_button = tk.Button(window, text="7", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
seven_button.place(x=10, y=180, width=75, height=50)

eight_button = tk.Button(window, text="8", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
eight_button.place(x=95, y=180, width=75, height=50)

nine_button = tk.Button(window, text="9", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
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

C_button = tk.Button(window, text="C", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
C_button.place(x=10, y=120, width=75, height=50)

sign_button = tk.Button(window, text="+/-", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
sign_button.place(x=95, y=120, width=75, height=50)

square_button = tk.Button(window, text="x²", font=('Bahnschrift SemiBold', 25), bg=ColorButton, fg=ColorFont, bd=0,command=rien)
square_button.place(x=180, y=120, width=75, height=50)
#Display of the window.
window.mainloop()