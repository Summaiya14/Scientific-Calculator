from tkinter import*
from math import*
from fractions import Fraction 

win=Tk()
win.title('Scientific Calculator')
win.geometry('917x224')
win.configure(background='Black')


π=pi
def fraction():
    x=text.get()
    x=str(Fraction(x))
    text.set(x)
def btnclick(num):
    global x
    x=x+str(num)
    text.set(x)

def clear():
    global x
    x=''
    text.set(0)

def equals():
    global x
    try:
        x=str(eval(text.get()))
        text.set(x)
    except ZeroDivisionError:
        text.set('Math Error')
    except SyntaxError:
        text.set('Syntax Error')
    except ValueError:
        text.set('invalid')


                
def root():
    global x
    x=float(text.get())
    x=str(x**(.5))
    text.set(x)


    
   
def delete():
    global x
    x=text.get()
    x=x[:-1]
    text.set(x)

def square():
    global x
    x=float(text.get())
    x=str(x**2)
    text.set(x)

def cube():
    global x
    x=float(text.get())
    x=str(x**3)
    text.set(x)

def cuberoot():
    global x
    x=float(text.get())
    x=(x**(1/3))
    x=str(format(x,'.6f'))
    text.set(x)

def inverse():
    global x
    x=float(text.get())
    x=(1/x)
    x=str(format(x,'.6f'))
    text.set(x)

def percentage():
    global x
    x=float(text.get())
    x=x/100
    x=str(format(x,'.6f'))
    text.set(x)


def dectobin():
    global x
    x=int(text.get())
    b=''
    while x>1:
        b = b+str(x%2)
        x = x//2
    b = b+"1"
    b = b[::-1]
    text.set(b)

def dectooctal():
    global x
    x=int(text.get())
    b=''
    while x>1:
        b = b+str(x%8)
        x = x//8
    b = b[::-1]
    text.set(b)

def dectooctal():
    global x
    x=int(text.get())
    b=''
    while x>1:
        b = b+str(x%8)
        x = x//8
    b = b[::-1]
    text.set(b)

def bintooct():
    global x
    x=text.get()
    x=x[::-1]
    a = 0
    for i in range(len(x)):
        a = a + (int(x[i])*(2**i))
    b=''
    while a>1:
        b = b+str(a%8)
        a = a//8
    b = b[::-1]
    text.set(b)
    
def bintodec():
    global x
    x=text.get()
    x=x[::-1]
    a = 0
    for i in range(len(x)):
        a = a + (int(x[i])*(2**i))
    text.set(str(a))
    
def nPr(a, b):
    global x
    a = int(a)
    b = int(b)
    return factorial(a)/factorial(a-b) 

def nCr(a, b):
    global x
    a = int(a)
    b = int(b)
    return nPr(a,b)/factorial(b)


def quad(a,b,c):
    global x
    a=int(a)
    b=int(b)
    c=int(c)
    x1=(-b+(b**2-(4*a*c))**0.5)/(2*a)

    x2=(-b-(b**2-(4*a*c))**0.5)/(2*a)

    return (x1,x2)

text=StringVar()
text.set(0)
x=''

entry=Entry(win,font=('aerial,20'),width=101,justify='right',text=text)
entry.grid(columnspan=15)

but1=Button(win,padx=12,text='7',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(7))
but1.grid(row=1,column=0)
but2=Button(win,padx=12,text='8',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(8))
but2.grid(row=1,column=1)
but3=Button(win,padx=12,text='9',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(9))
but3.grid(row=1,column=2)
but4=Button(win,padx=12,text='4',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(4))
but4.grid(row=2,column=0)
but5=Button(win,padx=12,text='5',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(5))
but5.grid(row=2,column=1)
but6=Button(win,padx=12,text='6',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(6))
but6.grid(row=2,column=2)
but7=Button(win,padx=12,text='1',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(1))
but7.grid(row=3,column=0)
but8=Button(win,padx=12,text='2',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(2))
but8.grid(row=3,column=1)
but9=Button(win,padx=12,text='3',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(3))
but9.grid(row=3,column=2)
but10=Button(win,padx=12,text='0',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(0))
but10.grid(row=4,column=0)
but11=Button(win,padx=12,text='x',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('*'))
but11.grid(row=3,column=4)
but12=Button(win,padx=12,text='+',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('+'))
but12.grid(row=4,column=4)
but13=Button(win,padx=12,text='-',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('-'))
but13.grid(row=4,column=5)
but14=Button(win,padx=12,text='/',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('/'))
but14.grid(row=3,column=5)
but15=Button(win,padx=12,text='=',justify='center',width=2,height=13,fg='black',bg='silver',command=lambda:equals())
but15.grid(column=3,row=1, rowspan=5)
but16=Button(win,padx=12,text='(',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick('('))
but16.grid(row=5,column=0)
but17=Button(win,padx=12,text=')',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(')'))
but17.grid(row=5,column=1)
but18=Button(win,padx=12,text='.',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick('.'))
but18.grid(row=4,column=1)
but19=Button(win,padx=12,text=',',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick(','))
but19.grid(row=5,column=2)
but20=Button(win,padx=12,text='Ac',height=2,width=5,fg='white',bg='red',command=lambda:clear())
but20.grid(row=1,column=4)
but21=Button(win,padx=12,text='del',height=2,width=5,fg='white',bg='red',command=lambda:delete())
but21.grid(row=1,column=5)
but22=Button(win,padx=12,text='exponent',height=2,width=5,fg='black',bg='silver',command=lambda:btnclick('*10**'))
but22.grid(row=4,column=2)
but23=Button(win,padx=12,text='log',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('log('))
but23.grid(row=2,column=4)
but24=Button(win,padx=12,text='ln',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('log10'))
but24.grid(row=2,column=5)
but25=Button(win,padx=12,text='π',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('π'))
but25.grid(row=5,column=4)
but26=Button(win,padx=12,text='e',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('e'))
but26.grid(row=5,column=5)
but27=Button(win,padx=12,text='√',height=2,width=5,fg='white',bg='dark blue',command=lambda:root())
but27.grid(row=1,column=6)
but28=Button(win,padx=12,text='x^2',height=2,width=5,fg='white',bg='dark blue',command=lambda:square())
but28.grid(row=2,column=6)
but29=Button(win,padx=12,text='x^3',height=2,width=5,fg='white',bg='dark blue',command=lambda:cube())
but29.grid(row=3,column=6)
but30=Button(win,padx=12,text='3√',height=2,width=5,fg='white',bg='dark blue',command=lambda:cuberoot())
but30.grid(row=4,column=6)
but31=Button(win,padx=12,text='%',height=2,width=5,fg='white',bg='dark blue',command=lambda:percentage())
but31.grid(row=5,column=6)
but32=Button(win,padx=12,text='x!',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('factorial('))
but32.grid(row=5,column=7)
but33=Button(win,padx=12,text='nPr',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('nPr('))
but33.grid(row=1,column=7)
but34=Button(win,padx=12,text='nCr',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('nCr('))
but34.grid(row=2,column=7)
but35=Button(win,padx=12,text='x^-1',height=2,width=5,fg='white',bg='dark blue',command=lambda:inverse())
but35.grid(row=3,column=7)
but36=Button(win,padx=12,text='x^',height=2,width=5,fg='white',bg='dark blue',command=lambda:btnclick('**'))
but36.grid(row=4,column=7)
but37=Button(win,padx=12,text='dectobin',height=2,width=5,fg='black',bg='gray',command=lambda:dectobin())
but37.grid(row=5,column=8)
but38=Button(win,padx=12,text='bintodec',height=2,width=5,fg='black',bg='gray',command=lambda:bintodec())
but38.grid(row=1,column=8)
but39=Button(win,padx=12,text='bintooct',height=2,width=5,fg='black',bg='gray',command=lambda:bintooct())
but39.grid(row=2,column=8)
but40=Button(win,padx=12,text='dectooct',height=2,width=5,fg='black',bg='gray',command=lambda:dectooctal())
but40.grid(row=3,column=8)
but41=Button(win,padx=12,text='dectofra',height=2,width=5,fg='black',bg='gray',command=lambda:fraction())
but41.grid(row=4,column=8)
but42=Button(win,padx=12,text='sin deg',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('sin(radians('))
but42.grid(row=2,column=9)
but43=Button(win,padx=12,text='cos deg',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('cos(radians('))
but43.grid(row=2,column=10)
but44=Button(win,padx=12,text='tan deg',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('tan(radians('))
but44.grid(row=2,column=11)
but45=Button(win,padx=12,text='cosec deg',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('1/sin(radians('))
but45.grid(row=2,column=12)
but46=Button(win,padx=12,text='sec deg',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('1/cos(radians('))
but46.grid(row=5,column=12)
but47=Button(win,padx=12,text='cot deg',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('1/tan(radians('))
but47.grid(row=3,column=13)
but48=Button(win,padx=12,text='sin rad',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('sin('))
but48.grid(row=1,column=9)
but49=Button(win,padx=12,text='cos rad',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('cos('))
but49.grid(row=1,column=10)
but50=Button(win,padx=12,text='tan rad',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('tan('))
but50.grid(row=1,column=11)
but51=Button(win,padx=12,text='cosec rad',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('1/sin('))
but51.grid(row=1,column=12)
but52=Button(win,padx=12,text='sec rad',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('1/cos('))
but52.grid(row=4,column=12)
but53=Button(win,padx=12,text='cot rad',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('1/tan('))
but53.grid(row=2,column=13)
but54=Button(win,padx=12,text='asin',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('asin('))
but54.grid(row=3,column=9)
but55=Button(win,padx=12,text='acos',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('acos('))
but55.grid(row=3,column=10)
but56=Button(win,padx=12,text='atan',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('atan('))
but56.grid(row=3,column=11)
but57=Button(win,padx=12,text='sinh',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('sinh('))
but57.grid(row=4,column=9)
but58=Button(win,padx=12,text='cosh',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('cosh('))
but58.grid(row=4,column=10)
but59=Button(win,padx=12,text='tanh',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('tanh('))
but59.grid(row=4,column=11)
but60=Button(win,padx=12,text='cosech',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('cosech('))
but60.grid(row=3,column=12)
but61=Button(win,padx=12,text='sech',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('sech('))
but61.grid(row=1,column=13)
but62=Button(win,padx=12,text='coth',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('coth('))
but62.grid(row=4,column=13)
but63=Button(win,padx=12,text='asinh',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('asinh('))
but63.grid(row=5,column=9)
but64=Button(win,padx=12,text='acosh',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('acosh('))
but64.grid(row=5,column=10)
but65=Button(win,padx=12,text='atanh',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('atanh('))
but65.grid(row=5,column=11)
but66=Button(win,padx=12,text='quad',height=2,width=5,fg='white',bg='black',command=lambda:btnclick('quad('))
but66.grid(row=5,column=13)







win.mainloop()
