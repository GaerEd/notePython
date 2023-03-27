from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

fileName = NONE

def newFile() :
    global fileName
    fileName = "Без названия"
    text.delete(1.0, END)

def saveAs() :
    out = asksaveasfile(mode = "w", defaultextension=".txt")
    data = text.get("1.0", END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Произошла ошибка!", "Нельзя сохранить файл.")

def openFile():
    global fileName
    inp = askopenfile(mode = "r")
    if inp is None:
        return
        fileName = inp.name
    data = inp.read()
    rext.delete("1.0", END)
    text.insert("1.0", data)

root = Tk()
root.title("Заметки")
root.geometry("400x400")

text = Text(root, width=400, height=400)
text.pack()

menuBar = Menu(root)
fileMenu = Menu(menuBar)

fileMenu.add_command(label = "Новый файл", command = newFile)
fileMenu.add_command(label = "Открыть файл", command = openFile)
fileMenu.add_command(label = "Сохранить как", command = saveAs)

menuBar.add_cascade(label = "Файл", menu = fileMenu)

root.config(menu = menuBar)
root.mainloop()