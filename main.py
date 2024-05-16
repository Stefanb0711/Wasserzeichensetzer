import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
import io

window = Tk()

fonts = ["Times New Roman", "Comic Sans MS", "Courier New"]

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

        canvas.image = ausgewähltes_bild

        canvas.create_image(x_position, y_position, anchor=NW, image=ausgewähltes_bild)

    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")
    # canvas.create_image(50, 50, image= ausgewähltes_bild, anchor=NW)


def datei_speichern():
    try:
        img = Image.new("RGBA", (canvas.winfo_reqwidth(), canvas.winfo_reqheight()), (255, 255, 255, 255))

        draw = ImageDraw.Draw(img)
        canvas.update()

        canvas.postscript(file="temp.ps", colormode="color")
        temp_img = Image.open("temp.ps")
        img.paste(temp_img, (0, 0))

        dateiname = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

        if dateiname:
            # canvas.postscript(file=dateiname, colormode='color')

            img.save(dateiname, format="PNG")

    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")





font_name = "Arial"


RED = "red"
GREEN = "green"
BLUE = "blue"

w_text = ""
w_text_position = (0, 0)
w_angle = None
w_color = None
w_font_size = 20
w_font = ImageFont.truetype("arial.ttf", 20)


def wasserzeichen_setzen():
    global w_text, w_text_position, w_angle, w_color, w_font, w_font_size

    w_text = wasserzeichen_textfeld.get()
    w_text_position = (scale_position_x.get(), scale_position_y.get())
    w_angle = wasserzeichen_winkel_regler.get()
    w_font_size = schriftgrösse_regler.get()

    colorbox_index = colorbox.curselection()
    if colorbox_index:
        selected_color = colorbox.get(colorbox_index)

        if selected_color == "Rot":
            w_color = RED
        elif selected_color == "Grün":
            w_color = GREEN
        elif selected_color == "Blau":
            w_color = BLUE


    if ausgewählter_font.get() == "Times New Roman":
        font_name = "Times New Roman"

    elif ausgewählter_font.get() == "Comic Sans MS":
        font_name = "Comic Sans MS"

    elif ausgewählter_font.get() == "Courier New":
        font_name = "Courier New"

    canvas.create_text(w_text_position, text=w_text, fill=w_color, font=(font_name, w_font_size),angle=w_angle)


def canvas_verstecken():
    if checkbutton_var.get() == 0:
        for item in canvas.find_all():
            canvas.itemconfig(item, state=HIDDEN)
    elif checkbutton_var.get() == 1:
        for item in canvas.find_all():
            canvas.itemconfig(item, state=NORMAL)


def zeige_wert(wert):
    # winkel_label.config(text=f"Wert : {wert}")
    pass


hauptmenü = Menu(window)

#bg_color = '#3D3D3D'

#window.config(background=bg_color, menu=hauptmenü)
window.config(menu=hauptmenü)
window.title("Wasserzeichensetzer")
window.geometry("1200x800")

"""
button_upload = Button(window, text="Upload")
button_upload.grid(column=0, row=0)
#button_upload.pack()
button_save = Button(window, text= "Save")
button_save.grid(column=1, row=0)
"""

canvas = Canvas(window, width=800, height=600, background="white")
canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

datei_menu = Menu(hauptmenü, tearoff=0)
hauptmenü.add_cascade(label="Datei", menu=datei_menu)

datei_menu.add_command(label="Datei auswählen", command=datei_auswählen)
datei_menu.add_command(label="Speichern", command=datei_speichern)

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
font_liste_dropdown.place(x=900, y=280)

textfeld_label = Label(window, text="Text")
textfeld_label.place(x=900, y=350)
wasserzeichen_textfeld = Entry(window)
wasserzeichen_textfeld.place(x=980, y=350)

winkel_setzen_label = Label(window, text="Winkel")
winkel_setzen_label.place(x=900, y=420)
wasserzeichen_winkel_regler = Scale(window, from_=0, to=360, orient=HORIZONTAL, command=zeige_wert)
wasserzeichen_winkel_regler.place(x=1000, y=400)

schriftgrösse_setzen_label = Label(window, text="Schriftgröße")
schriftgrösse_setzen_label.place(x=900, y=470)
schriftgrösse_regler = Scale(window, from_=10, to=100, orient=HORIZONTAL, command=zeige_wert)
schriftgrösse_regler.place(x=1000, y=450)

zeichen_setzen_button = Button(window, text="Wasserzeichen setzen", pady=5, padx=20, command=wasserzeichen_setzen)
zeichen_setzen_button.place(x=900, y=580)

winkel_label = Label(window, text="Winkel: 0 ")

scale_position_x = Scale(window, from_=0, to=800, orient=HORIZONTAL)
scale_position_x.place(x=950, y=120)
scale_position_y = Scale(window, from_=0, to=600, orient=HORIZONTAL)
scale_position_y.place(x=950, y=80)

label_position_x = Label(window, text="X")
label_position_y = Label(window, text="Y")
label_position_x.place(x=900, y=140)
label_position_y.place(x=900, y=100)

elemente = ["Rot", "Grün", "Blau"]

# Listbox erstellen
colorbox = Listbox(window, selectmode=SINGLE,
                   height=3)  # selectmode=tk.SINGLE ermöglicht die Auswahl eines einzelnen Elements
for element in elemente:
    colorbox.insert(END, element)

colorbox.place(x=900, y=200)

checkbutton_var = IntVar(value=1)
vorschau_check_button = Checkbutton(window, text="Zeichenfläche ausblenden", variable=checkbutton_var, command=canvas_verstecken)
vorschau_check_button.place(x=900, y=530)



window.mainloop()
