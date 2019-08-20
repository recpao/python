from tkinter import *  # Python 3

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="Esci", fg="red", command=master.destroy)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Ciao a tutti!", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("Ciao a tutti!")

root = Tk()
app = App(root)
root.mainloop()