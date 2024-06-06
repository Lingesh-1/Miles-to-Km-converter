from tkinter import *


def conv():
    m=float(inp.get())
    km=round(m*1.60934)
    la3['text']=km

win=Tk()
win.title('Mile To KM Converter')
win.minsize(200,100)


inp=Entry(width=10)
inp.focus()
# inpg=inp.get()
inp.grid(column=2,row=0)

la1=Label(text="Miles")
la1.grid(column=3,row=0)

la2=Label(text="is equal to")
la2.grid(column=1,row=2)

la3=Label(text="0")
la3.grid(column=2,row=2)

la4=Label(text="KM")
la4.grid(column=3,row=2)


but=Button(text='CALCULATE',command=conv)
but.grid(column=2,row=3)

win.mainloop()
