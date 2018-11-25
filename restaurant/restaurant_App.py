from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width = 1600,height = 50, bg = "powder blue", relief = SUNKEN)
Tops.pack(side=TOP)

Frame1 = Frame(root, width = 800,height = 700,relief = SUNKEN)
Frame1.pack(side=LEFT)

Frame2 = Frame(root, width = 300,height = 700,relief = SUNKEN)
Frame2.pack(side=RIGHT)
# ========================Time===========================================
localtime = time.asctime(time.localtime(time.time()))   # Datetime Function
# =========================Info==========================================
lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Management System",
                fg="steel Blue",bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblDatetime = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="steel Blue",bd=10,
                anchor='w')
lblDatetime.grid(row=1,column=0)
# =========================Calculator====================================
def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    x = random.randint(10908, 500876)
    randomFef = str(x)
    rand.set(randomFef)

    CoF = float(Fries.get())
    CoD = float(Drinks.get())
    CoFilet = float(Filet.get())
    CoBurger = float(Burger.get())
    CoChicken_Burger = float(Chicken_Burger.get())
    CoCheese_Burger = float(Cheese_Burger.get())

    CostofFries = CoF * 2.50
    CostofDrinks = CoD * 3.00
    CostofFilet = CoFilet * 5.99
    CostofBurger = CoBurger * 5.87
    CostofChicken_Burger = CoChicken_Burger * 5.99
    CostofCheese_Burger = CoCheese_Burger * 5.49

    CostofMeal = '$ ' + str('%.2f' % (CostofFries + CostofDrinks + CostofFilet
                                    + CostofBurger + CostofChicken_Burger + CostofCheese_Burger))

    PayTax = ((CostofFries + CostofDrinks + CostofFilet
                                    + CostofBurger + CostofChicken_Burger + CostofCheese_Burger)*0.2)

    TotalCost = (CostofFries + CostofDrinks + CostofFilet
                                    + CostofBurger + CostofChicken_Burger + CostofCheese_Burger)


    Ser_Charge = ((CostofFries + CostofDrinks + CostofFilet
                                    + CostofBurger + CostofChicken_Burger + CostofCheese_Burger)/99)


    Service = '$ ' + str('%.2f' % Ser_Charge)

    OverAllCost = '$ ' + str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = '$ ' + str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")


txtDisplay = Entry(Frame2, font=('arial', 20, 'bold'), textvariable = text_Input, bd=30,
                   insertwidth=4, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)
# ------------------------------------------------------------------------------------------------------
btn7=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=2,column=0)
btn8=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=2,column=1)
btn9=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='+', bg='powder blue', command=lambda: btnClick('+')).grid(row=2,column=3)
# ---------------------------------------------------------------------------------------------------
btn4=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=3,column=0)
btn5=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='5', bg='powder blue', command=lambda: btnClick(5)).grid(row=3,column=1)
btn6=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='6', bg='powder blue', command=lambda: btnClick(6)).grid(row=3,column=2)

Subtraction=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='-', bg='powder blue', command=lambda: btnClick('-')).grid(row=3,column=3)
# ---------------------------------------------------------------------------------------------------
btn1=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=4,column=0)
btn2=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=4,column=1)
btn3=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=4,column=2)

Multiply=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='*', bg='powder blue', command=lambda: btnClick('*')).grid(row=4,column=3)
# ---------------------------------------------------------------------------------------------------
btn0=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='0', bg='powder blue', command=lambda: btnClick(0)).grid(row=5,column=0)
btnClear=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='C', bg='powder blue',command=lambda:btnClearDisplay()).grid(row=5,column=1)
btnEquals=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='=', bg='powder blue',command=lambda:btnEqualsInput()).grid(row=5,column=2)

Division=Button(Frame2,padx=16,pady=16,bd=8, fg='black', font=('arial',20, 'bold'),
            text='/', bg='powder blue', command=lambda: btnClick('/')).grid(row=5,column=3)
# -----------------------------------Restaurant Info 1----------------------------------------------------------------


rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()


lblReference = Label(Frame1, font=('arial', 16, 'bold'), text = 'Reference', bd=16, anchor='w')
lblReference.grid(row=0, column=0)
txtReference = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = rand, bd=10, insertwidth = 4,
                     bg='powder blue', justify = 'right')
txtReference.grid(row=0, column=1)

lblFries = Label(Frame1, font=('arial', 16, 'bold'), text = 'Large Fries', bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = Fries, bd=10, insertwidth = 4,
                     bg='powder blue', justify = 'right')
txtFries.grid(row=1, column=1)

lblBurger = Label(Frame1, font=('arial', 16, 'bold'), text = 'Burger Meal', bd=16, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = Burger, bd=10, insertwidth = 4,
                     bg='powder blue', justify = 'right')
txtBurger.grid(row=2, column=1)

lblFilet = Label(Frame1, font=('arial', 16, 'bold'), text = 'Filet_o_Meal', bd=16, anchor='w')
lblFilet.grid(row=3, column=0)
txtFilet = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = Filet, bd=10, insertwidth = 4,
                     bg='powder blue', justify = 'right')
txtFilet.grid(row=3, column=1)

lblChicken = Label(Frame1, font=('arial', 16, 'bold'), text = 'Chicken Meal', bd=16, anchor='w')
lblChicken.grid(row=4, column=0)
txtChicken = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = Chicken_Burger, bd=10, insertwidth = 4,
                     bg='powder blue', justify = 'right')
txtChicken.grid(row=4, column=1)

lblCheese = Label(Frame1, font=('arial', 16, 'bold'), text = 'Cheese Meal', bd=16, anchor='w')
lblCheese.grid(row=5, column=0)
txtCheese = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = Cheese_Burger, bd=10, insertwidth = 4,
                     bg='powder blue', justify = 'right')
txtCheese.grid(row=5, column=1)

# -----------------------------------Restaurant Info 2----------------------------------------------------------------
lblDrinks = Label(Frame1, font=('arial', 16, 'bold'), text = 'Drinks', bd=16, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = Drinks, bd=10, insertwidth = 4,
                     bg='#ffffff', justify = 'right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(Frame1, font=('arial', 16, 'bold'), text = 'Cost of Meal', bd=16, anchor='w')
lblCost.grid(row=1, column=2)
txtCost = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = Cost, bd=10, insertwidth = 4,
                     bg='#ffffff', justify = 'right')
txtCost.grid(row=1, column=3)

lblService = Label(Frame1, font=('arial', 16, 'bold'), text = 'Service Charge', bd=16, anchor='w')
lblService.grid(row=2, column=2)
txtService = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = Service_Charge, bd=10, insertwidth = 4,
                     bg='#ffffff', justify = 'right')
txtService.grid(row=2, column=3)

lblStateTax = Label(Frame1, font=('arial', 16, 'bold'), text = 'State Tax', bd=16, anchor='w')
lblStateTax.grid(row=3, column=2)
txtStateTax = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = Tax, bd=10, insertwidth = 4,
                     bg='#ffffff', justify = 'right')
txtStateTax.grid(row=3, column=3)

lblSubTotal = Label(Frame1, font=('arial', 16, 'bold'), text = 'Sub Total', bd=16, anchor='w')
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = SubTotal, bd=10, insertwidth = 4,
                     bg='#ffffff', justify = 'right')
txtSubTotal.grid(row=4, column=3)

lblTotal = Label(Frame1, font=('arial', 16, 'bold'), text = 'Total Cost', bd=16, anchor='w')
lblTotal.grid(row=5, column=2)
txtTotal = Entry(Frame1, font=('arial', 16, 'bold'), textvariable = Total, bd=10, insertwidth = 4,
                     bg='#ffffff', justify = 'right')
txtTotal.grid(row=5, column=3)
# ====================================Buttons========================================================
btnTotal = Button(Frame1,padx = 16, pady = 8, bd = 16, fg = 'black',font=('arial', 16, 'bold'), width=10,
                  text = 'Total',bg='powder blue',command=lambda: Ref()).grid(row=7, column=1)

btnReset = Button(Frame1,padx = 16, pady = 8, bd = 16, fg = 'black',font=('arial', 16, 'bold'), width=10,
                  text = 'Reset',bg='powder blue',command=lambda: Reset()).grid(row=7, column=2)

btnExit = Button(Frame1,padx = 16, pady = 8, bd = 16, fg = 'black',font=('arial', 16, 'bold'), width=10,
                  text = 'Exit',bg='powder blue',command=lambda: qExit()).grid(row=7, column=3)


root.mainloop()

