# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:33:26 2022

@author: xrap
"""

from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import random
import time

global keep_going
global my_name


def startUp():
    global my_name
    
    def shutdown():
        global my_name
        my_name = textentry.get()
        root.destroy()
    
    root = Tk()
    
    root.geometry("500x500")
    
    img = Image.open("images/image1.png")
    
    img = img.resize((500,500), Image.ANTIALIAS)
    photoImg =  ImageTk.PhotoImage(img)
    
    # Create Canvas
    canvas1 = Canvas( root, width = 500,
                      height = 500)
      
    canvas1.pack(fill = "both", expand = True)
      
    # Display image
    canvas1.create_image( 0, 0, image = photoImg, 
                          anchor = "nw")
    
    textentry = Entry(canvas1)
    canvas1.create_window(250, 400, window=textentry, height=50, width=200)
    
    btn = Button(root, text="Save Name", command=shutdown)
    btn.place(x=225, y=450)
    
    canvas1.create_text( 250, 50, text = "Get ready to be motivated \n    with Shohei Ohtani!", fill='white', font=('Tahoma','24','bold'))
    
    root.mainloop()


def shOwOhtani():
    global keep_going
    global my_name
    
    def shutdown():
        global keep_going
        keep_going = 0
        root.destroy()
    
    root = Tk()
    
    root.geometry("500x500")
    
    pic = random.randint(1,17)
    message = random.randint(1,16)
    exercise = random.randint(1,16)
    
    pic = str(pic)
    
    img = Image.open("images/image"+pic+".png")
    
    # if pic == 1:
    #     img = Image.open("images/image1.png")
    # if pic == 2:
    #     img = Image.open("images/image2.png")
    # if pic == 3:
    #     img = Image.open("images/image3.png")
    # Label(root,image=img).pack()
    
    # img = Image.open("images/image1.png")
    img = img.resize((500,500), Image.ANTIALIAS)
    photoImg =  ImageTk.PhotoImage(img)
    
    # Create Canvas
    canvas1 = Canvas( root, width = 500,
                      height = 500)
      
    canvas1.pack(fill = "both", expand = True)
      
    # Display image
    canvas1.create_image( 0, 0, image = photoImg, anchor = "nw")
    
    # Choose text
    # if message == 1:
    #     words = "Way to go, "+my_name+"!"
    # if message == 2:
    #     words = "Shohei is cool!"
    # if message == 3:
    #     words = "Do jumping jacks!"
    
    if message == 1:
        words = "Way to go, "+my_name+"!"
    if message == 2:
        words = my_name+", you are fun and cool!"
    if message == 3:
        words = "Every strike brings you closer to the next home run."
    if message == 4:
        words = "I think it’s wasteful to limit myself without any reason\n         by saying, ‘it’s my limit’. So should you!"
    if message == 5:
        words = "      You should believe in your talents,\n what you have done, and your potential."
    if message == 6:
        words = "Just do your best, that is most important, "+my_name+"."
    if message == 7:
        words = "The frog in the well knows nothing of the sea."
    if message == 8:
        words = "You can do this, "+my_name+"!"
    if message == 9:
        words = "Impossible is for the unwilling."
    if message == 10:
        words = "You can and you will, "+my_name+"!"
    if message == 11:
        words = "Take a deep breath, you're doing great, "+my_name+"!"
    if message == 12:
        words = "Keep going. All in!"
    if message == 13:
        words = "Whatever you are, be a good one!"
    if message == 14:
        words = "Slow down and breathe, "+my_name+"."
    if message == 15:
        words = "Take it easy and live in the moment."
    if message == 16:
        words = "You're my Angel!"
    
    
    if exercise == 1:
        words1 = "Let's do 20 squats!"
    if exercise == 2:
        words1 = "Let's do 10 push-ups! "
    if exercise == 3:
        words1 = "Let's do 10 lunges per leg!"
    if exercise == 4:
        words1 = "Let's do a 30 second plank!"
    if exercise == 5:
        words1 = "Let's take a 5 minute walk!"
    if exercise == 6:
        words1 = "Let's do 20 bridges!"
    if exercise == 7:
        words1 = "Let's do some shoulder stretches!"
    if exercise == 8:
        words1 = "Let's stand up and stretch!"
    if exercise == 9:
        words1 = "Let's do 10 burpees!"
    if exercise == 10:
        words1 = "Let's do 15 dips!"
    if exercise == 11:
        words1 = "Let's do 30 calf raises!"
    if exercise == 12:
        words1 = "Let's do some toe touches!"
    if exercise == 13:
        words1 = "Drink some water!"
    if exercise == 14:
        words1 = "Don't forget to sit up straight!"
    if exercise == 15:
        words1 = "Look away from your screen for 30 seconds"
    if exercise == 16:
        words1 = "Let's jog in place for a minute!"
    
    
    # Add Text
    canvas1.create_text( 250, 50, text = words, fill='white', font=('Tahoma','12','bold'))
    
    canvas1.create_text( 250, 400, text = words1, fill='white', font=('Tahoma','12','bold'))
    
    btn = Button(root, text="Close for Now", command=root.destroy)
    btn.place(x=100, y=450)
    
    btn2 = Button(root, text="Make it Stop", command=shutdown)
    btn2.place(x=300, y=450)
    
    root.mainloop()


keep_going = 1

startUp()

while keep_going == 1:
    
    wait_time = random.randint(2,5)
    time.sleep(wait_time)
    shOwOhtani()

