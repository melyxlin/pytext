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
        saves file with latest content. If file is not stored on computer, stores it on computer
    """
    global filename
    if filename == None: #case when file is not stored
        saveFileAs()
    else:
        t = text.get(0.0, END)
        f = open(filename, 'w')
        f.write(t)
        f.close()

def saveFileAs(e=None):
    """
        stores file in a location on the computer
    """
    global filename
    f = asksaveasfile(mode = 'w', defaultextension = '.txt')
    t = text.get(0.0, END)
    try: #error handling
        f.write(t.rstrip()) 
    except: 
        showerror(title = "Error!", message = "Unable to save file.")
    filename = f.name #initiaizes the name of the file

def openFile(e=None):
    """
        opens file
    """
    global filename
    f = askopenfile(mode = 'r')
    t = f.read()
    filename = f.name
    text.delete(0.0, END)
    text.insert(0.0, t)

def closeFile(e=None):
    """
        closes file
    """
    global root
    root.quit()

def undoAction(e=None):
    """
        undos an action
    """
    text.edit_undo()

def redoAction(e = None):
    """
        redos an action
    """
    text.edit_redo()


root = Tk() #main window
root.title("Pytext - a simple python text editor")
root.minsize(width = 400, height = 400)
root.maxsize(width = 400, height = 400)



text = Text(root, width = 400, height = 400, undo = True)
text.pack()

menuBar = Menu(root) #menu bar

fileMenu = Menu(menuBar) #file options
fileMenu.add_command(label = "New", command = newFile, accelerator = "Control-N")
fileMenu.add_command(label = "Open", command = openFile, accelerator = "Control-O")
fileMenu.add_command(label = "Save", command = saveFile, accelerator = "Control-S")
fileMenu.add_command(label = "Save As", command = saveFileAs, accelerator = "Control-Shift-S")
fileMenu.add_separator()
fileMenu.add_command(label = "Quit", command = closeFile, accelerator = "Control-Q")
menuBar.add_cascade(label = "File", menu = fileMenu)

editMenu = Menu(menuBar) #edit options
editMenu.add_command(label = "Undo", command = undoAction, accelerator = "Control-Z")
editMenu.add_command(label = "Redo", command = redoAction, accelerator = "Control-Y")
editMenu.add_separator()
editMenu.add_command(label = "Cut", command=lambda: root.focus_get().event_generate('<<Cut>>'), accelerator = "Control-X")
editMenu.add_command(label = "Copy", command=lambda: root.focus_get().event_generate('<<Copy>>'), accelerator = "Control-C")
editMenu.add_command(label = "Paste", command=lambda: root.focus_get().event_generate('<<Paste>>'), accelerator = "Control-V")
menuBar.add_cascade(label = "Edit", menu = editMenu)

#keyboard shortcuts
root.bind('<Control-q>', closeFile)
root.bind('<Control-s>', saveFile)
root.bind('<Control-o>', openFile)
root.bind('<Control-n>', newFile)
root.bind('<Control-S>', saveFileAs)
root.bind('<Control-z>', undoAction)
root.bind('<Control-y>', redoAction)

root.config(menu = menuBar)
root.mainloop()








 
