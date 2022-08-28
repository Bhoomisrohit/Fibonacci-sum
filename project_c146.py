from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")
enter_no=Entry(root)
label_1 = Label(root, text="Fibonacci Series:  ")
label_2 = Label(root,text="Fibonacci Series:  ")


def Fibonacci():
    input_no=int(enter_no.get())
    first_no = 0
    second_no = 1
    sum = 0
    sum2=0
    counter = 1
    while (counter <= input_no):
        label_1["text"] += str(sum) + " "
        label_2["text"]="Fibonacci sum : " + str(sum2)
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2=sum2+sum
enter_no.pack() 
btn = Button(root, text="Show Fibonacci Series", command=Fibonacci,fg="white",bg="dark blue")

btn.pack()
label_1.pack()
label_2.pack()
root.mainloop()