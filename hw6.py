from tkinter import *

top = Tk()

batman_c = 0
superman_c = 0
spiderman_c = 0
wonderwoman_c = 0

def hitBatman():
    global batman_c
    batman_c = batman_c + 1
    batman_l['text'] = batman_c
    winner()
    
def superman():
    global superman_c
    superman_c = superman_c + 1
    superman_l['text'] = superman_c
    winner()

def spiderman():
    global spiderman_c
    spiderman_c = spiderman_c + 1
    spiderman_l['text'] = spiderman_c
    winner()

def wonderwoman():
    global wonderwoman_c
    wonderwoman_c = wonderwoman_c + 1
    wonderwoman_l['text'] = wonderwoman_c
    winner()

def winner():
    if batman_c > superman_c and batman_c > spiderman_c and batman_c > wonderwoman_c:
        winner_l['text'] = 'batman'
    elif superman_c > batman_c and superman_c > spiderman_c and superman_c > wonderwoman_c:
        winner_l['text'] = 'superman'
    elif spiderman_c > batman_c and spiderman_c > superman_c and spiderman_c > wonderwoman_c:
        winner_l['text'] = 'spiderman'
    elif wonderwoman_c > batman_c and wonderwoman_c > superman_c and wonderwoman_c > spiderman_c:
        winner_l['text'] = 'wonderwoman'
    else:
        winner_l['text'] = 'tied'

top['bg'] = 'light gray'
frame1 = Frame(top, bg = 'white')
frame1.pack()
Label(frame1, text = "Vote for your favorite superhero!").pack()

frame2 = Frame(top, bg = 'light gray')
frame2.pack()


Label(frame2, text = "SUPERHERO").grid(row = 0, column = 0)
Label(frame2, text = "VOTES").grid(row = 0, column = 1, pady = 10)


batman_l = Label(frame2, text = batman_c)
batman_l.grid(row = 1, column = 1)
Button(frame2, text = "Batman", bg = 'black', fg = 'white', command = hitBatman, width = 15).grid(row = 1, column = 0, pady = 5)


Button(frame2, text = "Superman", bg = "blue", fg = 'white', command = superman, width = 15).grid(row = 2, column = 0, pady = 5)
superman_l = Label(frame2, text = superman_c)
superman_l.grid(row = 2, column = 1)

Button(frame2, text = "Spiderman", bg = 'red', command = spiderman, width = 15).grid(row = 3, column = 0, pady = 5)
spiderman_l = Label(frame2, text = spiderman_c)
spiderman_l.grid(row = 3, column = 1)

Button(frame2, text = "Wonder Woman", bg = 'yellow', command = wonderwoman, width = 15).grid(row = 4, column = 0, pady = 5)
wonderwoman_l = Label(frame2, text = wonderwoman_c)
wonderwoman_l.grid(row = 4, column = 1)


Label(frame2, text = "Winner so far").grid(row = 5, column = 0, pady = 8)
winner_l = Label(frame2, text = "VOTES")
winner_l.grid(row = 5, column = 1)

mainloop()

