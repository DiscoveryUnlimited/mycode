#!/usr/bin/env python3
"""Alta3 Research | JPagan
Pizza with Matplotlib"""

import numpy as np
import time
import matplotlib.pyplot as plt

def main():

    #Welcome
    print("\nWelcome to Pagan's Pescetarian House of Pizza\n")
    time.sleep(2)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Onions', 'Mushrooms', 'Olives', 'Anchovies'
    toppings = ['Onions', 'Mushrooms', 'Olives', 'Anchovies']

    print("""Our toppings are:
 
        -Onions
        -Mushrooms
        -Olives
        -Anchovies
        """)
    time.sleep(2)

    # Input toppings
    a = input(f"What percentage of the pizza would you like to be {toppings[0]}? ")
    b = input(f"What percentage of the pizza would you like to be {toppings[1]}? ")
    c = input(f"What percentage of the pizza would you like to be {toppings[2]}? ")
    d = input(f"What percentage of the pizza would you like to be {toppings[3]}? ")

    time.sleep(1)

    # Get name for order
    print()
    name =  input("What's the name for the order? ")
    print("\nThat will be right up!\n")
    time.sleep(1)

    # Print progress
    print("Progress")
    time.sleep(2)
    print("...", end = " ", flush = True)
    time.sleep(2)
    print("...", end = " ", flush = True)
    time.sleep(2)
    print("...", end = " ", flush = True)
    time.sleep(2)
    print("...", end = " ", flush = True)
    time.sleep(2)
    print(".", end = "", flush = True)
    time.sleep(1)
    print(".", end = "", flush = True)
    time.sleep(1)
    print(".", end = "", flush = True)

    # Assign toppings
    sizes = [a, b, c, d]
    
    explode = [0, 0, 0, 0]
    max_value = max(sizes)
    index = sizes.index(max_value)
    # Explode largest topping percentageS
    explode[index] = 0.1

    # Plotting
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title(f"{name}'s Pizza") #Assign name to pizza

    # Display the graph
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/pizza.png")

    print()
    print("\nOrder up!\n")
    time.sleep(1)
    print("""
    You can grab your pizza at the Static Directory window at:
    
        /home/student/static/pizza.png
    """)
if __name__ == "__main__":
    main()