"""Define the thread of requesting the result from Emotion API."""

from threading import Thread
import cv2
import numpy as np

class RequestEmotion(Thread):
    """The class to request result from Emotion API."""
    def __init__(self, key, mode, source, plot, print_func):
        """Parameters
        ----------

        * key : (str)
            The key for Emotion API.

        * mode : (str)
            `local` for local raw image and `url` for URL online image.

        * source : (str)
            The link to the source (for either local or URL online).

        * plot : (ResultImg)
            The object of ResultImg to render result image.

        * print_func : (func)
            The function to print additional info.
        """
        super().__init__()
        self.key = key
        self.mode = mode
        self.source = source
        self.plot = plot
        self.print = print_func
    def run(self):
        with open('Group2016.jpg', 'rb') as f:
            data = f.read()
        data8uint = np.fromstring(data, np.uint8) # Convert string to an unsigned int array
        img = cv2.cvtColor(cv2.imdecode(data8uint, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
        self.plot.imshow(img)
        self.print("FUCK!")
