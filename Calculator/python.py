from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    value = ""
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

    elif text!="c":
        value = scvalue.get()+ text

    scvalue.set(value)
    screen.update()

root = Tk()
root.geometry("500x800")
root.title("Calculator")
root.config(bg="black")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


for i in range(9 ,0, -3):
    f = Frame(root, bg="cyan")
    
    for i in range(i, i-3, -1):
        b = Button(f, text=str(i), padx=5, pady=5, font="lucida 35 bold")
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)
        
    f.pack()


f = Frame(root, bg="cyan")

for char in "0-*":
    b = Button(f, text=char, padx=5, pady=5, font="lucida 35 bold")
    b.pack(side=LEFT, padx=8, pady=5)
    b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="cyan")

for char in "/%=":
    b = Button(f, text=char, padx=5, pady=7, font="lucida 35 bold")
    b.pack(side=LEFT, padx=4, pady=5)
    b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="cyan")

b = Button(f, text="c", padx=5, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="clac", padx=5, pady=5, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=5)


b = Button(f, text="+", padx=4, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=5)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()








