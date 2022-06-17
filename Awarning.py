from tkinter import *
import tkinter.font as font


def warn2():
    warn2= Toplevel
    warn2.configure(bg= 'lime')
    warn2.title(          'notice!!!'.upper())
    warn2.geometry('250x130')


    accfont= font.Font(family='helvetica', size=50)
    Label(warn2, text='!', font=accfont, bg= '#F0E68C', fg='blue').place(x=115, y=4)


    accfont2=font.Font(family= 'helvetica', size= 10)
    Label(warn2, text='you entered a wrong pasword !!!', font=accfont2, bg='#F0E68C', fg='green').place(x=10,y=100)

    

