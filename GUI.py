from tkinter import *
from typing import Container, Sized
import time
<<<<<<< HEAD
<<<<<<< HEAD
from sys import exit
import test_file as tf
from actions.structural_actions import chooseAccounts
import insta_bot as ib
from main import one
=======
>>>>>>> 32df6be8cb9bd951eaf545e1fdaf59838d46bfbc

def output():
    from ProcessManagement import ProcessManager
    account = acc.get()
    account = account.split(",")
    bots = bot_num.get()
    likes = like_num.get()
    comments = com_num.get()
    comsperpost = cpp.get()
    topics = topic.get()
    if account == "":
        print("You need to select a tageted account")
    elif bots == "":
        bots = None
    elif likes == "":
        likes = None
    elif comments == 0:
        ProcessManager(account,bots,likes,comments,0,"")
    else:
        pass
    ProcessManager(account,bots,likes,comments,comsperpost,topics)

<<<<<<< HEAD

#funtions in GUI
def darkMode():
    root["bg"]="#000000"
    title["bg"]="#000000"
    title["fg"]="#ffffff"
    command1["bg"]="#000000"
    command1["fg"]="#ffffff"
    command2["bg"]="#000000"
    command2["fg"]="#ffffff"
    dark["bg"]="#000000"
    dark["fg"]="#ffffff"
    return

def lightMode():
    root["bg"]="#ffffff"
    title["bg"]="#ffffff"
    title["fg"]="#000000"
    command1["bg"]="#ffffff"
    command1["fg"]="#000000"
    command2["bg"]="#ffffff"
    command2["fg"]="#000000"
    dark["bg"]="#ffffff"
    dark["fg"]="#000000"
    return

#content of GUI
root.title("Instagram Bot")
title = Label(root, text="Bot Settings", )
command1 = Label(root, text="target account")
command2 = Label(root, text="number of bots")
dark = Label(root, text="Dark Mode")
on = Button(root, text="ON", command=darkMode)
off = Button(root, text="OFF", command=lightMode)
start = Button(root, text="START", command=one)

#styling of GUI
root.geometry("1100x800")
title["font"]="Ariel", 20

#placing elements
title.grid(row=0, column=0)
command1.grid(row=1, column=0,)
command2.grid(row=1, column=1)
dark.grid(row=2, column=0)
on.grid(row=2, column=1)
off.grid(row=2, column=2)
start.grid(row=3, column=0)

=======
def restart():
    root.destroy()


if __name__ == "__main__":
    #creating standard sizes
    elem_width = 20
    input_width = 21
    rl = "flat"  

    #functions in GUI
    def darkMode():
        root["bg"]="#000000"
        title["bg"]="#000000"
        title["fg"]="#ffffff"
        command1["bg"]="#000000"
        command1["fg"]="#ffffff"
        command2["bg"]="#000000"
        command2["fg"]="#ffffff"
        command3["bg"]="#000000"
        command3["fg"]="#ffffff"
        command4["bg"]="#000000"
        command4["fg"]="#ffffff"
        command5["bg"]="#000000"
        command5["fg"]="#ffffff"
        command6["bg"]="#000000"
        command6["fg"]="#ffffff"
        dark["bg"]="#000000"
        dark["fg"]="#ffffff"

        acc.configure(bg="gray50",fg="white")
        bot_num.configure(bg="gray50",fg="white")
        like_num.configure(bg="gray50",fg="white")
        com_num.configure(bg="gray50",fg="white")
        cpp.configure(bg="gray50",fg="white")
        topic.configure(bg="gray50",fg="white")

        on.configure(bg="gray30",fg="white")
        off.configure(bg="gray30",fg="white")
        start.configure(bg="gray30",fg="white")
        close.configure(bg="gray30",fg="white")


    def lightMode():
        root["bg"]=defaultbg
        title["bg"]=defaultbg
        title["fg"]="#000000"
        command1["bg"]=defaultbg
        command1["fg"]="#000000"
        command2["bg"]=defaultbg
        command2["fg"]="#000000"
        command3["bg"]=defaultbg
        command3["fg"]="#000000"
        command4["bg"]=defaultbg
        command4["fg"]="#000000"
        command5["bg"]=defaultbg
        command5["fg"]="#000000"
        command6["bg"]=defaultbg
        command6["fg"]="#000000"
        dark["bg"]=defaultbg
        dark["fg"]="#000000"

        acc.configure(bg="white",fg="black")
        bot_num.configure(bg="white",fg="black")
        like_num.configure(bg="white",fg="black")
        com_num.configure(bg="white",fg="black")
        cpp.configure(bg="white",fg="black")
        topic.configure(bg="white",fg="black")
>>>>>>> 32df6be8cb9bd951eaf545e1fdaf59838d46bfbc

        on.configure(bg=defaultbg,fg="black")
        off.configure(bg=defaultbg,fg="black")
        start.configure(bg=defaultbg,fg="black")
        close.configure(bg=defaultbg,fg="black")


    #creating the GUI
    root = Tk()
    defaultbg = root.cget('bg')
        
    #content of GUI
    root.title("Instagram Bot")
    title = Label(root, text="Bot Settings")
    command1 = Label(root, text="target account", width=elem_width,relief=rl)
    command2 = Label(root, text="number of bots", width=elem_width,relief=rl)
    command3 = Label(root, text="number of likes", width=elem_width,relief=rl)
    command4 = Label(root, text="number of comments", width=elem_width,relief=rl)
    command5 = Label(root, text="number of comments p.p.", width=elem_width,relief=rl)
    command6 = Label(root, text="topic", width=elem_width,relief=rl)
    dark = Label(root, text="Dark Mode")
    on = Button(root, text="ON", command=darkMode,width=input_width)
    off = Button(root, text="OFF", command=lightMode,width=input_width)
    acc = Entry(root,width=input_width)
    bot_num = Entry(root,width=input_width)
    like_num = Entry(root,width=input_width)
    com_num = Entry(root,width=input_width)
    cpp = Entry(root,width=input_width)
    topic = Entry(root,width=input_width)
    start = Button(root, text="START", command=output)
    close = Button(root,text="CLOSE", command=root.destroy)

    #styling of GUI
    root.geometry("900x200")
    title["font"]="Ariel", 20

    #placing elements
    title.grid(row=0, column=0,columnspan=6)
    command1.grid(row=3, column=0,sticky="nesw")
    command2.grid(row=3, column=1,sticky="nesw")
    command3.grid(row=3, column=2,sticky="nesw")
    command4.grid(row=3, column=3,sticky="nesw")
    command5.grid(row=3, column=4,sticky="nesw")
    command6.grid(row=3, column=5,sticky="nesw")
    dark.grid(row=1, column=0,columnspan=2)
    on.grid(row=2, column=0,sticky="nws")
    off.grid(row=2, column=1,sticky="nws")
    acc.grid(row=4,column=0,sticky="nesw")
    bot_num.grid(row=4,column=1,sticky="nesw")
    like_num.grid(row=4,column=2,sticky="nesw")
    com_num.grid(row=4,column=3,sticky="nesw")
    cpp.grid(row=4,column=4,sticky="nesw")
    topic.grid(row=4,column=5,sticky="nesw")
    start.grid(row=5, column=0,columnspan=6,sticky="nesw",pady=(10,0))
    close.grid(row=6,column=0,columnspan=6,sticky="nesw")

    #creates mainloop
    root.mainloop()
=======
import os
import sys


if __name__ == "__main__":
    class GUI_Generator:

        def __init__(self): 
            #creating standard sizes
            elem_width = 20
            input_width = 21
            rl = "flat"

            #creating the GUI
            root = Tk()

            defaultbg = root.cget('bg')
            self.defaultbg = defaultbg

            #Information for OptionMenu
            from actions.comments import comDict
            selected_topic = StringVar(root)
            topics = comDict["topic_index"]
            selected_topic.set(topics[0])
                
            #content of GUI
            root.title("Instagram Bot")
            title = Label(root, text="Bot Settings")
            command1 = Label(root, text="target account", width=elem_width,relief=rl)
            command2 = Label(root, text="number of bots", width=elem_width,relief=rl)
            command3 = Label(root, text="number of likes", width=elem_width,relief=rl)
            command4 = Label(root, text="number of comments", width=elem_width,relief=rl)
            command5 = Label(root, text="number of comments p.p.", width=elem_width,relief=rl)
            command6 = Label(root,text="topic", width=elem_width,relief=rl)
            #dark = Label(root, text="Dark Mode")
            on = Button(root, text="DARK", command=self.darkMode,width=input_width)
            off = Button(root, text="LIGHT", command=self.lightMode,width=input_width)
            acc = Entry(root,width=input_width)
            bot_num = Entry(root,width=input_width)
            like_num = Entry(root,width=input_width)
            com_num = Entry(root,width=input_width)
            cpp = Entry(root,width=input_width)
            topic = OptionMenu(root,selected_topic,*topics)
            topic.config(width=input_width,bg=defaultbg,highlightbackground="white")
            topic["menu"].config(bg="white",fg="black")
            start = Button(root, text="START", command=self.output)
            close = Button(root,text="CLOSE", command=root.destroy)
            clear = Button(root,text="CLEAR",command=self.clearing)

            #styling of GUI
            root.geometry("925x200")
            title["font"]="Ariel", 20

            #placing elements
            title.grid(row=0, column=0,columnspan=6)
            command1.grid(row=3, column=0,sticky="nesw")
            command2.grid(row=3, column=1,sticky="nesw")
            command3.grid(row=3, column=2,sticky="nesw")
            command4.grid(row=3, column=3,sticky="nesw")
            command5.grid(row=3, column=4,sticky="nesw")
            command6.grid(row=3, column=5,sticky="nesw")
            #dark.grid(row=1, column=0,columnspan=2)
            on.grid(row=2, column=2,sticky="nws")
            off.grid(row=2, column=3,sticky="nws")
            acc.grid(row=4,column=0,sticky="nesw")
            bot_num.grid(row=4,column=1,sticky="nesw")
            like_num.grid(row=4,column=2,sticky="nesw")
            com_num.grid(row=4,column=3,sticky="nesw")
            cpp.grid(row=4,column=4,sticky="nesw")
            topic.grid(row=4,column=5,sticky="nesw")
            start.grid(row=5, column=0,columnspan=3,sticky="nesw",pady=(10,0))
            close.grid(row=6,column=0,columnspan=6,sticky="nesw")
            clear.grid(row=5,column=3,columnspan=3,sticky="nesw",pady=(10,0))

            self.root = root
            self.title = title
            self.command1 = command1
            self.command2 = command2
            self.command3 = command3
            self.command4 = command4
            self.command5 = command5
            self.command6 = command6
            #self.dark = dark
            self.on = on
            self.off = off
            self.acc = acc
            self.bot_num = bot_num
            self.like_num = like_num
            self.com_num = com_num
            self.cpp = cpp
            self.topic = topic
            self.selected_topic = selected_topic
            self.start = start
            self.close = close
            self.clear = clear

            #creates mainloop
            root.mainloop()


        #functions in GUI
        def darkMode(self):
            self.root["bg"]="#000000"
            self.title["bg"]="#000000"
            self.title["fg"]="#ffffff"
            self.command1["bg"]="#000000"
            self.command1["fg"]="#ffffff"
            self.command2["bg"]="#000000"
            self.command2["fg"]="#ffffff"
            self.command3["bg"]="#000000"
            self.command3["fg"]="#ffffff"
            self.command4["bg"]="#000000"
            self.command4["fg"]="#ffffff"
            self.command5["bg"]="#000000"
            self.command5["fg"]="#ffffff"
            self.command6["bg"]="#000000"
            self.command6["fg"]="#ffffff"
            #self.dark["bg"]="#000000"
            #self.dark["fg"]="#ffffff"

            self.acc.configure(bg="gray50",fg="white")
            self.bot_num.configure(bg="gray50",fg="white")
            self.like_num.configure(bg="gray50",fg="white")
            self.com_num.configure(bg="gray50",fg="white")
            self.cpp.configure(bg="gray50",fg="white")
            
            self.topic.configure(bg="gray30",fg="white",highlightbackground="gray50")
            self.topic["menu"].config(bg="gray30",fg="white")
            self.on.configure(bg="gray30",fg="white")
            self.off.configure(bg="gray30",fg="white")
            self.start.configure(bg="gray30",fg="white")
            self.close.configure(bg="gray30",fg="white")
            self.clear.configure(bg="gray30",fg="white")


        def lightMode(self):
            self.root["bg"]=self.defaultbg
            self.title["bg"]=self.defaultbg
            self.title["fg"]="#000000"
            self.command1["bg"]=self.defaultbg
            self.command1["fg"]="#000000"
            self.command2["bg"]=self.defaultbg
            self.command2["fg"]="#000000"
            self.command3["bg"]=self.defaultbg
            self.command3["fg"]="#000000"
            self.command4["bg"]=self.defaultbg
            self.command4["fg"]="#000000"
            self.command5["bg"]=self.defaultbg
            self.command5["fg"]="#000000"
            self.command6["bg"]=self.defaultbg
            self.command6["fg"]="#000000"
            #self.dark["bg"]=self.defaultbg
            #self.dark["fg"]="#000000"

            self.acc.configure(bg="white",fg="black")
            self.bot_num.configure(bg="white",fg="black")
            self.like_num.configure(bg="white",fg="black")
            self.com_num.configure(bg="white",fg="black")
            self.cpp.configure(bg="white",fg="black")
            
            self.topic.configure(bg=self.defaultbg,fg="black",highlightbackground="white")
            self.topic["menu"].config(bg=self.defaultbg,fg="black")
            self.on.configure(bg=self.defaultbg,fg="black")
            self.off.configure(bg=self.defaultbg,fg="black")
            self.start.configure(bg=self.defaultbg,fg="black")
            self.close.configure(bg=self.defaultbg,fg="black")
            self.clear.configure(bg=self.defaultbg,fg="black")

        def output(self):
            from ProcessManagement import ProcessManager
            account = self.acc.get()
            account = account.split(",")
            bots = self.bot_num.get()
            likes = self.like_num.get()
            comments = self.com_num.get()
            comsperpost = self.cpp.get()
            topics = self.selected_topic.get()
            if account == "":
                print("You need to select a tageted account")
            elif bots == "":
                bots = None
            elif likes == "":
                likes = None
            elif comments == 0:
                ProcessManager(account,bots,likes,comments,0,"")
            else:
                pass
            ProcessManager(account,bots,likes,comments,comsperpost,topics)

        def clearing(self):
            self.acc.config(textvariable="")
            self.bot_num.config(textvariable="")
            self.like_num.config(textvariable="")
            self.com_num.config(textvariable="")

if __name__ ==  "__main__":
    GG = GUI_Generator()
>>>>>>> 7864f955f2aa1acba5898e6bc7b9860830b12457
