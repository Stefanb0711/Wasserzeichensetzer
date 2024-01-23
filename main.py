import tkinter
from tkinter import *
from tkinter import filedialog

window = Tk()

fonts = ["Arial", "Helvetica", "Montserrat"]

ausgewähltes_bild = ""
def datei_auswählen():
    global ausgewähltes_bild
    dateipfad = filedialog.askopenfilename()
    print("Ausgewählte Datei:", dateipfad)
    ausgewähltes_bild = PhotoImage(file=dateipfad)
    try:
        canvas_breite = canvas.winfo_reqwidth()
        canvas_höhe = canvas.winfo_reqheight()

        # Breite und Höhe des Bildes
        bild_breite = ausgewähltes_bild.width()
        bild_höhe = ausgewähltes_bild.height()

        # Berechne Position für die Mitte des Canvas
        x_position = (canvas_breite - bild_breite) // 2
        y_position = (canvas_höhe - bild_höhe) // 2
        canvas.create_image(x_position, y_position, anchor=NW, image=ausgewähltes_bild)

    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")
    #canvas.create_image(50, 50, image= ausgewähltes_bild, anchor=NW)


def wasserzeichen_setzen():
    #Farbe des Wasser zeichens
    selected_index = listbox.curselection()
    wasserzeichen_farbe = "black"
    if selected_index:
        selected_item = listbox.get(selected_index[0])
        if selected_item == "Rot":
            wasserzeichen_farbe = "red"
        elif selected_item == "Grün":
            wasserzeichen_farbe = "green"
        elif selected_item == "Blau":
            wasserzeichen_farbe = "blue"


    wasserzeichen_text = wasserzeichen_textfeld.get()
    wasserzeichen_winkel = wasserzeichen_winkel_regler.get()
    wasserzeichen_font = (ausgewählter_font.get(), schriftgrösse_regler.get(), "bold")
    #schriftgröße = schriftgrösse_regler.get()
   # wasserzeichen_font = f"{ausgewählter_font.get()} 40 Bold"
    canvas.create_text(400, 300, text=wasserzeichen_text, font = wasserzeichen_font, angle=wasserzeichen_winkel, fill=wasserzeichen_farbe)


def canvas_verstecken():

    if checkbutton_var.get() == 0:
        for item in canvas.find_all():
            canvas.itemconfig(item, state=HIDDEN)
    elif checkbutton_var.get() == 1:
        for item in canvas.find_all():
            canvas.itemconfig(item, state=NORMAL)

def zeige_wert(wert):
    #winkel_label.config(text=f"Wert : {wert}")
    pass

hauptmenü = Menu(window)

window.config(background='#3D3D3D', menu= hauptmenü)
window.title("Wasserzeichensetzer")
window.geometry("1200x800")

"""
button_upload = Button(window, text="Upload")
button_upload.grid(column=0, row=0)
#button_upload.pack()
button_save = Button(window, text= "Save")
button_save.grid(column=1, row=0)
"""


canvas = Canvas(window, width=800, height=600, background='white')
canvas.grid(column=0, row=1, columnspan=2)

datei_menu = Menu(hauptmenü, tearoff=0)
hauptmenü.add_cascade(label="Datei", menu=datei_menu)

datei_menu.add_command(label="Datei auswählen", command=datei_auswählen)




"""button_black_watermark = Button(window, text="Black", padx=20, pady=5)
button_black_watermark.place(x=900, y=250)

button_blue_watermark = Button(window, text="Blue", padx=20, pady=5)
button_blue_watermark.place(x=1000, y=250)

button_red_watermark = Button(window, text="Red", padx=20, pady=5)
button_red_watermark.place(x=900, y=300)

button_green_watermark = Button(window, text="Green", padx=20, pady=5)
button_green_watermark.place(x=1000, y= 300)"""

ausgewählter_font = StringVar(window)
ausgewählter_font.set(fonts[0])

font_liste_dropdown = OptionMenu(window, ausgewählter_font, *fonts)
print(ausgewählter_font)
font_liste_dropdown.place(x = 900, y = 380)

textfeld_label = Label(window, text="Text")
textfeld_label.place(x= 900, y= 440)
wasserzeichen_textfeld = Entry(window)
wasserzeichen_textfeld.place(x = 980, y = 440)

winkel_setzen_label = Label(window, text="Winkel")
winkel_setzen_label.place(x= 900, y= 500)
wasserzeichen_winkel_regler = Scale(window, from_=0, to= 360, orient=HORIZONTAL, command=zeige_wert)
wasserzeichen_winkel_regler.place(x = 1000, y = 500)

schriftgrösse_setzen_label = Label(window, text="Schriftgröße")
schriftgrösse_setzen_label.place(x= 900, y= 550)
schriftgrösse_regler = Scale(window, from_=10, to= 100, orient=HORIZONTAL, command=zeige_wert)
schriftgrösse_regler.place(x = 1000, y = 550)

transparenz_label = Label(window, text="Transparenz")
transparenz_label.place(x= 900, y = 600)
transparenz_regler = Scale(window, from_=0, to= 100, orient=HORIZONTAL)
transparenz_regler.place(x = 1000, y = 600)


zeichen_setzen_button = Button(window, text="Wasserzeichen setzen", pady=5, padx=20, command=wasserzeichen_setzen)
zeichen_setzen_button.place(x= 900, y= 700)

winkel_label = Label(window, text="Winkel: 0 ")


elemente = ["Rot", "Grün", "Blau"]

# Listbox erstellen
listbox = Listbox(window, selectmode=SINGLE, height=3)  # selectmode=tk.SINGLE ermöglicht die Auswahl eines einzelnen Elements
for element in elemente:
    listbox.insert(END, element)

listbox.place(x = 900, y = 300)


checkbutton_var = IntVar(value=1)
vorschau_check_button = Checkbutton(window, text="Vorschau", variable=checkbutton_var, command=canvas_verstecken)
vorschau_check_button.place(x = 900 , y = 650)

"""
dateipfad = "C:/Users/Stefan/Downloads/gif_hintergrund.gif"
ausgewähltes_bild = PhotoImage(file=dateipfad)
try:
    #beispiel_img = PhotoImage(file="C:/Users/Stefan/Downloads/gif_hintergrund.gif")
    canvas.create_image(100, 100, anchor=NW, image=ausgewähltes_bild)
except Exception as e:
    print(f"Fehler beim Laden des Bildes: {e}")
"""

window.mainloop()

