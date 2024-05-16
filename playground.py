import tkinter as tk
from PIL import ImageTk, Image



def place_image_on_canvas(canvas):
    # Bild laden
    image = Image.open("Hintergrund.png")  # Passe den Dateinamen entsprechend an

    photo = ImageTk.PhotoImage(image)
    canvas.image = photo

    # Bild auf dem Canvas platzieren
    canvas.create_image(150, 150, anchor=tk.CENTER, image=photo)

def place_text_on_canvas(canvas):
    # Text auf dem Canvas platzieren
    canvas.create_text(100, 100, text="Hallo Welt!", fill="blue", font=("Helvetica", 16))


# Hauptfenster erstellen
root = tk.Tk()
root.title("Text auf Canvas")

# Canvas erstellen
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Text auf dem Canvas platzieren
place_image_on_canvas(canvas)
place_text_on_canvas(canvas)

# Hauptloop starten
root.mainloop()
