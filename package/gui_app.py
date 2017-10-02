import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.constants import INSERT
from tkinter.scrolledtext import ScrolledText


def launch(main):
    root = tkinter.Tk()

    def _build_label(text):
        Label(root, text=text, wraplength=200).pack(anchor=tkinter.W)

    def _build_combo_synonyms():
        def _text_update(_):
            current = url_ui.get()
            url_ui.delete(0, len(current))
            url_ui.insert(0, synonyms_combo_ui.selection_get())

        synonyms_combo_ui = ttk.Combobox(values=main.synonym_keys(), state='readonly')
        synonyms_combo_ui.bind("<<ComboboxSelected>>", _text_update)
        synonyms_combo_ui.pack()

    def _build_button(button_text, result_extractor):
        def _on_click_action(_):
            _current_url_text = url_ui.get()
            result_ui.insert(INSERT, result_extractor(_current_url_text))

        load_button_ui = ttk.Button(text=button_text)
        load_button_ui.bind('<Button-1>', _on_click_action)
        load_button_ui.pack()

    _build_label("Url to calculate Tag:")

    url_ui = ttk.Entry()
    url_ui.pack()

    _build_button("Load", lambda url: main.get_command(url))

    _build_button("View from Base", lambda url: main.view_command(url))

    _build_label("List of synonyms:")

    _build_combo_synonyms()

    _build_label("Result calculation:")

    result_ui = ScrolledText()
    result_ui.pack()

    root.mainloop()
