from math import *
def kb():
    e1.delete(0,END)
    e1.insert(END,'MADE BY KB WITH LOVE                 ')
def sqr(a):
    return pow(a,2)
def enternumber0(event):
    e1.insert(END,0)
def enternumber1(event):
    e1.insert(END,1)
def enternumber2(event):
    e1.insert(END,2)
def enternumber3(event):
    e1.insert(END,3)
def enternumber4(event):
    e1.insert(END,4)
def enternumber5(event):
    e1.insert(END,5)
def enternumber6(event):
    e1.insert(END,6)
def enternumber7(event):
    e1.insert(END,7)
def enternumber8(event):
    e1.insert(END,8)
def enternumber9(event):
    e1.insert(END,9)
def enterplus(event):
    e1.insert(END,'+')
def enterper(event):
    e1.insert(END,'%')
def enterdiff(event):
    e1.insert(END,'-')
def entermulti(event):
    e1.insert(END,'*')
def enterdiv(event):
    e1.insert(END,'/')
def enterdecimal(event):
    e1.insert(END,'.')
def entersqrt(event):
    e1.insert(END,'sqrt(')
def entersquare(event):
    e1.insert(END,'sqr(')
def enterrp(event):
    e1.insert(END,')')
def enterlp(event):
    e1.insert(END,'(')
    
from tkinter import *
def evaluate():
    a=v.get()
    e1.delete(0,END)
    e1.insert(END,eval(a))
def dele():
    e1.delete(0,END)
def dele1():
    a=int(len(e1.get()))
    e1.delete(a-1)
windows=Tk()
windows.title('Calculator')
v=StringVar()
e1=Entry(windows,width=38,textvariable=v,justify='right')
e1.grid(row=0,columnspan=9)
b1=Button(windows,text=' 7 ',height=2,width=4)
b1.grid(row=1,column=1)
b1.bind("<Button-1>",enternumber7)
b2=Button(windows,text=' 8 ',height=2,width=4)
b2.grid(row=1,column=2)
b2.bind("<Button-1>",enternumber8)
b3=Button(windows,text=' 9 ',height=2,width=4)
b3.grid(row=1,column=3)
b3.bind("<Button-1>",enternumber9)
b4=Button(windows,text=' /  ',height=2,width=4)
b4.grid(row=1,column=4)
b4.bind("<Button-1>",enterdiv)
b5=Button(windows,text=' AC',height=2,width=4,command=dele)
b5.grid(row=1,column=5)
b6=Button(windows,text='  C  ',height=2,width=4,command=dele1)
b6.grid(row=1,column=6)
b7=Button(windows,text=' 4 ',height=2,width=4)
b7.grid(row=2,column=1)
b7.bind("<Button-1>",enternumber4)
b8=Button(windows,text=' 5 ',height=2,width=4)
b8.grid(row=2,column=2)
b8.bind("<Button-1>",enternumber5)
b9=Button(windows,text=' 6 ',height=2,width=4)
b9.grid(row=2,column=3)
b9.bind("<Button-1>",enternumber6)
b10=Button(windows,text='  * ',height=2,width=4)
b10.grid(row=2,column=4)
b10.bind("<Button-1>",entermulti)
b11=Button(windows,text='  (   ',height=2,width=4)
b11.grid(row=2,column=5)
b11.bind("<Button-1>",enterlp)
b12=Button(windows,text='   )  ',height=2,width=4)
b12.grid(row=2,column=6)
b12.bind("<Button-1>",enterrp)
b13=Button(windows,text=' 1 ',height=2,width=4)
b13.grid(row=3,column=1)
b13.bind("<Button-1>",enternumber1)
b14=Button(windows,text=' 2 ',height=2,width=4)
b14.grid(row=3,column=2)
b14.bind("<Button-1>",enternumber2)
b15=Button(windows,text=' 3 ',height=2,width=4)
b15.grid(row=3,column=3)
b15.bind("<Button-1>",enternumber3)
b16=Button(windows,text='  - ',height=2,width=4)
b16.grid(row=3,column=4)
b16.bind("<Button-1>",enterdiff)
b17=Button(windows,text='  R  ',height=2,width=4)
b17.grid(row=3,column=5)
b17.bind("<Button-1>",entersqrt)
b18=Button(windows,text='  xx ',height=2,width=4)
b18.grid(row=3,column=6)
b18.bind("<Button-1>",entersquare)
b19=Button(windows,text=' 0 ',height=2,width=4)
b19.grid(row=4,column=1)
b19.bind("<Button-1>",enternumber0)
b20=Button(windows,text=' .  ',height=2,width=4)
b20.grid(row=4,column=2)
b20.bind("<Button-1>",enterdecimal)
b21=Button(windows,text=' %',height=2,width=4)
b21.bind("<Button-1>",enterper)
b21.grid(row=4,column=3)
b22=Button(windows,text=' + ',height=2,width=4)
b22.grid(row=4,column=4)
b22.bind("<Button-1>",enterplus)
b23=Button(windows,text='  =  ',height=2,width=10,command=evaluate)
b23.grid(row=4,column=5,columnspan=2)
i=PhotoImage(file='click_here_icon.png')
b24=Button(windows,image=i,height=60,width=150,command=kb)
b24.grid(row=5,column=1,columnspan=6)

windows.mainloop()
