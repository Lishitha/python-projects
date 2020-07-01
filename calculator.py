from tkinter import *

w = Tk()
w.geometry("180x200")
w.title("Calculator")
w.configure(bg="#e1d5e3")
eqn = StringVar()
exp = " "


#************text bar showing nmbr************
def input_num(num,eqn):
    #print("hiiiiiiiiiiii")
    global exp
    exp = exp +str(num)
    eqn.set(exp)


#************equation evaluate****************
def eval_eqn(eqn):
    global exp
    try:
        result = str(eval(exp))
        eqn.set(result)
    except ZeroDivisionError:
        print("cant divided by zero")
        exp = " "
        eqn.set("error")



#**************clear the screen***************
def clr_screen(eqn):
    global exp
    exp = " "
    eqn.set(" ")



# w.columnconfigure(0,weight=1)
# w.rowconfigure(0,weight=1)
# w.rowconfigure(1,weight=1)
#num = w.StringVar()
e = Entry(w,bd = 5,textvariable=eqn)
e.grid(row=0,columnspan=4)


b7 = Button(w, text="7", width=5, height=2, bg="#777378", command = lambda :input_num(7,eqn))
b8 = Button(w, text="8", width=5, height=2, bg="#777378",command = lambda :input_num(8,eqn))
b9 = Button(w, text="9", width=5, height=2, bg="#777378",command = lambda :input_num(9,eqn))
bmul = Button(w, text="*", width=5, height=2, bg="#777378",command = lambda :input_num("*",eqn))
b4 = Button(w, text="4", width=5, height=2, bg="#777378",command = lambda :input_num(4,eqn))
b5 = Button(w, text="5", width=5, height=2, bg="#777378",command = lambda :input_num(5,eqn))
b6 = Button(w, text="6", width=5, height=2, bg="#777378",command = lambda :input_num(6,eqn))
bdiv = Button(w, text="/", width=5, height=2, bg="#777378",command = lambda :input_num("/",eqn))
b1 = Button(w, text="1", width=5, height=2, bg="#777378",command = lambda :input_num(1,eqn))
b2 = Button(w, text="2", width=5, height=2, bg="#777378",command = lambda :input_num(2,eqn))
b3 = Button(w, text="3", width=5, height=2, bg="#777378",command = lambda :input_num(3,eqn))
b0 = Button(w, text="0", width=5, height=2, bg="#777378",command = lambda :input_num(0,eqn))
bplus = Button(w, text="+", width=5, height=2, bg="#777378",command = lambda :input_num("+",eqn))
bmin = Button(w, text="-", width=5, height=2, bg="#777378",command = lambda :input_num("-",eqn))
bclr = Button(w, text="C", width=5, height=2, bg="#777378",command = lambda :clr_screen(eqn))
beq = Button(w, text="=", width=5, height=2, bg="#777378",command = lambda :eval_eqn(eqn))


b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
bmul.grid(row=1,column=3)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
bdiv.grid(row=2,column=3)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b0.grid(row=3, column=3)
beq.grid(rowspan= 5,column=3)
bplus.grid(row=4,column=0)
bmin.grid(row=4,column=1)
bclr.grid(row=4,column=2)




w.mainloop()
