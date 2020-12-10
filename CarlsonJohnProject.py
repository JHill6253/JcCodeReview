from tkinter import *
import random
#Overall really good, I added a function to place all your UI components saving a few lines. 
# I looked over your ending functions and they could be improved but based on the size and amount of 
# work aleady put into it no reason to change anything. In the furture you can break those if statements 
#up into other functions that would cut down on lines of code and time complexity. 


root = Tk() 
root.geometry("600x1000")
root.title("Arithmetic Master")

myLabel = Label(root, text = "Choose the operation", width = 20, font = ("bold", 24))
myLabel.place(x = 100, y = 20)

operation = IntVar()
addition = Radiobutton(root, text = "Addition", padx = 5, variable = operation, value = 1, width = 20) 
subtraction = Radiobutton(root, text = "Subtraction", padx = 5, variable = operation, value = 2, width = 20)
multiplication = Radiobutton(root, text = "Multiplication", padx = 5, variable = operation, value = 3, width = 20)

#Consider making new problem button larger centered on new line for UI side 
addition.place(x = 10, y = 100)
subtraction.place(x = 150, y = 100)
multiplication.place(x = 290, y = 100)

# To make things easier you could write a function that takes these parameters 
def setPlace(val,wdth,fontBld,fontSize,X,Y):
    if(wdth>0 ):
        lbl =Label(root, textvariable = val, width = wdth, font = (fontBld, fontSize))
    else:
        lbl =Label(root, text = val, font = (fontBld, fontSize))
    lbl.place(x = X, y = Y)

    return lbl
    
value1 = StringVar()
val1 = setPlace(value1,5,"bold",50,175,150)

operator = StringVar()
operatorSign = setPlace(operator,1,"bold",60,100,250)

value2 = StringVar()
val2 = setPlace(value2,5,"bold",50,175,250) 

bar = setPlace('_______________',0,"bold",20,150,325)
 
feedback = StringVar() #instead of feedback could be strVarFeedback
bar = setPlace('feedback',0,"bold",15,425,450)


userEntry = StringVar() 
numberEntry = Entry(root, textvariable = userEntry, font = ("bold", 40))
numberEntry.configure(width = 5)
numberEntry.place(x = 200, y = 400)

bar = setPlace('_______________________________________',0,"bold",20,0,500)


addStat = StringVar()
addStatLabel = Label(root, textvariable = addStat, font = ("bold", 15))
addStatLabel.place(x = 0, y = 550)
addStat.set("Addition Statistics")
subStat = StringVar()
subStatLabel = Label(root, textvariable = subStat, font = ("bold", 15))
subStatLabel.place(x = 0, y = 600)
subStat.set("Subtraction Statistics")
mltStat = StringVar()
mltStatLabel = Label(root, textvariable = mltStat, font = ("bold", 15))
mltStatLabel.place(x = 0, y = 650)
mltStat.set("Multiplication Statistics")

addCount = 0
addRight = 0
subCount = 0
subRight = 0
mltCount = 0
mltRight = 0
correctAnswer = 0
canSubmit = False

def getGrammar(number):
    if number == 1:
        return " problem "
    else:
        return " problems "

def submitPressed():
    global addCount
    global addRight
    global subCount
    global subRight
    global mltCount
    global mltRight  
    global correctAnswer
    global canSubmit
    userAnswer = userEntry.get()
    # I mean alot of if's lol, based on the requirements this is good. You could make this alot shorter by using another function that breaks down
    # the responses but because of the already sheer size it's not really wort it at this point.
    if canSubmit == True:
        if operation.get() == 1:
            addSolve1 = value1.get()
            addSolve2 = value2.get()
            realAnswer = int(addSolve1) + int(addSolve2)
        if operation.get() == 2:
            subSolve1 = value1.get()
            subSolve2 = value2.get()
            realAnswer = int(subSolve1) - int(subSolve2)
        if operation.get() == 3:
            multSolve1 = value1.get()
            multSolve2 = value2.get()
            realAnswer = int(multSolve1) * int(multSolve2)
        if userAnswer.isdigit() == False:
            feedback.set("WRONG:" + str(realAnswer))        
        if int(userAnswer) == realAnswer:
            feedback.set("RIGHT!")
        if int(userAnswer) != realAnswer:
            feedback.set("WRONG:" + str(realAnswer))
    if operation.get() == 1 and int(userAnswer) == realAnswer:
        addCount = addCount + 1
        addRight = addRight + 1
        addStat.set("You solved " + str(addRight) + " addition problems out of " + str(addCount) + " problems correctly.")
    if operation.get() == 1 and int(userAnswer) != realAnswer:
        addCount = addCount + 1
        addStat.set("You solved " + str(addRight) + " addition problems out of " + str(addCount) + " problems correctly.")
    if operation.get() == 2 and int(userAnswer) == realAnswer:
        subCount = subCount + 1
        subRight = subRight + 1
        subStat.set("You solved " + str(subRight) + " subtraction problems out of " + str(subCount) + " problems correctly.")
    if operation.get() == 2 and int(userAnswer) != realAnswer:
        subCount = subCount + 1
        subStat.set("You solved " + str(subRight) + " subtraction problems out of " + str(subCount) + " problems correctly.")
    if operation.get() == 3 and int(userAnswer) == realAnswer:
        mltCount = mltCount + 1
        mltRight = mltRight + 1
        mltStat.set("You solved " + str(mltRight) + " multiplication problems out of " + str(mltCount) + " problems correctly.")
    if operation.get() == 3 and int(userAnswer) != realAnswer:
        mltCount = mltCount + 1
        mltStat.set("You solved " + str(mltRight) + " multiplication problems out of " + str(mltCount) + " problems correctly.")        
    userEntry.set("")
    canSubmit = False
    
def newPressed():
    #Same comment from above 
    global canSubmit
    canSubmit = True
    feedback.set("")
    if operation.get() == 1 or 3:
        value1.set(random.randint(10, 99))
        value2.set(random.randint(10, 99))
    if operation.get() == 2:
        value1.set(random.randint(10, 99))
        subHelp = value1.get()
        subHelp = int(subHelp)
        value2.set(random.randint(9, (subHelp - 1)))
    if operation.get() == 1:
        operator.set("+")
    if operation.get() == 2:
        operator.set("-")
    if operation.get() == 3:
        operator.set("x")

Button(root, text = "New Problem", width = 10, bg = "black", fg = "yellow", command = newPressed).place(x = 475, y = 100)

Button(root, text = "Submit", width = 10, bg = "black", fg = "yellow", command = submitPressed).place(x = 475, y = 400)

root.mainloop()
