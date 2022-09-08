import tkinter as tk
from tkinter import ttk

class invoiceGUI():
    def __init__(self,master):
        self.invoiceScreen = tk.Toplevel(height=600,width=1200)
        self.invoiceScreen.title("Create a new invoice")
        self.invoiceScreen.iconbitmap("i01_yaki logo.ico")



class AllGUI(tk.Tk):
    def __init__(self):
        super(AllGUI, self).__init__()
        self.title("Yaki Food Software.")
        self.iconbitmap("i01_yaki logo.ico")
        self.mainFrame = tk.Frame(self,width=1200,height=600)
        self.mainFrame.pack()
        self.invoiceButton = tk.Button(self.mainFrame,text="Invoice",width=30,height=5,command=self.invoiceCommand)
        self.invoiceButton.place(x=100,y=100)
    def invoiceCommand(self):
        for i in locals():
            print(i)
        self.invoiceScreen = invoiceGUI(self)




if __name__ == "__main__":
    gui = AllGUI()
    gui.mainloop()
