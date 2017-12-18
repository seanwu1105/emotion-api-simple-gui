"""Define the GUI interface."""

from tkinter import Button, Entry, Radiobutton, Tk, Label, LabelFrame, StringVar, N, S, W, E, END
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText
import requests
from matplotlib.image import imread
from PIL import Image
from io import BytesIO
from mpl import ResultImg

class GUIRoot(Tk):
    """The tkinter GUI root class."""
    def __init__(self, thread_cls):
        super().__init__()
        self.thread_cls = thread_cls
        self.filename = None
        self.title("Emotion API")
        self.grid()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(4, weight=1)

        # Create LabelFrames
        lf_key = LabelFrame(self, text="Emotion API Key")
        lf_key.grid(row=0, column=0, columnspan=1, sticky=W+E, padx=5, pady=3)
        lf_key.grid_columnconfigure(0, weight=1)
        lf_mode = LabelFrame(self, text="Mode")
        lf_mode.grid(row=1, column=0, columnspan=1, sticky=W+E, padx=5, pady=3)
        for i in range(2):
            lf_mode.grid_columnconfigure(i, weight=1)
        lf_source = LabelFrame(self, text="Image Source", height=50)
        lf_source.grid(row=2, column=0, columnspan=1, sticky=W+E, padx=5, pady=3)
        lf_source.rowconfigure(0, weight=1)
        lf_source.grid_propagate(False)
        lf_source.columnconfigure(0, weight=1)
        lf_source.columnconfigure(1, weight=5)
        lf_source.columnconfigure(2, weight=1)
        lf_request = LabelFrame(self, text="Request Result")
        lf_request.grid(row=3, column=0, columnspan=1, sticky=W+E, padx=5, pady=3)
        lf_request.grid_columnconfigure(0, weight=1)
        lf_console = LabelFrame(self, text="Console")
        lf_console.grid(row=4, column=0, columnspan=1, sticky=N+S+W+E, padx=5, pady=3)
        lf_console.grid_columnconfigure(0, weight=1)
        lf_console.grid_rowconfigure(0, weight=1)
        lf_img = LabelFrame(self, text="Output Image")
        lf_img.grid(row=0, column=1, rowspan=5, sticky=N+S+W+E)
        lf_img.grid_columnconfigure(0, weight=1)
        lf_img.grid_rowconfigure(0, weight=1)

        # Create Input Fields
        self.ety_key = Entry(lf_key)
        self.ety_key.insert(END, "bfe9b2f471e04b29a8fabfe3dd9f647d")
        self.ety_key.grid(sticky=W+E, padx=3)
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
        self.lb_filename = Label(lf_source, text="..")
        self.btn_fileopen = Button(lf_source, text="Open..", command=self.open_img)
        # URL Image Source
        self.lb_url = Label(lf_source, text="URL")
        self.ety_url = Entry(lf_source)
        self.ety_url.insert(END, "https://i.imgflip.com/qiev6.jpg")
        self.btn_url = Button(lf_source, text="Get Image", command=self.get_img)
        # set default mode: local raw image
        self.var_mode.set('local')
        self.change_mode()
        # request btn
        self.btn_request = Button(lf_request,
                                  text="Request Result",
                                  command=self.run_request,
                                  state='disable')
        self.btn_request.grid(sticky=W+E)

        # Create Output Console
        self.console = ScrolledText(lf_console, state='disable', width=35, bg='gray6', fg='white')
        self.console.grid(sticky=N+S+W+E)

        # Create Output Image
        self.plot = ResultImg(lf_img)
        self.plot.grid(sticky=N+S+W+E)

    def change_mode(self):
        """Change the image source mode."""
        if self.var_mode.get() == 'local':
            self.lb_filename.grid(row=0, column=0, columnspan=2)
            self.btn_fileopen.grid(row=0, column=2)
            self.lb_url.grid_forget()
            self.ety_url.grid_forget()
            self.btn_url.grid_forget()
        else:
            self.lb_filename.grid_forget()
            self.btn_fileopen.grid_forget()
            self.lb_url.grid(row=0, column=0)
            self.ety_url.grid(row=0, column=1, sticky=W+E, padx=3)
            self.btn_url.grid(row=0, column=2)

    def run_request(self):
        """Create the requesting thread to request the result from Emotion API."""
        source = self.filename if self.var_mode.get() == 'local' else self.ety_url.get()
        self.thread_cls(self.ety_key.get(),
                        self.var_mode.get(),
                        source,
                        self.plot,
                        self.print_console).start()

    def open_img(self):
        """Open the dialog let user to choose test file and get the test data."""
        max_name_len = 20
        self.filename = askopenfilename(filetypes=(("JPEG", "*.jpg"),
                                                   ("PNG", "*.png"),
                                                   ("All Files", "*.*")),
                                        title="Choose an Image")
        if self.filename:
            self.plot.imshow(imread(self.filename))
            self.print_console("Open a local raw image file.")
            self.btn_request.config(state='normal')
            if len(self.filename) > max_name_len:
                self.lb_filename.config(text=".."+self.filename[-max_name_len:])
            else:
                self.lb_filename.config(text=self.filename)

    def get_img(self):
        """Get the image from the given URL."""
        try:
            self.plot.imshow(Image.open(BytesIO(requests.get(self.ety_url.get()).content)))
        except Exception as e:
            self.print_console(e.args)
        else:
            self.print_console("Open a online image from URL.")
            self.btn_request.config(state='normal')

    def print_console(self, input_str):
        """Print the text on the conolse."""
        self.console.config(state='normal')
        self.console.insert(END, "{}\n".format(input_str))
        self.console.config(state='disable')
        self.console.see(END)
