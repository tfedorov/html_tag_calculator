import tkinter
from tkinter import ttk
from tkinter.constants import INSERT
from tkinter.scrolledtext import ScrolledText


def launch(main):
    root = tkinter.Tk()

    url_text_ui = ttk.Entry()
    url_text_ui.pack()

    result_text_ui = ScrolledText()
    ttk.Button(text="Load",
               command=lambda: result_text_ui.insert(INSERT, main.get_command(url_text_ui.get()))).pack()

    ttk.Button(text="View from Base",
               command=lambda: result_text_ui.insert(INSERT, main.view_command(url_text_ui.get()))).pack()

    def _text_update(event):
        current = url_text_ui.get()
        url_text_ui.delete(0, len(current))
        url_text_ui.insert(0, synonyms_combo_ui.selection_get())

    synonyms_combo_ui = ttk.Combobox(values=main.synonym_keys(), state='readonly')
    synonyms_combo_ui.bind("<<ComboboxSelected>>", _text_update)
    synonyms_combo_ui.pack()


    result_text_ui.pack()

    root.mainloop()
