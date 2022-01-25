import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title('OneTap')
root.iconbitmap('D:\My CS Projects\OneTap\laptop_computer_icon.ico')
apps = []


def addApps():
    filename = filedialog.askopenfilename(initialdir='/', title="Add your application",
                                          filetypes=(('Applications', '*.exe'), ('All files', '*.*')))

    if filename not in apps and filename != '':
        apps.append(filename)
    else:
        tk.messagebox.showwarning("Warning",
                                  "App already exists. Please try again.")

    reload()


def runApps():
    if apps == []:
        tk.messagebox.showwarning("Empty app list",
                                  "The app list is empty. Please add apps to proceed")
    else:
        for app in apps:
            os.startfile(app)

def removeApp(app):
    apps.remove(app)
    reload()

def load():   #Load the app_list frame
    i = 0
    for app in apps:
        label = tk.Label(app_list, text=app)
        label.grid(row=i, column=0)
        removeButt = tk.Button(app_list, text='Remove', bg='#22b4b7',
                               activebackground='grey', command=lambda x=app: removeApp(x))
        removeButt.grid(row=i, column=1, pady=5)
        i += 1

def reload():  #Reload the app_list frame.
    for widget in app_list.winfo_children():
        widget.destroy()
        
    load()

canvas = tk.Canvas(root, height=600, width=600, bg='#22b4b7')
canvas.pack()

app_list = tk.Frame(root, bg='white')
app_list.place(height=480, width=480, relx=0.1, rely=0.1)

selectApps = tk.Button(root, text='Select Apps', bg='#22b4b7',
                       command=addApps, activebackground='grey')
selectApps.pack(pady=5)
openApps = tk.Button(root, text='Open Apps', bg='#22b4b7',
                     command=runApps, activebackground='grey')
openApps.pack(pady=5)
exitProgram = tk.Button(root, text='Exit Program', bg='#22b4b7',
                        command=root.quit, activebackground='grey')
exitProgram.pack(pady=5)

if os.path.isfile('saved_apps.txt'):

    with open('saved_apps.txt', 'r') as file:
        temp = file.read()
        temp = temp.split(',')
        apps = temp
        apps.pop()  # Remove the empty string

    load()

root.mainloop()

with open('saved_apps.txt', 'w') as file:
    for app in apps:
        if app != '':
            file.write(app + ',')
