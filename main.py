from tkinter import *
import tkinter.messagebox as tkmb
import pyautogui
import pyttsx3
import time

def speak(command):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(command)
    engine.runAndWait()

class Gui(Tk):
    def __init__(self):
        super().__init__() # Calling ParentClass's __init__ method
        self.geometry("1000x500")
        self.minsize(500,250)
        self.maxsize(1920,1200)
        self.title('Notepad')
        self.config(background = "#641E16")
        self.size = 10

    def s_bar(self):
        self.var = StringVar()
        self.var.set("Active.....")
        self.s_bar = Label(self, textvariable=self.var,relief="flat",anchor=W,foreground="black")
        self.s_bar.config(background = "#D0D3D4")
        self.s_bar.pack(side=BOTTOM,fill=X)

    def menu(self):
        menubar = Menu(self)
        m1 = Menu(menubar,tearoff=0)
        m1.add_command(label = "New",command = self.new)
        m1.add_command(label = "Save",command = self.save) 
        m1.add_separator()       
        m1.add_command(label = "Exit",command = self.exit)
        self.config(menu=menubar)
        menubar.add_cascade(label = "File",menu = m1)

        m3 = Menu(menubar,tearoff=0)
        m3.add_command(label = "Speak",command = self.speak)
        self.config(menu=menubar)
        menubar.add_cascade(label = "Special !!",menu = m3)

        m4 = Menu(menubar,tearoff=0)
        m4.add_command(label = "Cut",command = self.cut)
        m4.add_command(label = "Copy",command = self.copy)
        m4.add_command(label = "Paste",command = self.paste)
        self.config(menu=menubar)
        menubar.add_cascade(label = "Edit",menu = m4)

        m5 = Menu(menubar,tearoff=0)
        m5.add_command(label = "Help",command = self.help)
        self.config(menu=menubar)
        menubar.add_cascade(label = "Help",menu = m5) 

    def cut(self):
        self.text_area.event_generate(("<<Cut>>"))
        self.var.set("Cut")
        self.s_bar.update()
        time.sleep(2)
        self.var.set("Active....") 

    def copy(self):
        self.text_area.event_generate(("<<Copy>>"))
        self.var.set("Copy")
        self.s_bar.update()
        time.sleep(2)
        self.var.set("Active....") 
        
    def paste(self):
        self.text_area.event_generate(("<<Paste>>"))
        self.var.set("Paste")
        self.s_bar.update()
        time.sleep(2)
        self.var.set("Active....") 

    def help(self):
        self.var.set("Helping")
        self.s_bar.update()
        time.sleep(1)
        tkmb.showinfo("Helping User....","For help please contact the developer.")
        self.var.set("Active....") 

    def speak(self):
        self.var.set("Speaking")
        self.s_bar.update()
        time.sleep(1)
        self.var.set("Active....")
        speak(self.text_area.get("1.0", "end-1c"))

    def text_area(self):
        self.text_area = Text(self, font="calibri 15", background="#ECF0F1", foreground="black", relief=FLAT)
        self.text_area.pack(expand=True, fill=BOTH)

    def scroll(self):
        self.Scroll = Scrollbar(self.text_area)
        self.Scroll.pack(side=RIGHT, fill=Y)
        self.Scroll.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.Scroll.set)

    def save(self):
        self.var.set("Saving")
        self.s_bar.update()
        time.sleep(1)
        self.var.set("Active....") 

        filename = pyautogui.prompt("Enter filename : ") 
        text_content = self.text_area.get("1.0", "end-1c")  # Retrieve text from the text area
        with open(f"{filename}.txt", "w") as file:
            file.write(text_content)

    def new(self):
        self.destroy()
        main()
        
    def exit(self):
        self.destroy()

def main():
    speak('hello world')    
    notepad = Gui()
    notepad.title()
    notepad.s_bar()
    notepad.menu()
    notepad.text_area()
    notepad.scroll()
    notepad.mainloop()

main() 