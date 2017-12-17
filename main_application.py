"""The simple GUI application for Microsoft Emotion API as
   an example for final project in NCU CSIE Neural Network, Taiwan (2017).
   Author: Sean Wu (104502551)
"""

from gui import GUIRoot
from request_emotion import RequestEmotion

def main():
    """The main function."""
    gui_root = GUIRoot(RequestEmotion)
    gui_root.mainloop()

if __name__ == '__main__':
    main()
