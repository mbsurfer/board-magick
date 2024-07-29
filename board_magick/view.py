import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from dataclasses import dataclass
from typing import Optional


class BoardMagickView(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")

        self.title("Board Magick")
        self.geometry("1200x800")
        self.iconphoto(False, tk.PhotoImage(file="icon32x32.png"))

        self.buttons_frame = None
        self.buttons = {}
        self.create_button_frame()

    def create_button_frame(self):
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(fill=X, pady=20, padx=20)
        button_padding = 10

        self.buttons['select_dir'] = ttk.Button(self.buttons_frame, text="Select Folder", style=PRIMARY)
        self.buttons['select_dir'].grid(row=0, column=0, padx=(0, button_padding))

        self.buttons['create_boards'] = ttk.Button(self.buttons_frame, text="Create Boards", style=SUCCESS,
                                                   state=DISABLED)
        self.buttons['create_boards'].grid(row=0, column=1, padx=(0, button_padding))

        self.buttons['stop'] = ttk.Button(self.buttons_frame, text="Stop", style=DANGER, state=DISABLED)
        self.buttons['stop'].grid(row=0, column=2, padx=(0, button_padding))

        self.buttons['open'] = ttk.Button(self.buttons_frame, text="Open Boards", style=PRIMARY, state=DISABLED)
        self.buttons['open'].grid(row=0, column=3, padx=(0, button_padding))

        # Right Aligned Buttons
        self.buttons_frame.grid_columnconfigure(4, weight=1)

        self.buttons['open'] = ttk.Button(self.buttons_frame, text="Reset", style=DANGER)
        self.buttons['open'].grid(row=0, column=4, padx=(0, button_padding), sticky=E)
