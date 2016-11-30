from tkinter import *

comic_list = []

class Comic:
    def __init__(self, make, quantity):
        self.make = make
        self.quantity = quantity
        comic_list.append(self)

    def decomission(self):
        if self.quantity >= 1:
            self.quantity -= 1
            return True
        else:
            return False
        
    def restock(self, quantity):
        self.quantity += quantity


def remove_comic():

    for comic in comic_list:
        if comic.make == comic_selected.get():
            if comic.decomission() == True:
                removed_comic_feedback.set("1 " + comic_selected.get() + " removed.")
            else:
                removed_comic_feedback.set("All " + comic_selected.get() + " removed.")

    display_stock_details()

    
def add_comics():
    for comic in comic_list:
        if restock_comic.get() == comic.make:
            comic.restock(restock_num.get())
    display_stock_details()

        
def display_stock_details():
    comic_details = ""

    for comic in comic_list:
        comic_details += comic.make + " : " + str(comic.quantity) + " in stock." + "\n"

    stock_details.set(comic_details)

def comic_makes_list():
    comic_makes=[]

    for comic in comic_list:
        comic_makes.append(comic.make)

    return comic_makes

Comic("Super Dude", 8)
Comic("Lizard Man", 12)
Comic("Water Woman", 3)

root = Tk()
root.title("Comics stock control")
root.geometry("675x170+200+200")
root.configure(background = "#483d8b")


#Left Frame - Sell Comic
left_frame = Frame(root)
top_label = Label(left_frame, text = "Sell Comic", font=("Helvetica", "24"), fg = "#f8f8ff",  bg = "#483d8b").pack(side = TOP, ipadx = 10, ipady = 10)
left_frame.configure(bg = "#483d8b")

comic_makes_l = comic_makes_list()
comic_selected = StringVar()
comic_selected.set(comic_makes_l[0])
configure_OptionMenu = OptionMenu(left_frame, comic_selected, *comic_makes_l)
configure_OptionMenu.configure(bg = "#9370db", activebackground = "#dda0dd", fg = "#f8f8ff", activeforeground = "#f8f8ff", highlightthickness=0)
configure_OptionMenu["menu"].config(bg="#9370db", activebackground = "#dda0dd", fg = "#f8f8ff")
configure_OptionMenu.pack(pady=4)

Button(left_frame, text = "Remove Comic", activebackground = "#dda0dd", activeforeground = "#f8f8ff", fg = "#f8f8ff", width = 20, command = remove_comic, bg = "#9370db").pack(side = TOP)
left_frame.pack(side = LEFT, ipadx = 10, ipady = 15)

removed_comic_feedback = StringVar()
Label(left_frame, textvariable = removed_comic_feedback, width = 20, bg = "#483d8b", fg = "#f8f8ff").pack(side = TOP, ipadx = 10, ipady = 10)


#Middle Frame - Comic Stock
middle_frame = Frame(root)
Label(middle_frame, text = "Comic Stock", font = ("Helvetica", "24"), bg = "#483d8b", fg = "#f8f8ff").pack(side = TOP, ipadx = 10, ipady = 10)
middle_frame.configure(background = "#483d8b")

stock_details = StringVar()
Label(middle_frame, textvariable = stock_details, bg = "#483d8b", fg = "#f8f8ff").pack(side = TOP)

middle_frame.pack(side = LEFT, ipadx = 10, ipady = 30)


#Right Frame - Restock Comic
right_frame = Frame(root)
restock_comic = Label(right_frame, text = "Restock Comic", fg = "#f8f8ff", font=("Helvetica", "24"), bg = "#483d8b").pack(side = TOP, ipadx = 10, ipady = 10)
right_frame.configure(background = "#483d8b")

restock_comic = StringVar()
restock_comic.set(comic_makes_l[0])
configure_OptionMenu = OptionMenu(right_frame, restock_comic, *comic_makes_l)
configure_OptionMenu.configure(bg = "#9370db", activebackground = "#dda0dd", fg = "#f8f8ff", activeforeground = "#f8f8ff", highlightthickness=0)
configure_OptionMenu.pack(pady=4)
configure_OptionMenu["menu"].config(bg="#9370db", activebackground = "#dda0dd", fg = "#f8f8ff")
configure_OptionMenu.pack() 

restock_num = IntVar()
Entry(right_frame, textvariable = restock_num, width = 10, bg = "#9370db", fg = "#f8f8ff", selectbackground = "#483d8b").pack(side=TOP, pady=3)

Button(right_frame, text="Add Comics", activebackground = "#dda0dd", command = add_comics, fg = "#f8f8ff", bg = "#9370db", activeforeground = "#f8f8ff").pack(side=TOP, ipadx = 5, pady=3)

restock_feedback = StringVar()
Label(right_frame, textvariable = restock_feedback, bg = "#483d8b").pack(side = TOP, ipadx = 10, ipady =10)
right_frame.pack(side = LEFT, ipadx=10, ipady=5)

display_stock_details()
root.mainloop()
