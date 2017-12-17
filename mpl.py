"""Define the matplotlib to show the result image, which is embedded in tkinter GUI."""

from tkinter import Frame, BOTH
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ResultImg(Frame):
    """The class creating result image."""
    def __init__(self, master=None):
        super().__init__(master)
        fig = Figure(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)
        self.ax = fig.add_subplot(1, 1, 1) # the main axis

    def imshow(self, img):
        """Show the image on the main axis."""
        self.ax.imshow(img)
        self.canvas.show()
