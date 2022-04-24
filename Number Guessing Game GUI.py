from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import random

#number = None
tries = 0

def think_number(a = 1, b = 100):
    global number
    number = random.randint(1,100)

think_number()

def check_number():
    global number, tries
    tries+=1
    our_num = int(entry.get())
    if our_num > number:
        main_label.configure(text=f'The Number is Smaller then '+ str(our_num))
        Tries.configure(text=f'Tries: {str(tries)}')
        Tries.text=str(f'Tries: {str(tries)}')
        image.configure(image=im_laugh)
        image.image = im_laugh
    elif our_num < number:
        main_label.configure(text=f'The Number is Greater then ' + str(our_num))
        Tries.configure(text=f'Tries: {str(tries)}')
        Tries.text = str(f'Tries: {str(tries)}')
        image.configure(image=im_laugh)
        image.image = im_laugh
    elif our_num == number:
        main_label.configure(text=f'Wow! You got it ')
        Tries.configure(text=f'Tries: {str(tries)}')
        Tries.text = str(f'Tries: {str(tries)}')
        image.configure(image=im_over)
        image.image = im_over

win = Tk()
win.configure(bg='white')
win.geometry('400x400')
win.title("Number Guessing Game - Sourav Ghosh")

im_think = ImageTk.PhotoImage(file="thinking.jpeg")
im_laugh = ImageTk.PhotoImage(file="laughing.jpg")
im_over = ImageTk.PhotoImage(file="over.jpeg")

main_label = Label(win,text="Let me guess a number", bg='white')
main_label.pack(pady=15)

image = Label(win,image=im_think, border=0)
image.pack(pady= 15)

user_input = Label(win,text='Enter Your Number Here : ', bg='white')
user_input.pack()

entry = ttk.Entry(win)
entry.pack(pady = 15)

button = ttk.Button(win, text='Check', command = check_number)
button.pack()

Tries = Label(win, text=f'Tries: {tries}', bg='white')
Tries.pack(side='left')

win.mainloop()