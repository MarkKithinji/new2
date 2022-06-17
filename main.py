

from tkinter import *
from tkinter import font
import tkinter.messagebox
from turtle import title
from studentfile import *
from teacherfile import *
from roomsfile import *
from tkinter import font as tkFont
from Dwarning1 import *

# import os



window =Tk()
window.title("information center".upper())
window.configure(bg='#D3D3D3')
#window.Title("school information desk")
# def main_screen():
#     screen=Tk
#     screen.geometry('1280x720+150+80')
#     screen.configure(bg='D3D3D3')
#     #trying to get a good icon
#     image_icon=PhotoImage(file='Wasserabweisend Homedeco Coral sea weed.jfif')
#     screen.iconphoto(False, image_icon)
#     screen.title('main window'.upper())
# main_screen()
window.geometry('750x900')

# class login:
#     def __init__(self, window):
#         self.window = window
#         self.bg= ImageTK.PhotoImage(file='images/1.jpg')
#         self.bg_image=Label(self.window, image= self.bg).place(x=0,y=0, relwidth=1, relheight=1)


Label(window, text= 'please enter your password :'.upper(), bg='#D3D3D3').place(x=20, y=40)
########################### password ####################3


#creating a pop up message for accepted password

#giving a function  to password button
def passC():
    
    if pass1=='1234' and name_== 'mark':
        print('accept')
    else:
        warn1()
    
    
#lcd = tkFont.Font(family='lcdmono2', size=36, weight='bold')

buttonpass= Button(window, height=3, width=45, command=passC,text='SUBMIT?', font='elephant', bg='grey', borderwidth=7).place(x=150, y=120)



#adding a text place for password
pass1=StringVar()
pass1=Entry(window, width=23, borderwidth=3, bg='#D3D3D3', textvariable=pass1)
pass1.insert(0,'PASSWORD')
pass1.place(x=22, y=60)

#adding directing message
Label(window, text='Please enter your name :'.upper(), bg='#D3D3D3').place(x=500, y=40)

# buttonpass= Button(window, height=5, width=20, text='Submit ! *-*').place(x=500, y=120)

name_=StringVar()
name_=Entry(window, width=24, borderwidth=3, bg='#D3D3D3')
name_.insert(0,'NAME')
name_.place(x=500, y=60)


label=Label(window, text='-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', bg='#D3D3D3').place(x=1,y=220)

Label(window, text= 'student info:', bg='#D3D3D3').place(x=20, y=240) 
# s_name_box=Entry(window)
# e= Entry(window, width= 50, bg= '#D3D3D3',borderwidth= '5' )
# e.insert(0, 'Enter student name, pronoun, admission number, subject and average grade')
# e.place(x=150, y=20)
#btn 1
# input1= StringVar()
# e_s= Entry(window, width= 40, borderwidth=3, fg='grey', textvariable=input1)
# e_s.insert(0, 'enter your name')
# e_s.place(x= 20, y= 70)
# #btn 2
# input2= StringVar()
# e_s2= Entry(window, width= 40, borderwidth=3, fg='grey', textvariable=input2)
# e_s2.insert(0, 'enter your password')
# e_s2.place(x= 20, y= 100)
def myClick():
    win2()
    
    myLabel= Label (window, text= 'submiting', bg='#D3D3D3')
    myLabel.place(x=350, y=600)

mybutton=Button (window, text='Browse',width=70, command= myClick, bg='#D3D3D3', fg='#000000')
mybutton.place(x= 150, y=240)

f_name_box=Entry(window,width=20)

####################################################################################################################
#mybutton.grid(row=2, column=2)
Label(window, text='teachers information', bg='#D3D3D3').place(x= 20, y=310)

# e_1= Entry(window, width= 50, bg= '#D3D3D3',borderwidth= '5' )

# e_1.insert(0, 'enter teacher info')
# e_1.place(x= 150, y= 70)


emptyLabel= Label(window, text='')
#emptyLabel.grid(row=2, column= 2)


def myClick_1():
    win3()    
    myLabel= Label (window, text= 'submiting', bg='#D3D3D3')
    myLabel.place(x=350, y=600)
mybutton=Button (window, text='Browse', width=70, command= myClick_1, bg='#D3D3D3', fg='#000000')
mybutton.place(x= 150, y=310)

f_name_box=Entry(window,width=20)
################################################################################################################3
Label(window, text='information on rooms', bg='#D3D3D3'). place(x=20, y= 380)
# e_2= Entry(window, width= 50, bg= '#D3D3D3',borderwidth= '5' )
# e_2.insert(0, 'enter room info')
# e_2.place(x= 150, y=130)

def myClick_2():

        win4()
myLabel= Label (window, text= 'submiting', bg='#D3D3D3')
myLabel.place(x=350, y=600)

mybutton=Button (window, text='browse',width=70, command= myClick_2, bg='#D3D3D3', fg='#000000')
mybutton.place(x=150, y=380)
f_name_box=Entry(window,width=20)
####################################################################################################################################3







window.mainloop()