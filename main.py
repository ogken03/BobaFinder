import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from playsound import playsound
from GoogleMapsPart import BobaSearch
from io import StringIO
import sys


def play_music():
        playsound('MainMenuMusic.mp3', block=False)

def submit_data():
    state = state_entry.get()
    city = city_entry.get()
    zip_code = zip_entry.get()

    sys.stdout = StringIO()
    GMobj = BobaSearch(city, state, zip_code)
    output_text = sys.stdout.getvalue()

    submit_button.place_forget()
    frame.place_forget()
    show_new_screen(state, city, zip_code, output_text)

def show_new_screen(state, city, zip_code,output_text):

    new_frame = ttk.Frame(root)
    new_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    ttk.Label(new_frame, text="Boba Search Results", font=(modern_font, 16)).pack()
    ttk.Label(new_frame, text=f"State: {state}", font=modern_font).pack()
    ttk.Label(new_frame, text=f"City: {city}", font=modern_font).pack()
    ttk.Label(new_frame, text=f"Zip Code: {zip_code}", font=modern_font).pack()

    canvas = tk.Canvas(new_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(new_frame, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    content_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

    output_label = ttk.Label(content_frame, text=output_text, font=modern_font, wraplength=900)
    output_label.pack()



    back_button = ttk.Button(content_frame, text="Back", command=lambda: go_back(new_frame))
    back_button.pack(anchor=tk.NW)
    style.configure("TButton", font=modern_font,foreground="black", background="#007BFF",relief=tk.RAISED, borderwidth=0,anchor="center")


    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * (event.delta // 120), "units"))

    canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))


def show_console_output(output_text):

    popup_window = tk.Toplevel(root)
    popup_window.title("Console Output")


    ttk.Label(popup_window, text=output_text, font=modern_font).pack()

def go_back(new_frame):

    new_frame.destroy()
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    submit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

def update_background_position():
    global background_offset
    background_offset -= 1
    canvas.move(background_image_id, -1, 0)



    if background_offset <= -100:
        background_offset = 0
        canvas.move(background_image_id, 100, 0)

    root.after(50, update_background_position)


root = tk.Tk()
root.title("bobafinder")



play_music()


window_width = 700
window_height = 400
root.geometry(f"{window_width}x{window_height}")


root.resizable(False, False)


modern_font = ("Helvetica", 12)


canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()


#THIS IS THE MAIN MENU ATTRIBUTES
background_path = "background.png"
background_image = Image.open(background_path)
background_photo = ImageTk.PhotoImage(background_image)


background_offset = 0
background_image_id = canvas.create_image(background_offset, 0, image=background_photo, anchor=tk.NW, tag="background")


label_frame = ttk.Frame(root)
label_frame.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


image_path = "booba.png"
image = Image.open(image_path)
image = image.resize((50, 50))
logo_image = ImageTk.PhotoImage(image)

bobafinder_label = ttk.Label(label_frame, text="bobafinder", image=logo_image, compound="left", font=(modern_font, 24))
bobafinder_label.pack(side=tk.LEFT, padx=10)


frame = ttk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

state_label = ttk.Label(frame, text="State:", font=modern_font)
state_label.grid(row=0, column=0, padx=5, pady=5)
state_entry = ttk.Entry(frame, font=modern_font)
state_entry.grid(row=0, column=1, padx=5, pady=5)

city_label = ttk.Label(frame, text="City:", font=modern_font)
city_label.grid(row=1, column=0, padx=5, pady=5)
city_entry = ttk.Entry(frame, font=modern_font)
city_entry.grid(row=1, column=1, padx=5, pady=5)

zip_label = ttk.Label(frame, text="Zip:", font=modern_font)
zip_label.grid(row=2, column=0, padx=5, pady=5)
zip_entry = ttk.Entry(frame, font=modern_font)
zip_entry.grid(row=2, column=1, padx=5, pady=5)


submit_button = ttk.Button(root, text="Submit", command=submit_data, style="Modern.TButton")
submit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)



#ADJUSTING STYLE AND LOOKS
style = ttk.Style()
style.configure("Modern.TButton", font=modern_font, foreground="black", background="#007BFF")

style.configure("TButton",font=modern_font,foreground="white",background="#007BFF",relief=tk.RAISED,borderwidth=0,anchor="center")
style.map("TButton",relief=[("pressed", tk.SUNKEN), ("active", tk.RIDGE)])

style.configure("TEntry",font=modern_font,foreground="black",relief=tk.SOLID,borderwidth=2,anchor="w")


update_background_position()

root.mainloop()
