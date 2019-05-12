from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

filename = None

def newFile(e=None): 
    """
        creates a new file
    """
    global filename
    filename = "Untitled" #initial name of file
    text.delete(0.0, END) #main empty text box

def saveFile(e=None):
    """ 
        saves file
    """
    global filename
    if filename == None: 
        saveFileAs()
    else:
        t = text.get(0.0, END)
        f = open(filename, 'w')
        f.write(t)
        f.close()

def saveFileAs(e=None):
    global filename
    f = asksaveasfile(mode = 'w', defaultextension = '.txt')
    filename = f.name
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip()) 
    except:
        showerror(title = "Error!", message = "Unable to save file.")

def openFile(e=None):
    global filename
    f = askopenfile(mode = 'r')
    t = f.read()
    filename = f.name
    text.delete(0.0, END)
    text.insert(0.0, t)

def closeFile(e=None):
    global root
    root.quit()

root = Tk() #main window
root.title("Pytext - a simple python text editor")
root.bind('<Control-q>', closeFile)
root.bind('<Control-s>', saveFile)
root.bind('<Control-o>', openFile)
root.bind('<Control-n>', newFile)
root.bind('<Control-S>', saveFileAs)
root.minsize(width = 400, height = 400)
root.maxsize(width = 400, height = 400)

text = Text(root, width = 400, height = 400)
text.pack()

menuBar = Menu(root) #menu bar

filemenu = Menu(menuBar) #file options
filemenu.add_command(label = "New", command = newFile)
filemenu.add_command(label = "Open", command = openFile)
filemenu.add_command(label = "Save", command = saveFile)
filemenu.add_command(label = "Save As", command = saveFileAs)
filemenu.add_separator()
filemenu.add_command(label = "Quit", command = closeFile)
menuBar.add_cascade(label = "File", menu = filemenu)


root.config(menu = menuBar)
root.mainloop()








 
