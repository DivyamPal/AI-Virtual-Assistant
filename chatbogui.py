from tkinter import *
root = Tk()
root.title("CHATBOT")
root.iconbitmap(r'C:\Users\Hritik\AppData\Roaming\JetBrains\PyCharmCE2020.2\scratches\icon.ico')
root.geometry("498x665")
#frame1= Label(text = "Welcome ",bd=3, relief= "sunken",bg ='indian red',fg= 'red')
frame2= LabelFrame(bd=5)
frame3= LabelFrame()

input = Entry(frame3,bg='lavender')
input.insert(0, "Enter your msg " )

def sendmsg():
    user.delete(0,END)
    user.insert(0, input.get())
speechbutton=Button(frame3, text="speech",bg='slateblue',font = ("Times",10,"bold"))
sendbutton =  Button(frame3, text="SEND",command=sendmsg,bg='royalblue3',fg='gold2',font = ("Times",10,"bold"))

user=Entry(frame2,bd=3,bg= "deep sky blue",fg = 'white', font = ("Times",10,"bold"))
user.insert(0, "YOUR QUERY" )
chatbot=Entry(frame2, bd=3,bg= "green yellow",fg = 'tomato', font = ("Times",10,"bold"))
chatbot.insert(0, "HI its me chatbot" )

#frame1.grid(row=0,column=0,ipadx=218,ipady=10,sticky=W)
frame2.grid(row=1,column=0 ,rowspan=4, columnspan=10 ,sticky=W,ipady=200)
frame3.grid(row=5,column=0,sticky=W)

speechbutton.grid(row=0,column=0,ipadx=20, ipady=15)
input.grid(row=0,column=1,columnspan=3,ipadx=100, ipady=15)
sendbutton.grid(row=0,column=4,ipadx=20, ipady=15)
user.grid(row=0,column=1,sticky= E,ipadx=55,pady=10,ipady=10)
chatbot.grid(row=1,column=0,sticky= W,ipadx=60,pady=10,ipady=10)

root.mainloop()