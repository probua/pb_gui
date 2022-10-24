import pygame
import webbrowser
from tkinter import *
from PIL import Image as PIL_Image

from cfg import init_variables as iv
from src.functions.path_resources import resources
from src.windows import settings as win_settings


def init():

    root = Tk()
    root.title("PB_GUI") # Title
    root.geometry("500x500") # Resolution
    root.resizable(False, False)
    icon = PhotoImage(file = resources("probua.png")) # Icon
    root.iconphoto(False, icon)

    def play_music():
        pygame.mixer.music.load(resources("nggyu.mp3"))
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(loops=0)

    def stop_music():
        pygame.mixer.music.stop()

    gif_img = PIL_Image.open(resources("nggyu.gif"))
    frames = gif_img.n_frames
    im = [PhotoImage(file = resources("nggyu.gif"), format=f"gif -index {i}") for i in range(frames)]

    def play_gif(count):
        im2 = im[count]
        gif_label.config(image=im2)
        count += 1
        if count == frames: count = 0
        root.after(80, lambda: play_gif(count))

    def gen_button_on_pressed():
        gen_link = f"{iv.url}?field1={iv.field1}&field2={iv.field2}"
        link_label['text'] = gen_link

        link_copy_button["state"] = NORMAL
        open_browser_button["state"] = NORMAL

    def link_copy_button_on_pressed():
        root.clipboard_clear()
        root.clipboard_append(link_label['text'])

    def open_browser_button_on_pressed():
        webbrowser.open_new_tab(link_label['text'])
        open_browser_button["state"] = DISABLED

    # Frames
    main_frame = Frame(root)
    music_frame = Frame(main_frame)
    music_options_frame = Frame(music_frame)
    gen_frame = Frame(main_frame)
    link_frame = Frame(main_frame)

    # Elements
    settings_button = Button(main_frame, text = "Settings", command = win_settings.init, font = iv.font)
    gif_label = Label(music_frame)
    play_music_button = Button(music_options_frame, text = "Play Music", command = play_music, font = iv.font)
    stop_music_button = Button(music_options_frame, text = "Stop Music", command = stop_music, font = iv.font)
    footer_label = Label(main_frame, text = iv.footer, font = iv.font)

    gen_button = Button(main_frame, text = "Generate", command = lambda: gen_button_on_pressed(), font = iv.font)
    link_label = Label(link_frame, bg = "white", text = "Generated Link", font = iv.font)
    link_copy_button = Button(link_frame, text = "Copy", command = link_copy_button_on_pressed, font = iv.font)
    open_browser_button = Button(main_frame, text = "Open in browser", command = open_browser_button_on_pressed, font = iv.font)

    # GUI
    main_frame.pack(padx=15, pady=15)

    music_frame.pack()
    music_options_frame.pack(fill=X, expand=True)

    play_music_button.pack(side=LEFT, fill = X, expand = True)
    stop_music_button.pack(side=RIGHT, fill = X, expand = True)
    gif_label.pack(fill=X, expand=True)
    gen_frame.pack(fill=X, expand=True)
    gen_button.pack(fill=X, expand=True)

    settings_button.pack(fill = X, expand = True)

    link_frame.pack(fill=X, expand=True)
    link_label.pack(padx=1, side=LEFT)
    link_label.config(width=68)
    link_copy_button.pack(side=RIGHT, fill=X, expand=True)

    open_browser_button.pack(fill = X, expand = True)
    link_copy_button["state"] = DISABLED
    open_browser_button["state"] = DISABLED

    footer_label.pack(fill = X, expand = True)

    play_music()
    play_gif(0)
    root.mainloop()