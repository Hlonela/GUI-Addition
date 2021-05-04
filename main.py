#import the 'tkinter module
from tkinter import*
root = Tk() # Blank window
root.geometry("600x600")
#create the title for the window
root.title("Adding two numbers")


#creating label widgets
label1 = Label(root, text = "Please enter first number:");
label2 = Label (root, text = "Please enter second number:")
label3 = Label(root, text="Your answer:")
#Positioning the input & output fields
first_num = Entry (root )
second_num = Entry(root)
answer = Entry(root)

#functions
def button_clear ():
    #CLEARING THE INPUT FIELDS
    answer.delete(0, END)
    first_num.delete(0,END)
    second_num.delete(0,END)

def button_add ():
    # SUM OF THE TWO NUMBERS
    digit_1 = first_num.get();
    digit_2 = second_num.get();
    first_add = int(digit_1)
    second_add = int (digit_2)
    answer.insert(0, first_add + second_add)

def button_exit ():
    # EXITING
    import sys
    sys.exit()
    # exits the program
    #sys.exit("Age less than 18")

# Buttons
button_add = Button(root, text="Add", width=10, command=button_add)
button_clear = Button(root, text="Clear", width=10, command=button_clear)
button_exit = Button(root, text="Exit", width=10, command=button_exit)

#display
label1.grid(row=0, column=0, padx=10, pady=10 )
label2.grid(row=1,column=0, padx=10, pady=10)
label3.grid(row=2,column=0, padx=10, pady=10)
first_num.grid(row=0,column=1, padx=10, pady=10)
second_num.grid(row=1,column=1, padx=10, pady=10)
answer.grid(row=2,column=1, padx=10, pady=10)
button_add.grid(row=3,column=1, padx=10, pady=10)
button_clear.grid(row=3,column=2, padx=10, pady=10)
button_exit.grid(row=3,column=3, padx=10, pady=10)


root.mainloop();