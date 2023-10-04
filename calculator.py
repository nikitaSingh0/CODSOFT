from tkinter import *

num1=num2=operator=None

def get_digit(digit):
    current = result['text']
    new = current + str(digit)
    result.config(text=new)

def clear_button():
    result.config(text="")

def get_operator(op):
    global num1,operator

    num1 = (int)(result['text'])   
    operator=op
    result.config(text=str(num1)+operator)

def get_result():
    global num1,num2,operator

    num2 = int(result['text'].split(operator)[1])

    if operator == '+':
        result.config(text = str(num1+num2))
    elif operator == '-':
        result.config(text = str(num1-num2))
    elif operator == '*':
        result.config(text = str(num1*num2))  
    elif operator == '/':
        if num2 == 0:
            result.config(text='Error')
        else:
            result.config(text = str(round(num1/num2,5)))
    else:
        result.config(text='Error')        



# Creates the main application window and assigns it to the root variable.
root=Tk()
root.title("Simple Calculator")
root.geometry("300x400")

root.resizable(0,0)

root.configure(background="black")

result=Label(root,text="",bg="black",fg="white")
result.grid(row=0,column=0,columnspan=500,pady=(50,25),sticky='e')
result.config(font=('verdana',27))


# first row
seven7=Button(root,text='7',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_digit(7))
seven7.grid(row=1,column=0)
seven7.config(font=('verdana',15))

eight8=Button(root,text='8',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_digit(8))
eight8.grid(row=1,column=1)
eight8.config(font=('verdana',15))

nine9=Button(root,text='9',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_digit(9))
nine9.grid(row=1,column=2)
nine9.config(font=('verdana',15))

add=Button(root,text='+',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_operator('+'))
add.grid(row=1,column=3)
add.config(font=('verdana',15))

# second row
four4=Button(root,text='4',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_digit(4))
four4.grid(row=2,column=0)
four4.config(font=('verdana',15))

five5=Button(root,text='5',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_digit(5))
five5.grid(row=2,column=1)
five5.config(font=('verdana',15))

six6=Button(root,text='6',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_digit(6))
six6.grid(row=2,column=2)
six6.config(font=('verdana',15))

sub=Button(root,text='-',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_operator('-'))
sub.grid(row=2,column=3)
sub.config(font=('verdana',15))

# third row
one1=Button(root,text='1',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_digit(1))
one1.grid(row=3,column=0)
one1.config(font=('verdana',15))

two2=Button(root,text='2',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_digit(2))
two2.grid(row=3,column=1)
two2.config(font=('verdana',15))

three3=Button(root,text='3',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_digit(3))
three3.grid(row=3,column=2)
three3.config(font=('verdana',15))

mul=Button(root,text='*',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_operator('*'))
mul.grid(row=3,column=3)
mul.config(font=('verdana',15))
# fourth row
clear=Button(root,text='C',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :clear_button())
clear.grid(row=4,column=0)
clear.config(font=('verdana',15))

zero=Button(root,text='0',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_digit(0))
zero.grid(row=4,column=1)
zero.config(font=('verdana',15))

equals=Button(root,text='=',bg='mistyrose3',fg='black',width=5,height=2,command=get_result)
equals.grid(row=4,column=2)
equals.config(font=('verdana',15))

div=Button(root,text='/',bg='mistyrose3',fg='black',width=5,height=2,command=lambda :get_operator('/'))
div.grid(row=4,column=3)
div.config(font=('verdana',15))

#  Starts the main event loop of the Tkinter application
root.mainloop()
