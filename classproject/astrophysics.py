#!/usr/bin/env python3
""" Alta3 Research Project | JPagan
    Astrophysics App"""

# imports
import tkinter as tk
from tkinter import ttk
import pyglet
from PIL import ImageTk
from api_functions import planet_list, planet_info, pic, space_crew, planet_weight, planet_gravity

# font paths
FONT_PATH1 = "./fonts/Raleway-ExtraBold.ttf"
FONT_PATH2 = "./fonts/Ubuntu-R.ttf"
FONT_PATH3 = "./fonts/raleway.medium.ttf"

# image paths
IMG_PATH1 = "./assets/Astrophysics2_logo.png"
IMG_PATH2 = "./assets/Astrophysics2_planet_logo.png"
IMG_PATH3 = "./assets/gravity.png"
IMG_PATH4 = "./assets/dailypic.jpg"
IMG_PATH5 = "./assets/Astrophysics2_banner_logo.png"

# background color
BK_COLOR = "#95A1F1"

# import fonts
pyglet.font.add_file(FONT_PATH1)
pyglet.font.add_file(FONT_PATH2)
pyglet.font.add_file(FONT_PATH3)

# initiallize app
root = tk.Tk()
root.title("Astrophysics App")
root.eval("tk::PlaceWindow . center")

# User info
name_var = tk.StringVar()
weight_str = tk.StringVar()
weight_var = tk.DoubleVar()
destination_var = tk.StringVar()

# create a frame widget
frame1 = tk.Frame(root, width=550, height=800, bg=BK_COLOR)
frame2 = tk.Frame(root, width=550, height=800, bg=BK_COLOR)
frame3 = tk.Frame(root, bg=BK_COLOR)
frame4 = tk.Frame(root, bg=BK_COLOR)

# place frame widgets in window
for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0, column=0, sticky="nesw")


def clear_widgets(frame_num):
    """function to clear current window"""
    for widget in frame_num.winfo_children():
        widget.destroy()


def enlist():
    """executes window loading if input conditions are met"""
    if len(name_var.get()) == 0 or len(weight_str.get()) == 0:
        clear_widgets(frame1)
        load_frame1()
    else:
        try:
            weight_var.set(float(weight_str.get()))
            load_frame2()
        except ValueError:
            clear_widgets(frame1)
            load_frame1()


def load_frame1():
    """loads frame 1"""
    clear_widgets(frame2)
    clear_widgets(frame3)
    clear_widgets(frame4)
    # stack frame 1 above frame 2
    frame1.tkraise()
    # prevent widgets from modifying the frame
    frame1.pack_propagate(False)

    # create logo widget
    logo_img = ImageTk.PhotoImage(file=IMG_PATH1)
    logo_widget = tk.Label(frame1, image=logo_img, bg=BK_COLOR)
    logo_widget.image = logo_img
    logo_widget.pack()

    # create label widget for instructions
    tk.Label(
        frame1,
        text="Welcome Space Cadet",
        bg=BK_COLOR,
        fg="black",
        font=("Raleway ExtraBold", 25)
    ).pack(pady=15)

    # create label widget for instructions
    tk.Label(
        frame1,
        text="Enter Your Name",
        bg=BK_COLOR,
        fg="white",
        font=("Raleway", 16)
    ).pack()

    # create name entry widget
    name_var.set("")
    tk.Entry(frame1,
             textvariable=name_var,
             font=("Ubuntu", 12)
             ).pack(pady=10)

    # create label widget for instructions
    tk.Label(
        frame1,
        text="Enter Your Weight (lbs)",
        bg=BK_COLOR,
        fg="white",
        font=("Raleway", 16)
    ).pack()

    # create weight entry widget
    weight_str.set("")
    tk.Entry(frame1,
             textvariable=weight_str,
             font=("Ubuntu", 12)
             ).pack(pady=10)

    # enlist button
    tk.Button(
        frame1,
        text="ENLIST",
        font=("Ubuntu", 20),
        bg="#272740",
        fg="white",
        cursor="hand2",
        activebackground="#45458B",
        activeforeground="black",
        command=lambda: enlist()
    ).pack(pady=20)


def load_frame2():
    """loads frame 2"""
    clear_widgets(frame1)
    clear_widgets(frame3)
    clear_widgets(frame4)
    # bring frame to front
    frame2.tkraise()

    # variables
    title = "Cadet Data"
    name = "Name: " + str(name_var.get())
    weight = "Weight: " + str(weight_var.get())
    gravity = "Earth Gravity = 9.8 m/s²"
    cadet_values = [name, weight, "", gravity]

    # create logo
    logo_img = ImageTk.PhotoImage(file=IMG_PATH2)
    logo_widget = tk.Label(frame2, image=logo_img, bg=BK_COLOR)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    # page title
    tk.Label(
        frame2,
        text=title,
        bg=BK_COLOR,
        fg="white",
        font=("Raleway ExtraBold", 25)
    ).pack(pady=20, padx=5)

    # cadet values
    for i in cadet_values:
        tk.Label(
            frame2,
            text=i,
            bg="#272740",
            fg="white",
            font=("Raleway", 16)
        ).pack(fill="both", padx=25)

    # dropdown menu title
    tk.Label(
        frame2,
        text="Choose a Landing Site",
        bg=BK_COLOR,
        fg="white",
        font=("Raleway ExtraBold", 20)
    ).pack(pady=25, padx=25)

    # destination dropdown menu
    destination_var.set("")
    planet_name = planet_list()
    ttk.Combobox(
        frame2,
        values=planet_name,
        state="readonly",
        textvariable=destination_var,
        font=("Ubuntu", 16)
    ).pack()

    # Launch button
    tk.Button(
        frame2,
        text="LAUNCH",
        font=("Ubuntu", 18),
        bg="#272740",
        fg="white",
        cursor="hand2",
        activebackground="#45458B",
        activeforeground="black",
        command=lambda: load_frame3()
    ).pack(side="right", pady=20, padx=20)

    # Back button
    tk.Button(
        frame2,
        text="BACK",
        font=("Ubuntu", 18),
        bg="#272740",
        fg="white",
        cursor="hand2",
        activebackground="#45458B",
        activeforeground="black",
        command=lambda: load_frame1()
    ).pack(side="left", pady=20, padx=20)

    # Crew button
    tk.Button(
        frame2,
        text="CREW CHECK",
        font=("Ubuntu", 18),
        bg="#272740",
        fg="white",
        cursor="hand2",
        activebackground="#45458B",
        activeforeground="black",
        command=lambda: load_frame4()
    ).pack(side="left", pady=20, padx=50)


def load_frame3():
    """loads frame 3"""
    clear_widgets(frame1)
    clear_widgets(frame2)
    clear_widgets(frame4)
    # bring frame to front
    frame3.tkraise()

    # variables
    planet = destination_var.get()
    planet_data = planet_info(planet)
    gravity = planet_data[0]
    avg_dis = planet_data[1]
    avg_temp = planet_data[2]-273.15
    weight = planet_weight(weight_var.get(), gravity)

    # fact statements
    planet_facts = [
        planet.capitalize() + " Gravity = " + str(round(gravity, 2)) +
        " m/s² on it's surface.",
        "It has an average distance from the Sun of " +
        str(round(avg_dis, 2)) + " km",
        "The average temperature is " + str(round(avg_temp, 2)) + " °C",
        "",
        "If you were standing on the surface of " + planet.capitalize(),
        "you would weigh " + str(round(weight, 2)) + " lbs"]

    # create logo widget
    logo_img = ImageTk.PhotoImage(file=IMG_PATH5)
    logo_widget = tk.Label(frame3, image=logo_img, bg=BK_COLOR)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    # title
    tk.Label(
        frame3,
        text=planet,
        bg=BK_COLOR,
        fg="black",
        font=("Raleway ExtraBold", 35)
    ).pack(pady=25, padx=25)

    # create figure
    planet_gravity(planet)
    # create logo widget
    logo_img1 = ImageTk.PhotoImage(file=IMG_PATH3)
    logo_widget1 = tk.Label(frame3, image=logo_img1, bg=BK_COLOR)
    logo_widget1.image = logo_img1
    logo_widget1.pack(pady=20, padx=25)

    # planet data
    for i in planet_facts:
        tk.Label(
            frame3,
            text=i,
            bg="#272740",
            fg="white",
            font=("Ubuntu", 20)
        ).pack(fill="both", padx=25)

    # Quit button
    tk.Button(
        frame3,
        text="QUIT",
        font=("Ubuntu", 18),
        bg="#272740",
        fg="white",
        cursor="hand2",
        activebackground="#45458B",
        activeforeground="black",
        command=lambda: root.destroy()
    ).pack(pady=20)


def load_frame4():
    """loads frame 4"""
    clear_widgets(frame1)
    clear_widgets(frame2)
    clear_widgets(frame3)
    # bring frame to front
    frame4.tkraise()

    # pic of the day
    caption = pic()

    # create logo widget
    logo_img = ImageTk.PhotoImage(file=IMG_PATH4)
    logo_widget = tk.Label(frame4, image=logo_img, bg=BK_COLOR)
    logo_widget.image = logo_img
    logo_widget.pack(pady=10)

    # caption
    tk.Label(
        frame4,
        text=caption,
        bg=BK_COLOR,
        fg="white",
        font=("Ubuntu", 10)
    ).pack()

    # crew title
    tk.Label(
        frame4,
        text="Crew in Space",
        bg=BK_COLOR,
        fg="white",
        font=("Ubuntu", 20)
    ).pack(pady=25, padx=25)

    # crew info
    crew_names, craft = space_crew()
    for i in range(len(crew_names)):
        tk.Label(
            frame4,
            text=f"{crew_names[i]} : {craft[i]}",
            bg="#272740",
            fg="white",
            font=("Raleway", 12)
        ).pack(fill="both", padx=25)

    # Back button
    tk.Button(
        frame4,
        text="BACK",
        font=("Ubuntu", 18),
        bg="#272740",
        fg="white",
        cursor="hand2",
        activebackground="#45458B",
        activeforeground="black",
        command=lambda: load_frame2()
    ).pack(pady=20)


def main():
    """Runs App"""

    # load the first frame
    load_frame1()

    # run app
    root.mainloop()


if __name__ == "__main__":
    main()
