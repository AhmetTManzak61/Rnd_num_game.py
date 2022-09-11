from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.geometry("1000x1000")
root.title("Random number guessing game")

def selectDiff():
    global diff
    diff = AnswerEntry.get()
    diff = int(diff)
    messagebox.showinfo("Difficulty selected.")



def generateNum():
    global num, tries, points
    global diff
    tries = 0
    if diff == 1:
        num = random.randint(1,10)
    elif diff == 2:
        num = random.randint(1,50)
    elif diff == 3:
        num = random.randint(1,100)
    messagebox.showinfo("A number has been generated.")

def guessNumber():
    global num
    global tries
    global points
    user_resp = AnswerEntry.get()
    user_resp = int(user_resp)
    tries = tries + 1
    points = 100 - (tries-1) * 10
    if user_resp > num:
        ResultLabel1.config(text="Incorrect. Try guessing lower.", fg="Red")
    elif user_resp < num:
        ResultLabel1.config(text="Incorrect. Try guessing higher", fg="Red")
    else:
        ResultLabel1.config(text="You won! The number was {}".format(num), fg="Green")
        ResultLabel2.config(text="Number of attempts = {} ".format(tries), fg="Green")
        ResultLabel3.config(text="Points earned = {}".format(points), fg="Green")
        AnswerEntry.delete(0,"end")


Title = Label(root, text="Random Number Guessing Game", font=("Arial",30))
Title.pack()



MainFrame = Frame(root)
MainFrame.pack(pady=50)


SelectdiffLabel = Label(MainFrame, text="Select a difficulty. Enter the number in front of the difficulty setting.", font=("Arial",20))
SelectdiffLabel.pack()
numdiffLabel = Label(MainFrame, text = "1-Easy(1-10)  2-Medium(1-50)  3-Hard(1-100)", font=("Arial", 12))
numdiffLabel.pack()


AnswerEntry = Entry(MainFrame, font=("Arial",15))
AnswerEntry.pack(pady=10)


selectdiffbtn = Button(MainFrame, text="Select difficulty", width=16, font=("Arial", 15), background="red", command=selectDiff)
selectdiffbtn.pack()

gennumbtn = Button(MainFrame, text="Generate number", width=16, font=("Arial", 15), background="blue", command=generateNum)
gennumbtn.pack(pady=5)

guessbtn = Button(MainFrame, text="Guess", width=16, font=("Arial", 15), background="green", command=guessNumber)
guessbtn.pack(pady=5)



ResultLabel1 = Label(MainFrame, text="", font=("Arial",15))
ResultLabel2 = Label(MainFrame, text="", font=("Arial",15))
ResultLabel3 = Label(MainFrame, text="", font=("Arial",15))
ResultLabel1.pack()
ResultLabel2.pack()
ResultLabel3.pack()


root.mainloop()



