import tkinter as tk
from tkinter import *
from tkinter import ttk

#esto es robado si? sufri mucho agregando el scrollbar :(((((
class Frame_scroll(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self, height=500, width=1000)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, padx=50, pady=15)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side = RIGHT, fill = Y ) #self 
    
    def clear(self): #este es mio
        limpiar_frame(self.scrollable_frame)

#limpiar frames (por si acaso jsjs)
def elimnar_frame(Frame):
    Frame.destroy()

def limpiar_frame(frame):
   for w in frame.winfo_children():
      w.destroy()