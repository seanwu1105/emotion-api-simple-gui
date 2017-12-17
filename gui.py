"""Define the GUI interface."""

from tkinter import Button, Entry, Radiobutton, Tk, Label, LabelFrame, StringVar, N, S, W, E
from tkinter.scrolledtext import ScrolledText

class GUIRoot(Tk):
    """The tkinter GUI root class."""
    def __init__(self):
        super().__init__()
        self.title("Emotion API")
        self.grid()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(3, weight=1)

        # Create LabelFrames
        lf_key = LabelFrame(self, text="Key")
        lf_key.grid(row=0, column=0, columnspan=1, sticky=W+E, padx=5, pady=3)
        lf_key.grid_columnconfigure(0, weight=1)
        lf_mode = LabelFrame(self, text="Mode")
        lf_mode.grid(row=1, column=0, columnspan=1, sticky=W+E, padx=5, pady=3)
        for i in range(2):
            lf_mode.grid_columnconfigure(i, weight=1)
        self.lf_source = LabelFrame(self, text="Image Source", height=50)
        self.lf_source.grid(row=2, column=0, columnspan=1, sticky=W+E, padx=5, pady=3)
        self.lf_source.rowconfigure(0, weight=1)
        self.lf_source.grid_propagate(False)
        lf_console = LabelFrame(self, text="Console")
        lf_console.grid(row=3, column=0, columnspan=1, sticky=N+S+W+E, padx=5, pady=3)
        lf_console.grid_columnconfigure(0, weight=1)
        lf_console.grid_rowconfigure(0, weight=1)
        lf_img = LabelFrame(self, text="Output Image")
        lf_img.grid(row=0, column=2, rowspan=2)

        # Create Input Fields
        ety_key = Entry(lf_key)
        ety_key.grid(sticky=W+E)
        self.var_mode = StringVar()
        Radiobutton(lf_mode,
                    text="Local Image",
                    variable=self.var_mode,
                    value='local',
                    command=self.change_mode).grid(row=1, column=0)
        Radiobutton(lf_mode,
                    text="URL Image",
                    variable=self.var_mode,
                    value='url',
                    command=self.change_mode).grid(row=1, column=1)
        # Local Image Source
        self.lb_filename = Label(self.lf_source, text="..")
        self.btn_fileopen = Button(self.lf_source, text="Open..")
        # URL Image Source
        self.lb_url = Label(self.lf_source, text="URL")
        self.ety_url = Entry(self.lf_source)
        # set default mode: local raw image
        self.var_mode.set('local')
        self.change_mode()

        # Create Output Console
        console = ScrolledText(lf_console, state='disable', width=30)
        console.grid(sticky=N+S+W+E)

    def change_mode(self):
        """Change the image source mode."""
        if self.var_mode.get() == 'local':
            self.lf_source.columnconfigure(0, weight=6)
            self.lf_source.columnconfigure(1, weight=1)
            self.lb_filename.grid(row=0, column=0)
            self.btn_fileopen.grid(row=0, column=1)
            self.lb_url.grid_forget()
            self.ety_url.grid_forget()
        else:
            self.lf_source.columnconfigure(0, weight=1)
            self.lf_source.columnconfigure(1, weight=3)
            self.lb_filename.grid_forget()
            self.btn_fileopen.grid_forget()
            self.lb_url.grid(row=0, column=0)
            self.ety_url.grid(row=0, column=1, sticky=W+E)
