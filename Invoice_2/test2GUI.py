import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
class nothingness(tk.Tk):
    def __init__(self):
        super(nothingness, self).__init__()

        self.sqlShit()


        self.geometry('1200x500')
        self.configure(background='#BFEFFF')
        self.title('Invoice Window')

        #self.place(self.master,x=0,y=0)
        # This is the section of code which creates a text input box
        self.date = tk.Entry(self)
        self.date.place(x=100, y=25)

        # This is the section of code which creates the a tk.Label
        tk.Label(self, text='Date :', bg='#BFEFFF', font=('arial', 12, 'normal')).place(x=50, y=25)

        # This is the section of code which creates the a tk.Label
        tk.Label(self, text='Invoice To :', bg='#BFEFFF', font=('verdana', 12, 'normal')).place(x=50, y=50)

        # This is the section of code which creates the a tk.Label
        tk.Label(self, text='Invoice No. :', bg='#BFEFFF', font=('verdana', 12, 'normal')).place(x=550, y=25)

        # This is the section of code which creates a text input box
        self.invoiceNo = tk.Entry(self)
        self.invoiceNo.place(x=700, y=25)

        # This is the section of code which creates the a tk.Label
        tk.Label(self, text='Due Date :', bg='#BFEFFF', font=('verdana', 12, 'normal')).place(x=300, y=25)

        # This is the section of code which creates a text input box
        self.dueDate = tk.Entry(self)
        self.dueDate.place(x=400, y=25)

        # This is the section of code which creates the a tk.Label
        tk.Label(self, text='Project Code :', bg='#BFEFFF', font=('verdana', 12, 'normal')).place(x=550, y=50)

        # This is the section of code which creates a text input box
        self.projectCode = tk.Entry(self)
        self.projectCode.place(x=700, y=50)

        # This is the section of code which creates the a tk.Label
        tk.Label(self, text='Place of Supply :', bg='#BFEFFF', font=('verdana', 12, 'normal')).place(x=550, y=75)

        # This is the section of code which creates a text input box
        self.placeOfSupply = tk.Entry(self)
        self.placeOfSupply.place(x=700, y=75)

        self.invoiceTo = tk.Text(self,wrap=tk.CHAR)
        self.invoiceTo.place(x=160,y=50,width=380,height=100)
        invoiceToFont = ("Times new Roman", 15)
        self.invoiceTo.configure(font=invoiceToFont)

        self.MiddleFramesFrame = tk.Frame(master = self,height = 300,width=1000)
        self.MiddleFramesFrame.place(x=25,y=175)

        self.middleBillingTable()
        #self.frame_middle_billing = ScrolledWindow(parent = self.MiddleFramesFrame,canv_h=300,canv_w=1000)
        #self.frame_middle_billing.place(x=0,y=111110)

        self.latestBillingRow = 1


    def invoiceNo(self):
        try:
            with open(""):
                pass
        except:
            pass
    def sqlShit(self):

        self.conn = sqlite3.connect("HPG.db")
        self.cur = self.conn.cursor()

    def middleBillingTable(self):
        try:
            self.tableCanvas
        except:
            self.tableCanvas = tk.Canvas(self.MiddleFramesFrame, bg="white")
            self.tableCanvas.place(x=0, y=0, width=1000, height=300)

            self.addItem = ttk.Button(self.tableCanvas, text="Add Item", command=self.addItemClicked, width=50)
            self.editItem = ttk.Button(self.tableCanvas, text="Edit Item", command=self.editItemClicked, width=50)
            self.deleteItem = ttk.Button(self.tableCanvas, text="Delete Item", command=self.deleteItemClicked,
                                         width=50)
            self.addItemRow = 2
            self.tableItemDataCanvasHeight = 25
            self.tableItemDataCanvas = tk.Canvas(self.tableCanvas, bg="white", width=1000,
                                                  height=self.tableItemDataCanvasHeight)
            self.refreshTable()

    def refreshTable(self):
        for child in self.tableItemDataCanvas.winfo_children():
            child.destroy()

        x = 5

        for rowNames in ["SNO", "PRODUCT NAME","RATE","QUANTITY","AMOUNT"]:
            tk.Label(self.tableItemDataCanvas, text=str(rowNames)).place(x=x, y=5)
            x += 150
        y = 25
        self.tableItemDataCanvasHeight = 25
        try:
            for rowData in self.cur.execute("SELECT * FROM STOCKMASTER"):
                x = 5
                for value in rowData:
                    tk.Label(self.tableItemDataCanvas, text=str(value)).place(x=x, y=y)
                    x += 150
                y += 30
                self.tableItemDataCanvasHeight += 30
        except:
            print("errored")
        self.tableItemDataCanvas.grid(row=1, columnspan=4)
        self.addItem.grid(row=self.addItemRow, column=1)
        self.editItem.grid(row=self.addItemRow, column=2)
        self.deleteItem.grid(row=self.addItemRow, column=3)
        self.tableItemDataCanvas["height"] = self.tableItemDataCanvasHeight

    def addItemClicked(self):

        self.addItemWindow = tk.Toplevel(self.tableCanvas)
        self.addItemWindow.title("Add item")
        self.addItemWindow.geometry("300x210")

        tk.Label(self.addItemWindow, text="Product Desc.").place(x=20, y=30)
        self.addItemEntryDesc = tk.Entry(self.addItemWindow)
        self.addItemEntryDesc.place(x=125, y=30)

        tk.Label(self.addItemWindow, text="Rate").place(x=20, y=60)
        self.addItemEntryRate = tk.Entry(self.addItemWindow)
        self.addItemEntryRate.place(x=125, y=60)

        tk.Label(self.addItemWindow, text="Quantity").place(x=20, y=90)
        self.addItemEntryQuantity = tk.Entry(self.addItemWindow)
        self.addItemEntryQuantity.place(x=125, y=90)

        tk.Label(self.addItemWindow, text="Amount").place(x=20, y=120)
        self.addItemEntryAmount= tk.Entry(self.addItemWindow,state="disabled")
        self.addItemEntryAmount.place(x=125, y=120)

        self.addItemButton = ttk.Button(self.addItemWindow, text="Add item", command=self.addItemCommand)
        self.addItemButton.place(x=200, y=175)
    def editItemClicked(self):
        pass
    def deleteItemClicked(self):
        pass

    def addItemCommand(self):
        if self.addItemEntryAmount.get() == "":
            self.addItemEntryAmount.configure(state="normal")
            self.addItemEntryAmount.insert(tk.END,int(self.addItemEntryRate.get()) * int(self.addItemEntryQuantity.get()))
        entries = [self.addItemEntryDesc, self.addItemEntryRate, self.addItemEntryQuantity,
                   self.addItemEntryAmount]
        entryData = [i.get() for i in entries]
        values = []
        for i in entries:
            value = i.get()
            values.append(value)
        messagebox.showinfo("Entry added!", "The entry was added.")
        self.addItemWindow.destroy()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS 
        STOCKMASTER (SNO INT,PRODUCT_DESC VARCHAR,RATE INT,QUANTITY INT,AMOUNT DOUBLE);""")
        try:
            res = self.cur.execute("""SELECT * FROM STOCKMASTER ORDER BY SNO DESC LIMIT 1""")
            var1 = []
            for i in res:
                var1.append(i)
            self.masterSNo = var1[0][0] + 1
            print(self.masterSNo, 1)
        except Exception as e:
            print(e)
            self.masterSNo = 1
        self.cur.execute("""INSERT INTO STOCKMASTER VALUES (?,?,?,?,?)""", (self.masterSNo,) + tuple(entryData))
        self.conn.commit()
        self.refreshTable()


    def invoiceToSet(self):

        if len(self.invoiceTo.get('1.0',tk.END)) > 100:

            text = self.invoiceTo.get('1.0',tk.END)
            self.invoiceTo.delete('1.0',tk.END)
            self.invoiceTo.insert('1.0',text)

    def table(self,i):

        var1 = "self.text_" + str(
            i) + "_1 = tk.Text(master = self.frame_middle_billing,width = 15,height = 1,state = \"disabled\")"
        var2 = "self.text_" + str(i) + "_1.place(y = " + str((i) * 20) + ",x = 10)"
        exec(var1)
        exec(var2)

        var1 = "self.entry_" + str(
            i) + "_2 = tk.Entry(master = self.frame_middle_billing,width = 50,state = \"disabled\")"
        var2 = "self.entry_" + str(i) + "_2.place(y = " + str((i) * 20) + ",x = 105)"
        exec(var1)
        exec(var2)

        var1 = "self.entry_" + str(
            i) + "_3 = tk.Entry(master = self.frame_middle_billing,width = 15,state = \"disabled\")"
        var2 = "self.entry_" + str(i) + "_3.place(y = " + str((i) * 20) + ",x = 410)"
        exec(var1)
        exec(var2)

        var1 = "self.entry_" + str(
            i) + "_4 = tk.Entry(master = self.frame_middle_billing,width = 15,state = \"disabled\")"
        var2 = "self.entry_" + str(i) + "_4.place(y = " + str((i) * 20) + ",x = 505)"
        exec(var1)
        exec(var2)

        var1 = "self.text_" + str(
            i) + "_5 = tk.Text(master = self.frame_middle_billing,width = 15,height = 1,state = \"disabled\")"
        var2 = "self.text_" + str(i) + "_5.place(y = " + str((i) * 20) + ",x = 600)"
        exec(var1)
        exec(var2)

    def billing_entry_enabler(self):
        # latest = "self.entry_"+str(self.latest_billing_row)+ "_
        for i in range(2, 5):
            latest = "self.entry_" + str(self.latest_billing_row) + "_" + str(i) + ".configure(state = 'normal')"
            exec(latest)

class ScrolledWindow(tk.Frame):
    """
    1. Master widget gets scrollbars and a canvas. Scrollbars are connected
    to canvas scrollregion.

    2. self.scrollwindow is created and inserted into canvas

    Usage Guideline:
    Assign any widgets as children of <ScrolledWindow instance>.scrollwindow
    to get them inserted into canvas

    __init__(self, parent, canv_w = 400, canv_h = 400, *args, **kwargs)
    docstring:
    Parent = master of scrolled window
    canv_w - width of canvas
    canv_h - height of canvas

    """


    def __init__(self, parent, canv_w = 400, canv_h = 400, *args, **kwargs):
        """Parent = master of scrolled window
        canv_w - width of canvas
        canv_h - height of canvas

       """
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.s = ttk.Style()
        self.s.configure('TFrame', background='green')
        # creating a scrollbars
        self.xscrlbr = ttk.Scrollbar(self.parent, orient = 'horizontal')
        #self.xscrlbr.grid(column = 0, row = 1, sticky = 'ew', columnspan = 2)

        self.xscrlbr.place(x=0,y=self.parent.winfo_reqheight() - 20)
        #self.xscrlbr.pack(fill=tk.Y,expand=1,side=tk.RIGHT)
        self.yscrlbr = ttk.Scrollbar(self.parent)
        #self.yscrlbr.grid(column = 1, row = 0, sticky = 'ns')
        self.yscrlbr.place(x=self.parent.winfo_reqwidth() - 20,y=0)
        # creating a canvas
        self.canv = tk.Canvas(self.parent)
        self.canv.config(relief = 'flat',
                         width = canv_w,
                         heigh = canv_h,
                         bd = 2,
                         bg = "white")
        # placing a canvas into frame
        #self.canv.grid(column = 0, row = 0, sticky = 'nsew')
        self.canv.place(x=0,y=0)
        # accociating scrollbar comands to canvas scroling
        self.xscrlbr.config(command = self.canv.xview)
        self.yscrlbr.config(command = self.canv.yview)

        # creating a frame to inserto to canvas
        self.scrollwindow = ttk.Frame(self.parent,height=canv_h - 20,width=canv_w - 20,style="")

        self.canv.create_window(0, 0, window = self.scrollwindow, anchor = 'nw')

        self.canv.config(xscrollcommand = self.xscrlbr.set,
                         yscrollcommand = self.yscrlbr.set,
                         scrollregion = self.canv.bbox("all"))

        self.yscrlbr.lift(self.scrollwindow)
        self.xscrlbr.lift(self.scrollwindow)
        self.scrollwindow.bind('<Configure>', self._configure_window)
        self.scrollwindow.bind('<Enter>', self._bound_to_mousewheel)
        self.scrollwindow.bind('<Leave>', self._unbound_to_mousewheel)

        return

    def _bound_to_mousewheel(self, event):
        self.canv.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canv.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canv.yview_scroll(int(-1*(event.delta/120)), "units")

    def _configure_window(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.scrollwindow.winfo_reqwidth(), self.scrollwindow.winfo_reqheight())
        self.canv.config(scrollregion='0 0 %s %s' % size)
        if self.scrollwindow.winfo_reqwidth() != self.canv.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canv.config(width = self.scrollwindow.winfo_reqwidth())
        if self.scrollwindow.winfo_reqheight() != self.canv.winfo_height():
            # update the canvas's width to fit the inner frame
            self.canv.config(height = self.scrollwindow.winfo_reqheight())


if __name__ == "__main__":
    b = nothingness()
    b.mainloop()
