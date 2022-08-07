import tkinter as tk
from tkinter import *
import pyshorteners
import pyperclip

win = tk.Tk()
win.title("IC URL Shorter")
win.geometry("170x250")
win.iconbitmap("icon.ico")
win.resizable(False, False)

def copy_url():
    pyperclip.copy(short_url.get())

def url_short():
    link = url.get()

    s = pyshorteners.Shortener().tinyurl.short(link)

    short_url.insert(0, s)

url_name = Label(text = "Url address")
url_name.place(relx = .5, rely = .1, anchor = "c")

url = StringVar()
url_entry = Entry(textvariable = url)
url_entry.place(relx = .5, rely = .17, anchor = "c")

short_url_text = Label(text = "Url short")
short_url_text.place(relx = .5, rely = .27, anchor = "c")

short = StringVar()
short_url = Entry(textvariable = short)
short_url.place(relx = .5, rely = .35, anchor = "c")

short_click = Button(text = "Short URL", command = url_short)
short_click.place(relx = .5, rely = .7, anchor = "c")

copy_click = Button(text = "Copy url", command = copy_url)
copy_click.place(relx = .5, rely = .85, anchor = "c")

win.mainloop()