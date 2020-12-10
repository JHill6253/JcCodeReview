'''
This is the backbone for your project.  Download this file and save it using
the naming structure LastFirstProject.py.  For example, if I were re-naming
this file, I would name it SzecseiDeniseProject.py

You will upload this file with your solutions to the individual parts of the
problem.  Points will be awarded based on the number of steps that you complete
correctly.  You should not use any outside resources (tutors, CS students,
industry professionals, Chegg, StackOverflow, etc...).  The work that you submit
must be your own.  If you need to review how to incorporate various GUI components
into a progrem or script, review the Widgets example that I developed before the
Thanksgiving break.  All of the python instructions have been provided in that
example.  Using functions that I have not discussed during lecture will earn
0 points for that particular problem.  For example, there are many ways to
place widgets into a root window.  I want you to use the method that I demonstrated
in the example.  So, if you decide to use a different approach, you will earn
0 points for that component.  If you want to explore different ways to
create GUIs, that is great.  But for this assignment, I want you to stick to
what was presented in class.

If you run this script, a small window should appear...it should not crash!
The script that you submit MUST run without any errors.  If it cannot run
because of syntax errors, you will get a 0 on the project.  So, make sure
that you test your code before you submit it.

WARNING: LATE WORK IS NOT ACCEPTED.  DO NOT WAIT UNTIL THE LAST MINUTE TO
SUBMIT YOUR PROJECT.  IF ICON GOES DOWN, OR YOU LOSE INTERNET, YOU WILL RECEIVE
A 0 ON THE ASSIGNMENT.  AS SOON AS YOU MAKE PROGRESS, SUBMIT A WORKING VERSION
OF YOUR INTERMEDIATE PROGRAM SO THAT YOU WON'T GET A 0 ON THE ASSIGNMENT.  THE
TA WILL GRADE THE MOST RECENT SUBMISSION.

IMPORTANT NOTES: 

ALL PROBLEMS INVOLVE 2-DIGIT NUMBERS...MAKE SURE THAT YOU GENERATE
RANDOM 2 DIGIT NUMBERS APPROPRIATELY

WHEN THE SUBMIT BUTTON IS PRESSED, THE ENTRY BOX IS CLEARED

CHECK THE VIDEO FOR THE WORDING FOR THE STATISTICS AND THE FEEDBACK

FOR SUBTRACTION PROBLEMS, MAKE SURE THAT THE PROBLEMS INVOLVE SUBTRACTING
A SMALLER NUMBER FROM A LARGER NUMBER, SO THAT THE ANSWER IS ALWAYS POSITIVE

PAY ATTENTION TO DATA TYPES WHEN COMPARNING THE USER'S ANSWER TO THE
CORRECT ANSWER.  THERE ARE DANGERS INVOLVED IN TRYING TO CAST TO AN INTEGER
ESPECIALLY WHEN IT COMES TO USERS MESSING AROUND AND TRYING TO MAKE YOUR
PROGRAM CRASH.  YOUR PROGRAM SHOULD NOT CRASH IF THE USER ENTERS NON-DIGIT
INFORMATION.

IF CLARIFICATIONS TO THIS PROJECT ARE MADE, THEY WILL BE IN A MODULE
TITLED: PROJECT CLARIFICATIONS.  CHECK IT OFTEN, IN CASE ANYTHING NEEDS
TO BE CLARIFIED.  IF YOU ARE NOT SURE ABOUT SOMETHING, ASK!

'''
#we need to import tkinter to create the GUI
from tkinter import *

#we will be generating random numbers for our problems, so we will import
#the random library
import random

#we will need a Tk() root object to create your window, and put things inside of it
root = Tk() 

#perhaps we want to set the size of our window and place things in our window
#set the size of the window to be 600 units wide (the x-component) and
#1000 units high/long (the y-component)
#2 points  (CUMULATIVE POINTS: 2/100)
root.geometry("600x1000")

#create a title for the window: Arithmetic Master
#2 points  (CUMULATIVE POINTS: 4/100)
root.title("Arithmetic Master")

#put a label on the screen that reads: Choose the operation
#determine where it should go so that it has the general look of the
#window that I used in my demonstration
#4 points  (CUMULATIVE POINTS: 6/100)
myLabel = Label(root, text = "Choose the operation", width = 20, font = ("bold", 24))
#add to screen
myLabel.place(x = 100, y = 20)

#put radio buttons on the screen: Addition, Subtraction, Multiplication
#create a variable to store the operation that is selected so that
#you can create the correct type of problem.  Use an IntVar() for this.
#determine where they should go so that it has the general look of
#the window that I used in my demonstration
#10 points  (CUMULATIVE POINTS: 16/100)
operation = IntVar()

addition = Radiobutton(root, text = "Addition", padx = 5, variable = operation, value = 1, width = 20) 
subtraction = Radiobutton(root, text = "Subtraction", padx = 5, variable = operation, value = 2, width = 20)
multiplication = Radiobutton(root, text = "Multiplication", padx = 5, variable = operation, value = 3, width = 20)

addition.place(x = 10, y = 100)
subtraction.place(x = 150, y = 100)
multiplication.place(x = 290, y = 100)

#we will now create the widgets that present the problem to the user
#we will deal with the buttons later on

#we will need to be able to present the first number, the operation,
#and the second number.  Use the symbols  +   -   x   for the operations
#when presenting the problem.  Use a bold font, and for the numbers
#use a font size 50, and for the operator use a font size of 60
#use several variables (StringVar()) to be able to change the contents
#of each component individually.
#NOTE: if you want to focus on the placement first, just set the
#text to be a two-digit number so you can see what it looks like
#on the screen.  You can then incorporate the StringVar() component
#after you have decided on location.

#First, create a label for the first value in the problem
#you will want to be able to change the contents of this label
#so you'll need a variable to store the value (StringVar())
#place the first value on the screen, arranging it so that it resembles
#the model in the demonstration
#5 points  (CUMULATIVE POINTS: 21/100)
value1 = StringVar()
val1 = Label(root, textvariable = value1, width = 5, font = ("bold", 50))
val1.place(x = 175, y = 150)

#create a label for the operator and place it on the screen so that it looks.  
#nice.  Remember that this label will change to reflect the operation selected 
#by the user, so we will need a variable to update its contents.  
#we will use a StringVar(), and the symbols +    -    x for the operations
#4 points  (CUMULATIVE POINTS: 25/100)
operator = StringVar()
operatorSign = Label(root, textvariable = operator, width = 1, font = ("bold", 60))
operatorSign.place(x = 100, y = 250)

#Create a label for the second value in the problem
#you will want to be able to change the contents of this label
#so you'll need a variable to store the value (StringVar())
#place the second value on the screen, arranging it so that it resembles
#the model in the demonstration
#5 points  (CUMULATIVE POINTS: 30/100)
value2 = StringVar()
val2 = Label(root, textvariable = value2, width = 5, font = ("bold", 50))
val2.place(x = 175, y = 250)

#Next, put a label for the bar.  This will not change, so we do not need
#a variable for its contents.  Place it on the screen so that it looks nice
#with the other label placements.  Use a bold font of size 20 for this label
#2 points  (CUMULATIVE POINTS: 32/100)
bar = Label(root, text = "_________________", font = ("bold", 20))
bar.place(x = 150, y = 325)

#Create a label for the feedback...Since this will change as the user
#solves problems, we need a StringVar() to keep track of its values
#use a bold font of size 15 for this label
#remember to include the correct answer if the submission is incorrect
#HINT: if you want the feedback to be invisible after a new problem
#is presented, set its contents to be the empty string.
#5 points    (CUMULATIVE POINTS: 37/100)
feedback = StringVar()
feedbackLabel = Label(root, textvariable = feedback, font = ("bold", 15))
feedbackLabel.place(x = 425, y = 450)

#make an entry box for the answer and place it on the screen.  You'll need 
#access to the contents, because you will have to check if their answer 
#is correct or incorrect.  Use a bold font of size 40 for this entry box
#4 points   (CUMULATIVE POINTS: 41/100)
userEntry = StringVar()
numberEntry = Entry(root, textvariable = userEntry, font = ("bold", 40))
numberEntry.configure(width = 5)
numberEntry.place(x = 200, y = 400)

#Next, we'll deal with the statistics

#let's put a label for the bar to separate the problem presentation
#from the statistics onto the screen.  Again, the contents will
#not change, so we do not need a variable to access the information.
#2 points  (CUMULATIVE POINTS: 43/100)
bar2 = Label(root, text = "_______________________________________", font = ("bold", 20))
bar2.place(x = 0, y = 500)

#next, put labels for the statistics for addition/subtraction/multiplication 
#onto the screen.  Remember that we'll be updating these lables, so we'll
#need some StringVar() variables to keep track of their contents

#Put the Addition statistics Label on the screen
#Initially set the contents of the label to be "Addition Statistics"
#3 points  (CUMULATIVE POINTS: 46/100)
addStat = StringVar()
addStatLabel = Label(root, textvariable = addStat, font = ("bold", 15))
addStatLabel.place(x = 0, y = 550)
addStat.set("Addition Statistics")

#Put the Subtraction statistics Label on the screen
#Initially set the contents of the label to be "Subtraction Statistics"
#3 points   (CUMULATIVE POINTS: 49/100)
subStat = StringVar()
subStatLabel = Label(root, textvariable = subStat, font = ("bold", 15))
subStatLabel.place(x = 0, y = 600)
subStat.set("Subtraction Statistics")


#Put the Multiplication statistics Label on the screen
#Initially set the contents of the label to be "Multiplication Statistics"
#3 points   (CUMULATIVE POINTS: 52/100)
mltStat = StringVar()
mltStatLabel = Label(root, textvariable = mltStat, font = ("bold", 15))
mltStatLabel.place(x = 0, y = 650)
mltStat.set("Multiplication Statistics")


#here are the global variables you will use to track the number of each type of problem
#as well as their success rate; you will reference them in a function
addCount = 0
addRight = 0

subCount = 0
subRight = 0

mltCount = 0
mltRight = 0

correctAnswer = 0
canSubmit = False

#because the grammar changes depending on the number associated with the word
#'problem' we will create a helper function to give us the correct phrasing
def getGrammar(number):
    if number == 1:
        return " problem "
    else:
        return " problems "

#now we can deal with our buttons.  Remember that we have two buttons to handle:
#the submit button and the new button.  The new button will generate a new problem,
#and the submit button will check the answer and update the statistics.  Follow the
#logic in the comments to complete these functions.  Some of the things I have
#have done for you (and specified the variable names...so don't change them!).

#you will fill in the details for a submitPressed function to associate with the button
#20 points   (CUMULATIVE POINTS: 72/100)

def submitPressed():
    #reference the global variable count (let python know that count is a global variable,
    #not a local variable.  Every time i press the button, the counter will increment by 1

    global addCount
    global addRight
    
    global subCount
    global subRight
    
    global mltCount
    global mltRight  
    
    global correctAnswer
    global canSubmit
    
    
    #get the user's answer from the entry box:
    userAnswer = userEntry.get()
    #here is the outline of what you need to do:
    #only proceed if a question can be submitted
    #get/calculate the correct answer
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
            
    #get the operation so that you can update the correct statistics!
    #HINT: work this logic out for one operation (addition) first, and test
    #your logic.  if your logic is correct, then you should be able to copy
    #and paste (and modify your variables accordingly) for the other two
    #operations.
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
        
    #once you are finished, remember to clear out the contents of the entry box
    #and change to boolean so that a user cannot submit again...they only get
    #to submit after a new question has been created.
    userEntry.set("")
    canSubmit = False
    
#you will fill in the details for a newPressed function to associate with the button
#20 points   (CUMULATIVE POINTS: 92/100) 

def newPressed():
    #this is a new problem, so the user should be able to submit their answer
    #you'll want to update that global variable
    global canSubmit
    canSubmit = True
    #remove the feedback text
    feedback.set("")
    #generate the numbers for the problem...be careful with subtraction!
    if operation.get() == 1 or 3:
        value1.set(random.randint(10, 99))
        value2.set(random.randint(10, 99))
    if operation.get() == 2:
        value1.set(random.randint(10, 99))
        subHelp = value1.get()
        subHelp = int(subHelp)
        value2.set(random.randint(9, (subHelp - 1)))
    #determine the operator for the problem
    if operation.get() == 1:
        operator.set("+")
    if operation.get() == 2:
        operator.set("-")
    if operation.get() == 3:
        operator.set("x")
        
#create a new button and put it near the radio buttons on the screen.  The
#text should read 'New Problem'...choose colors to customize your button (if you want)
#be sure to connect the functionality to the appropriate function created previously!
#4 points   (CUMULATIVE POINTS: 96/100)
Button(root, text = "New Problem", width = 10, bg = "black", fg = "yellow", command = newPressed).place(x = 475, y = 100)

#create a submit button and put it near the Entry box on the screen.  The
#text should read 'Submit'...choose colors to customize your button (if you want)
#be sure to connect the functionality to the appropriate function created previously!
#4 points   (CUMULATIVE POINTS: 100/100)
Button(root, text = "Submit", width = 10, bg = "black", fg = "yellow", command = submitPressed).place(x = 475, y = 400)

#this line of code will run your function and create the window for you
root.mainloop()
