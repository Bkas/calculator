from tkinter import *

#CREATING ROOT WINDOW
root = Tk()

#GIVING SIZE AND NAME CALCULATOR
root.geometry("312x324")
root.resizable(0, 0)
root.title("My Calculator")
root.iconbitmap('calcus.ico')


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

input_text = StringVar()

frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
frame.pack(side=TOP)


entry = Entry(frame, font=('arial', 18, 'bold'),fg='black', textvariable=input_text, width=50, bg="azure", bd=0, justify=RIGHT)
entry.grid(row=0, column=0)
entry.pack(ipady=10)

btn_frame = Frame(root, width=312, height=272.5, bg="grey")
btn_frame.pack()

#DEFINING BUTTONS AND PLACING THEM ON THE SCREEN ACCORDING TO MY COHICE BY USING GRID
btn_clear = Button(btn_frame, text="C", fg="black", width=32, height=3, bd=0, bg="silver", cursor="hand2", command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

btn_divide = Button(btn_frame, text="/", fg="white", width=10, height=3, bd=0, bg="orange", cursor="hand2",
                command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

btn_seven = Button(btn_frame, text="7", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

btn_eight = Button(btn_frame, text="8", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

btn_nine = Button(btn_frame, text="9", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

btn_multiply = Button(btn_frame, text="*", fg="white", width=10, height=3, bd=0, bg="orange", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

btn_four = Button(btn_frame, text="4", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

btn_five = Button(btn_frame, text="5", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

btn_six = Button(btn_frame, text="6", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

btn_minus = Button(btn_frame, text="-", fg="white", width=10, height=3, bd=0, bg="orange", cursor="hand2",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)


btn_one = Button(btn_frame, text="1", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

btn_two = Button(btn_frame, text="2", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

btn_three = Button(btn_frame, text="3", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

btn_plus = Button(btn_frame, text="+", fg="white", width=10, height=3, bd=0, bg="orange", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)


btn_zero = Button(btn_frame, text="0", fg="black", width=21, height=3, bd=0, bg="white", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

btn_point = Button(btn_frame, text=".", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

btn_equals = Button(btn_frame, text="=", fg="black", width=10, height=3, bd=0, bg="ivory", cursor="hand2",
                command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

#LOOPS THE PROGRAM UNTIL USER USES
root.mainloop()