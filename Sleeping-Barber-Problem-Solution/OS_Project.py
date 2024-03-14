from threading import *
import time
from tkinter import *
from PIL import ImageTk, Image
custready=0
access=1
noofseats=4
come=0
def SBP():
    global c
    root=Tk()
    root.title("Sleeping Barber Problem Solution")
    
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Set window size to 80% of screen size
    window_width = int(screen_width * 0.8)
    window_height = int(screen_height * 0.8)
    
    root.geometry(f"{window_width}x{window_height}")
    c = Canvas(root, bg='cyan', height=window_height, width=window_width)
    c.pack()
    
    img = ImageTk.PhotoImage(Image.open("images/bg.png"))  
    c.create_image(0, 0, anchor=NW, image=img)
    c.create_rectangle(100, 100, window_width - 100, window_height - 100, fill='white')
    c.create_rectangle(110, 110, 500, window_height - 160, fill='white')
    c.create_rectangle(510, 110, 1100, window_height - 160, fill='white')
    c.create_rectangle(1110, 110, window_width - 110, window_height - 160, fill='white')
    
    fnt = ('Times', 28, 'bold','underline')
    c.create_text(500, 50, text="SLEEPING BARBER PROBLEM SOLUTION . . .", font=fnt, fill='BLACK')
    fnt = ('Times', 28, 'bold','underline')
    c.create_text(300, 150, text="MAIN ROOM", font=fnt, fill='black')
    c.create_text(800, 150, text="WAITING ROOM", font=fnt, fill='black')
    c.create_text(1250, 150, text="ENTRY DOOR", font=fnt, fill='black') 
    
    fnt = ('Times', 30, 'bold')
    b1 = Button(c, text="ENTER", font=fnt, command= lambda: buttonClick())
    b1.place(x=window_width // 2 - 100, y=window_height - 120, width=200, height=70)
    root.mainloop()
    
def buttonClick():
    global come    
    come=1

def signal1(s):
    global custready
    custready=s
    custready=custready+1

def wait1(s):
    global custready,c,img19
    cnt=0
    custready=s
    if custready==0:
        print("Barber is Sleeping")
        img1 = ImageTk.PhotoImage(Image.open("images/sleepingbarber.png"))  
        c.create_image(170, 230, anchor=NW, image=img1)
        img2 = ImageTk.PhotoImage(Image.open("images/chairs.png"))  
        c.create_image(620, 250, anchor=NW, image=img2)
    while(custready<=0):
        cnt=1
    if cnt==1:
        cnt=0
        print("Barber Wake Up")
        img3 = ImageTk.PhotoImage(Image.open("images/wakeupbarber.png"))  
        c.create_image(170, 230, anchor=NW, image=img3)
        time.sleep(1)
        img19 = ImageTk.PhotoImage(Image.open("images/readybarber.png"))  
        c.create_image(170, 230, anchor=NW, image=img19)     
    custready=custready-1

def signal2(s):
    global access
    access=s
    access=access+1

def wait2(s):
    global access
    access=s
    while(access<=0):
        pass
    access=access-1

class Barber(Thread):
    def run(self):
        global custready,access,noofseats,c
        while(True):
            wait1(custready)
            wait2(access)
            time.sleep(0.2)
            print("Customer Enters into Main Room")
            if custready==1:
                img4 = ImageTk.PhotoImage(Image.open("images/1person.png"))  
                c.create_image(620, 250, anchor=NW, image=img4)
            elif custready==2:
                img5 = ImageTk.PhotoImage(Image.open("images/2person.png"))
                c.create_image(620, 250, anchor=NW, image=img5)
            elif custready==3:
                img6 = ImageTk.PhotoImage(Image.open("images/3person.png"))  
                c.create_image(620, 250, anchor=NW, image=img6)
            elif custready==4:
                img7 = ImageTk.PhotoImage(Image.open("images/4person.png"))
                c.create_image(620, 250, anchor=NW, image=img7)
            else:
                img8 = ImageTk.PhotoImage(Image.open("images/chairs.png"))
                c.create_image(620, 250, anchor=NW, image=img8)
            time.sleep(1)        
            noofseats=noofseats+1
            print("started cutting")
            img9 = ImageTk.PhotoImage(Image.open("images/workingbarber.png"))  
            c.create_image(170, 230, anchor=NW, image=img9)
            time.sleep(10)
            print("Cutting complete")
            img10 = ImageTk.PhotoImage(Image.open("images/readybarber.png"))  
            c.create_image(170, 230, anchor=NW, image=img10)
            time.sleep(1)
            signal2(access)

class Customer(Thread):
    def run(self):
        global custready,access,noofseats,come,c
        while(True):
            if come==1:
                come=0
                img16 = ImageTk.PhotoImage(Image.open("images/entering.png"))  
                i16=c.create_image(1120, 250, anchor=NW, image=img16)
                time.sleep(1)
                c.delete(i16)
                if noofseats>0:
                    print("Customer Enters into Waiting Room")
                    noofseats=noofseats-1
                    signal1(custready)
                    if custready==1:
                        img11 = ImageTk.PhotoImage(Image.open("images/1person.png"))  
                        c.create_image(620, 250, anchor=NW, image=img11)
                    elif custready==2:
                        img12 = ImageTk.PhotoImage(Image.open("images/2person.png"))  
                        c.create_image(620, 250, anchor=NW, image=img12)
                    elif custready==3:
                        img13 = ImageTk.PhotoImage(Image.open("images/3person.png"))  
                        c.create_image(620, 250, anchor=NW, image=img13)
                    elif custready==4:
                        img14 = ImageTk.PhotoImage(Image.open("images/4person.png"))  
                        c.create_image(620, 250, anchor=NW, image=img14)
                    else:
                        img15 = ImageTk.PhotoImage(Image.open("images/chairs.png"))
                        c.create_image(620, 250, anchor=NW, image=img15)
                    time.sleep(1)
                elif noofseats==0:
                    img17 = ImageTk.PhotoImage(Image.open("images/nospace.png"))  
                    i17=c.create_image(1120, 250, anchor=NW, image=img17)
                    time.sleep(0.5)
                    c.delete(i17)
                    img18 = ImageTk.PhotoImage(Image.open("images/leaving.png"))  
                    i18=c.create_image(1120, 250, anchor=NW, image=img18)
                    time.sleep(1)
                    c.delete(i18)
                    print("Customer Enters But There is No Space, Customer Leaves")
b=Barber()
c=Customer()
b.start()
c.start()
SBP()
