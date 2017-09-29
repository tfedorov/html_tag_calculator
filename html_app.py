import tkinter
from tkinter import ttk
from tkinter.constants import INSERT
from tkinter.scrolledtext import ScrolledText

import main_facade as main

root = tkinter.Tk()

text = ttk.Entry()
text.pack()

button = ttk.Button(text="Get", command=lambda: __get_command()).pack()


def _text_update(event):
    current = text.get()
    text.delete(0, len(current))
    text.insert(0, combo.selection_get())


combo = ttk.Combobox(values=main.synonym_keys(), state='readonly')
combo.bind("<<ComboboxSelected>>", _text_update)
combo.pack()

result_text = ScrolledText()
result_text.pack()


def __get_command():
    get_command_result = main.get_command(text.get())
    result_text.insert(INSERT, get_command_result)


root.mainloop()
