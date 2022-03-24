from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os  # for music
import speech_recognition as s_r
#import smptlib
import pyautogui  #for screenshot

# install webdriver for required browser to use selenium
#from selenium import webdriver




#import m2
#from subprocess import call
#from tkinter import ttk
root = Tk()
root.title('AI Virtual Assistant')
#root.iconbitmap('1.jpg')

root.geometry("1055x633")
#root.configure(bg='maroon')

#img = ImageTk.PhotoImage(Image.open("100.jpg"))
#imglabel = Label(image=img)
#imglabel.pack()
#def call():





# Microsoft speech Api - sapi5
engine = pyttsx3.init('sapi5')
# getproperty is use to get the total number of voice available in your system
voices = engine.getProperty('voices')
# set property is use to set the voice of our assistant
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

canvas = Canvas(width=800, height=800)
canvas.pack(expand=YES, fill=BOTH)

image = ImageTk.PhotoImage(file="696969.jpg")
canvas.create_image(10, 10, image=image, anchor=NW)
img1 = ImageTk.PhotoImage(Image.open("222.png"))
img2 = ImageTk.PhotoImage(Image.open("777.png"))
img3 = ImageTk.PhotoImage(Image.open("444.png"))
img4 = ImageTk.PhotoImage(Image.open("555.png"))

frame = LabelFrame(canvas )
frame.pack(side = BOTTOM)


# For Greeting purpose
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour <= 12:
        speak(" Good morning sir")
    elif hour >= 12 and hour <= 18:
        speak(" Good evening sir")
    else:
        speak("Good night sir")

    speak("I am Friday your Personal Voice Assistant ")



mybutton1 = Button(frame, text="   Voice Assistant ", image=img1, command=wishme(),
                   compound=RIGHT, fg="sky blue", activebackground="black", activeforeground="white",
                   bg="purple", bd=10, padx=38, pady=2,font=("Helvetica", 15)).pack()
mybutton2 = Button(frame, text="   Chat BOT ", fg="sky blue", activebackground="black",
                   activeforeground="white", bg="purple", bd=10, image=img2,
                   compound=RIGHT, padx=53, pady=2, font=("Helvetica", 15)).pack()

buttonquit = Button(frame, text="   EXIT HERE", command=root.quit, fg="sky blue",
                    activebackground="black", activeforeground="white", bg="purple", bd=10, image=img3,
                    compound=RIGHT, padx=50, pady=2, font=("Helvetica", 15)).pack()
root.mainloop()
# takecommand takes input from user and return it in string form

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        for i in sr.Microphone.list_microphone_names():
            print(i)
            print("\n")
        print("SPEAK...")
        r.energy_threshold=500
        r.dynamic_energy_threshold=500
        r.pause_threshold = 1  # it is seconds of non speaking before a phrase is considered Complete by default its set to zero
        audio = r.listen(source)
    try:
        print("RECOGNIZING...")
        query = r.recognize_google(audio, Language='en-in')
        print(query)
    except Exception as e:
        print("PLEASE SAY IT AGAIN...")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your password')
    server.sendmail('your email', to, content)
    server.close()
"""
def calculator():
    # to take symbols and number from calculate string

    OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators

    PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities


    def infix_to_postfix(expression):  # input expression
        stack = []  # initially stack empty
        output = ''  # initially output empty
        for ch in expression:

            if ch not in OPERATORS:  # if an operand then put it directly in postfix expression
                output += ch
            elif ch == '(':  # else operators should be put in stack
                stack.append('(')
            elif ch == ')':
                while stack and stack[-1] != '(':
                    output += stack.pop()
                stack.pop()
            else:
                # lesser priority can't be on top on higher or equal priority

                # so pop and put in output
                while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                    output += stack.pop()
                stack.append(ch)
        while stack:
            output += stack.pop()
        return output


    expression = input('Enter  expression ')
    pexp = infix_to_postfix(expression)


class Evaluate:
    # Constructor to initialize the class variables
    def _init_(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # check if the stack is empty

    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
        # The main function that converts given infix expression

    # to postfix expression
    def evaluatePostfix(self, exp):
        # Iterate over the expression for conversion
        for i in exp:
            # If the scanned character is an operand

            # (number here) push it to the stack

            if i.isdigit():
                self.push(i)
            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(int(eval(val2 + i + val1))))
        return int(self.pop())


obj = Evaluate(len(pexp))
print(obj.evaluatePostfix(pexp))
"""


#def climate():
#    driver = webdriver.Firefox()
#    driver.get("https://weather.com/en-IN/weather/today/l/26.85,80.95?par=google&temp=c")



if __name__ == "__main__":
    wishme()
    speak("Here is the quick whether report..")
 #   climate()
    while True:
        # query is conv in lower case so that if statement doesn't treat capital and lower case query in a different manner
        query = takecommand().lower()
        if 'search' in query:
            speak("Please wait i am searching...")
            query = query.replace("wikipedia", " ")
            # sentence = 2--> only beginning 2 statements are going to be in variable result
            results = wikipedia.summary(query, sentence=2)
            speak(results)
            print(results)
        elif "youtube" in query:
            webbrowser.open("youtube.in")
        elif "google" in query:
            webbrowser.open("Google.in")
        elif "Amazon" in query:
            webbrowser.open("Amazon.in")
        elif "Flipkart" in query:
            webbrowser.open("Flipkart.in")
        elif "music" in query:
            music_dir = 'D:\\music'
            songs = os.listendir(music_dir)
            # Here we are going to  play 1st song everytime we ask friday to play the song
            os.startfile(os.pathjoin(music_dir, songs[0]))
        elif "time" in query:
            strtime = datetime.datetime.now().strftime( "%H: %M: %S")
            speak(f"Sir the time is {strtime}")
        elif "open code" in query:
            codepath = "....target of vs code"

            # Here email is sent to hritik only
        elif "email to hritik" in query:
            try:
                speak("what shoul i send")
                comtent = takecommand()
                to = "hritik162001@gmail.com"
                sendemail(to, content)
                speak("Sir, email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry there is some error in sending email")

        #elif "calculate" in query:
         #   calculator()

        elif "Screenshot" in query:
            screenshot = pyautogui.screenshot()
            screenshot.save()







