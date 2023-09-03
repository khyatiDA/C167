from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Working On Canvas Using Functions")
window.geometry("1000x600")

label = Label(window, text = "Choose Color :")
label.place(relx = 0.6, rely = 0.9, anchor = CENTER)

canvas = Canvas(window, width = 990, height = 490, bg = "white", highlightbackground = "grey")
canvas.pack()

fill_color = ["Blue", "Green", "Red", "Yellow"]
color_dropdown = ttk.Combobox(window, state = "readonly", values = fill_color, width = 10)
color_dropdown.place(relx = 0.8, rely = 0.9, anchor = CENTER)

coordinates_values = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

startx = Label(window, text = "Start - X")
startx.place(relx = 0.1, rely = 0.85, anchor = CENTER)

d1 = ttk.Combobox(window, state = "readonly", values = coordinates_values, width = 10)
d1.place(relx = 0.2, rely = 0.85, anchor = CENTER)

starty = Label(window, text = "Start - Y")
starty.place(relx = 0.3, rely = 0.85, anchor = CENTER)

d2 = ttk.Combobox(window, state = "readonly", values = coordinates_values, width = 10)
d2.place(relx = 0.4, rely = 0.85, anchor = CENTER)

endx = Label(window, text = "End - X")
endx.place(relx = 0.5, rely = 0.85, anchor = CENTER)

d3 = ttk.Combobox(window, state = "readonly", values = coordinates_values, width = 10)
d3.place(relx = 0.6, rely = 0.85, anchor = CENTER)

endy = Label(window, text = "End - Y")
endy.place(relx = 0.7, rely = 0.85, anchor = CENTER)

d4 = ttk.Combobox(window, state = "readonly", values = coordinates_values, width = 10)
d4.place(relx = 0.8, rely = 0.85, anchor = CENTER)

def circle(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    
    keypress = 'c'
    draw(keypress, oldx, oldy, newx, newy)
    
def rectangle(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    
    keypress = 'r'
    draw(keypress, oldx, oldy, newx, newy)
    
def line(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    
    keypress = 'l'
    draw(keypress, oldx, oldy, newx, newy)

def draw(direction, oldx, oldy, newx, newy):
    color = color_dropdown.get()
    if(direction == 'c'):
        draw_circle = canvas.create_oval(oldx, oldy, newx, newy,width = 3, fill = color)
        
    if(direction == 'r'):
        draw_rectangle = canvas.create_rectangle(oldx, oldy, newx, newy,width =3 ,  fill = color)
        
    if(direction == 'l'):
        draw_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = color)
        
window.bind("{c}", circle)
window.bind("{r}", rectangle)
window.bind("{l}", line)

window.mainloop()