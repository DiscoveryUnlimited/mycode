#!/usr/bin/env python3
""" Alta3 Research Project | JPagan
    Astrophysics App"""

# imports
import tkinter as tk
import pyglet
from PIL import ImageTk

# set colors
bg_color = "#95A1F1"

# load custom fonts
pyglet.font.add_file("./fonts/Ubuntu-Bold.ttf")
pyglet.font.add_file("./fonts/Raleway-ExtraBold.ttf")

def main():

	def clear_widgets(frame):
		# select all frame widgets and delete them
		for widget in frame.winfo_children():
			widget.destroy()

	def launch():
		if len(name_var.get()) == 0 or weight_var.get() <= 0:
			load_frame1
		elif isinstance(weight_var.get(), float) == False:
			load_frame1
		else:
			load_frame2()


	def load_frame1():
		clear_widgets(frame2)
		clear_widgets(frame3)
		# stack frame 1 above frame 2
		frame1.tkraise()
		# prevent widgets from modifying the frame
		frame1.pack_propagate(False)


		# create logo widget
		logo_img = ImageTk.PhotoImage(file="assets/Astrophysics2_logo.png")
		logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
		logo_widget.image = logo_img
		logo_widget.pack()

		# create label widget for instructions
		tk.Label(
			frame1, 
			text="Welcome Space Cadet",
			bg=bg_color,
			fg="black",
			font=("Raleway", 30)
			).pack(pady=20)

		# create label widget for instructions
		tk.Label(
			frame1, 
			text="Enter Your Name",
			bg=bg_color,
			fg="white",
			font=("Raleway", 14)
			).pack()

		# create name entry widget
		name_var.set("")
		tk.Entry( frame1,
			textvariable = name_var,
			font=("Ubuntu", 12)
			).pack(pady=10)
		
		# create label widget for instructions
		tk.Label(
			frame1, 
			text="Enter Your Weight",
			bg=bg_color,
			fg="white",
			font=("Raleway", 14)
			).pack()
		
		# create weight entry widget
		weight_var.set("")
		tk.Entry( frame1,
			textvariable = weight_var,
			font=("Ubuntu", 12)
			).pack(pady=10)
		

		# create button widget
		
		tk.Button(
			frame1,
			text="LAUNCH",
			font=("Ubuntu", 20),
			bg="#272740",
			fg="white",
			cursor="hand2",
			activebackground="#45458B",
			activeforeground="black",
			command=lambda:launch()
			).pack(pady=20)

	def load_frame2():
		clear_widgets(frame1)
		clear_widgets(frame3)
		# stack frame 2 above frame 1
		frame2.tkraise()

		# variables
		title = "What next?"
		name 	= "Name: " + str(name_var.get())
		weight 	= "Weight: " + str(weight_var.get())
		table_values = [name, weight]


		# create logo widget
		logo_img = ImageTk.PhotoImage(file="assets/Astrophysics2_planet_logo.png")
		logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color)
		logo_widget.image = logo_img
		logo_widget.pack(pady=20)

		# object title widget
		tk.Label(
			frame2, 
			text=title,
			bg=bg_color,
			fg="white",
			font=("Ubuntu", 20)
			).pack(pady=25, padx=25)

		# object table_values widgets
		for i in table_values:
			tk.Label(
				frame2, 
				text=i,
				bg="#272740",
				fg="white",
				font=("Raleway", 12)
				).pack(fill="both", padx=25)
		
		# Calcualte button
		tk.Button(
			frame2,
			text="CALCULATE",
			font=("Ubuntu", 18),
			bg="#272740",
			fg="white",
			cursor="hand2",
			activebackground="#45458B",
			activeforeground="black",
			command=lambda:load_frame3()
			).pack(pady=20)

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
			command=lambda:load_frame1()
			).pack(pady=20)

	def load_frame3():
		clear_widgets(frame1)
		clear_widgets(frame2)
		# stack frame 2 above frame 1
		frame3.tkraise()

		# variables
		title =  "Results:"

		# create logo widget
		logo_img = ImageTk.PhotoImage(file="assets/Astrophysics3_banner_logo.png")
		logo_widget = tk.Label(frame3, image=logo_img, bg=bg_color)
		logo_widget.image = logo_img
		logo_widget.pack(pady=20)

		# title
		tk.Label(
			frame3, 
			text=title,
			bg=bg_color,
			fg="white",
			font=("Ubuntu", 20)
			).pack(pady=25, padx=25)


		# Restart button
		tk.Button(
			frame3,
			text="Restart",
			font=("Ubuntu", 18),
			bg="#272740",
			fg="white",
			cursor="hand2",
			activebackground="#45458B",
			activeforeground="black",
			command=lambda:load_frame1()
			).pack(pady=20)



	# initiallize app
	root = tk.Tk()
	root.title("Astrophysics App")
	root.eval("tk::PlaceWindow . center")

	# User info
	name_var=tk.StringVar()
	weight_var=tk.DoubleVar()
	
	# create a frame widget
	frame1 = tk.Frame(root, width=550, height=700, bg=bg_color)
	frame2 = tk.Frame(root, bg=bg_color)
	frame3 = tk.Frame(root, bg=bg_color)

	# place frame widgets in window
	for frame in (frame1, frame2, frame3):
		frame.grid(row=0, column=0, sticky="nesw")

	# load the first frame
	load_frame1()

	# run app
	root.mainloop()

if __name__ == "__main__":
	main()