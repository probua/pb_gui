from tkinter import *
from cfg import init_variables
from src.functions.path_resources import resources

def init():

    icon = PhotoImage(file = resources("probua.png")) # Icon

    settings = Toplevel()
    settings.title("Settings")
    settings.geometry("300x200")
    settings.resizable(False, False)
    settings.iconphoto(False, icon)

    def apply_settings():
        init_variables.url = url_box.get()
        init_variables.field1 = field1_box.get()
        init_variables.field2 = field2_box.get()

    def accept_settings():
        apply_settings()
        settings.destroy()

    def restore_settings():
        url_box.delete(0, len(url_box.get()))
        field1_box.delete(0, len(field1_box.get()))
        field2_box.delete(0, len(field2_box.get()))

        url_box.insert(0, init_variables.DEFAULT_URL)
        field1_box.insert(0, init_variables.DEFAULT_FIELD1)
        field2_box.insert(0, init_variables.DEFAULT_FIELD2)

    options_frame = Frame(settings)
    op_url_frame = Frame(options_frame)
    op_field1_frame = Frame(options_frame)
    op_field2_frame = Frame(options_frame)
    op_buttons_frame = Frame(options_frame)

    #Link Options
    url_label = Label(op_url_frame, text = "url: ", font = init_variables.font)
    url_box = Entry(op_url_frame, font = init_variables.font)
    url_box.insert(0, init_variables.url)

    field1_label = Label(op_field1_frame, text = "field1: ", font = init_variables.font)
    field1_box = Entry(op_field1_frame, font = init_variables.font)
    field1_box.insert(0, init_variables.field1)

    field2_label = Label(op_field2_frame, text = "field2: ", font = init_variables.font)
    field2_box = Entry(op_field2_frame, font = init_variables.font)
    field2_box.insert(0, init_variables.field2)

    default_button = Button(op_buttons_frame, text = "Restore", command = restore_settings, font = init_variables.font)
    apply_button = Button(op_buttons_frame, text = "Apply", command = apply_settings, font = init_variables.font)
    accept_button = Button(op_buttons_frame, text = "Accept", command = accept_settings, font = init_variables.font)

    options_frame.pack(padx=15, pady=15, fill=X, expand=True)

    op_url_frame.pack(fill=X, expand=True)
    op_field1_frame.pack(fill=X, expand=True)
    op_field2_frame.pack(fill=X, expand=True)
    op_buttons_frame.pack(fill=X, expand=True)

    field1_label.pack(side=LEFT, fill = X, expand = False)
    field1_box.pack(side=RIGHT, fill = X, expand = True)
    field2_label.pack(side=LEFT, fill = X, expand = False)
    field2_box.pack(side=RIGHT, fill = X, expand = True)

    url_label.pack(side=LEFT, fill = X, expand = False)
    url_box.pack(side=RIGHT, fill = X, expand = True)

    default_button.pack(side=LEFT, fill = X, expand = True)
    apply_button.pack(side=LEFT, fill = X, expand = True)
    accept_button.pack(side=LEFT, fill = X, expand = True)