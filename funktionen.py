from tkinter import *
from tkinter import filedialog

def wasserzeichen_setzen():
    wasserzeichen_text = wasserzeichen_textfeld.get()
    wasserzeichen_winkel = wasserzeichen_winkel_regler.get()
    wasserzeichen_font = (ausgewählter_font.get(), schriftgrösse_regler.get, "bold")
    wass
   # wasserzeichen_font = f"{ausgewählter_font.get()} 40 Bold"
    canvas.create_text(200, 200, text=wasserzeichen_text, font = wasserzeichen_font, angle=wasserzeichen_winkel_regler.get())