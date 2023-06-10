import os.path
from tkinter import Tk, PhotoImage

current_dir = os.path.dirname(__file__)

root = Tk()
root.title("Desktop Entry Maker")
root.iconphoto(True, PhotoImage(file=f"{current_dir}/assets/icon48x48.png"))

root.mainloop()
