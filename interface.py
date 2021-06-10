import tkinter as tk

def center_window(width, height):

    # get screen width et height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calcule position x et y
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

window = tk.Tk()
window.title("Calculatrice")
center_window(318,468)
window.resizable(0, 0)

window.mainloop()