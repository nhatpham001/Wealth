from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Wealth")
#labels
Header = Label(root, text = "Let's invest!")
Header.grid(row =0, column = 0)


label1 = Label(root, text = "how many years do you want to invest in?")
label1.grid(row = 1, column = 0 )

label2 = Label(root, text = "how much do you want to have after those years?")
label2.grid(row = 5, column = 0 )

label3 = Label(root, text = "the stock market grows 7 percent annually")
label3.grid(row = 8, column = 0 )

#input fields
years = Entry(root, width = 30, borderwidth = 5)
years.grid(row = 3, column = 0, )
years.insert(0, "Enter Years ")

total_money = Entry(root, width =30, borderwidth = 5)
total_money.grid(row = 6, column = 0, )
total_money.insert(0, "Enter Amount ")

rate = Entry(root, width =30, borderwidth = 5)
rate.grid(row = 9, column = 0, )
rate.insert(0, ".07")

#calculate compound interest
def calculate():
    r = float(rate.get())
    yrs = int(years.get())
    
    totalmoney = int(total_money.get())
    oneyear  = ((totalmoney * r)/(((1+r)**yrs)-1))
    result  = ((totalmoney * r)/(((1+r)**yrs)-1))/360

    label = Label(root, text  = "Each day, you'll have to save $" + str(round(result, 2)))
    label.grid(row =16, column = 0)
    return round(oneyear, 0)
    
#graph data
def graph():
    #inputs
    r = float(rate.get())
    yrs = int(years.get())

    #range on x and y
    xlist = np.arange(0, int(years.get()), .5)
    ylist = calculate()*(((1+r)**xlist)-1)/r

    plt.figure(num = 0, dpi = 120 )
    plt.plot(xlist,ylist)
    plt.xlabel('Years')
    plt.ylabel('Total Return (USD)')
    plt.title('Investment Graph (USD) by Years')
    plt.show()

#start button
Start = Button(root, text = "Start Calculate", command= calculate)
Start.grid(row = 15, column =  0)

#graph button
graph = Button(root, text = "Graph!", command= graph)
graph.grid(row = 17, column = 0)

root.mainloop()