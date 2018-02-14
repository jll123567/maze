import tkinter as tk
from tkinter import ttk

NORM_FONT = ("Verdana", 12)


def popupmsg(msg):
    popup = tk.Tk()
    sw = popup.winfo_screenwidth()
    sh = popup.winfo_screenheight()
    popup.wm_title("!")
    # centering help from <https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
    # /14912644>
    popup.geometry('%dx%d+%d+%d' % (100, 80, ((sw / 2) - 50), ((sh / 2) - 40)))
    label = ttk.Label(popup, text=str(msg), font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    b1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    b1.pack()

    popup.mainloop()


popupmsg("testing")
