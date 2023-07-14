# Imports necessary modules
import tkinter as tk
from tkinter import *
import webbrowser

# create ParentWindow via Tkinter
class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")

# Use of tk.Label for placing instructions on how to use application
        self.lbl_instruction = tk.Label(self.master, text="Enter custom text or click the Default HTML page button.")
        self.lbl_instruction.grid(row=0, column=0,padx=(10,0), pady=(10,0), sticky=N+W)

# Use of tk.Entry to create an area for users to enter content to place in HTML body
        self.txt_customText = tk.Entry(self.master,text='')
        self.txt_customText.grid(row=1,column=0,columnspan=3,padx=(10,10), pady=(10,0), sticky=N+E+S+W)

# Button to activate function to Place in default text as body in HTML page
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1, padx=(10,10), pady=(10,10))

#Button to activate function to grab content from user entry and place text as body in HTML page
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=2, column=2, padx=(10,10), pady=(10,10))

# Default HTML from assignment instructions
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<hl>" + htmlText + "</hl>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

# Modified instructions to grad content from tk.Entry above, using get()
    def customHTML(self):
        customText = self.txt_customText.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<hl>" + customText + "</hl>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")




if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
