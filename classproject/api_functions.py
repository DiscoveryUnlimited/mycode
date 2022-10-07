#!/usr/bin/env python3
""" Alta3 Research Project | JPagan
    Astrophysics Functions"""

# imports
import urllib.request
import requests
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def planet_list():
    """List of planets"""

    # API URL
    ss_api = "https://api.le-systeme-solaire.net/rest/bodies/"

    # make API call and sort data
    bodiesrequest = requests.get(ss_api)
    bodydata = bodiesrequest.json()
    bodies = bodydata.get('bodies')
    names = []
    for body in bodies:
        if body.get('isPlanet') and body.get('englishName') != "Earth":
            names.append(body.get('englishName'))

    return names


def planet_info(planet):
    """Information about planet"""

    # API URL
    ss_api = "https://api.le-systeme-solaire.net/rest/bodies/"

    # make API call and sort data
    bodiesrequest = requests.get(ss_api)
    bodydata = bodiesrequest.json()
    bodies = bodydata.get('bodies')
    data = []
    for body in bodies:
        if body.get('englishName') == planet:
            data.append(body.get('gravity'))
            data.append((body.get('aphelion') + body.get('perihelion'))/2)
            data.append(body.get('avgTemp'))

    return data


def pic():
    """space picture of the day"""

    # API URL and key
    nasa_api = "https://api.nasa.gov/planetary/apod?"
    nasa_key = "api_key=" + "ZqrQl0M6SGoFZNND3HphsebfoAVJ8AfDjA7hVpgj"

    # make API call and sort data
    picrequest = requests.get(nasa_api + nasa_key)
    picdata = picrequest.json()

    # URL and title variables
    picurl = picdata["url"]
    pictitle = picdata["title"]

    # file name
    filename = "./assets/dailypic.jpg"

    # save URL to file
    urllib.request.urlretrieve(picurl, filename)

    # open image
    img = Image.open(filename)

    # Size of the image in pixels (size of original image)
    width, height = img.size

    # Resize image
    new_width = 350
    new_height = new_width*(height/width)
    newsize = (new_width, int(new_height))
    img.thumbnail(newsize)

    # save image
    img.save(filename, "JPEG")

    return pictitle


def space_crew():
    """People in space"""

    # API URL
    peopleurl = "http://api.open-notify.org/astros.json"

    # make API call and sort data
    peoplerequest = requests.get(peopleurl)
    peopledata = peoplerequest.json()
    people = peopledata.get('people')
    names = []
    craft = []
    for person in people:
        names.append(person.get('name'))
        craft.append(person.get('craft'))

    return names, craft


def planet_weight(weight1, gravity):
    """Calculate force on surface of other body"""

    # force calcualation
    weight2 = weight1*(gravity/9.8)

    return weight2


def planet_gravity(planet):
    """gravity function"""

    # API URL
    ss_api = "https://api.le-systeme-solaire.net/rest/bodies/"

    # make API call and log mass
    bodiesrequest = requests.get(ss_api)
    bodydata = bodiesrequest.json()
    bodies = bodydata.get('bodies')
    mass = float()
    radius = float()
    for body in bodies:
        if body.get('englishName') == planet:
            massdata = body.get('mass')
            mass = massdata.get('massValue')*(10**massdata.get('massExponent'))
            radius = body.get('meanRadius')*1000

    # calculation variables
    g_constant = 6.6743*(10**(-11))  # m^3/(kg s^2)
    radial_max = 4*radius

    # plot data
    plt.figure(figsize=(8, 5))
    inc_r = (radial_max/1000)

    # arguments
    radi = np.arange(radius, radial_max, inc_r)
    grav = g_constant*(mass/(radi**2))

    # lables
    plt.title("Gravity of Planet", fontsize=20)
    plt.xlabel("Radial Distance from Center (m)", fontsize=17)
    plt.ylabel("Gravity (m/s²)", fontsize=17)
    plt.axvline(radius, color="black", ls="--", label=f'Radius: {radius} m')
    plt.legend(loc='upper center', fontsize=14)
    plt.plot(radi, grav)
    plt.savefig('./assets/gravity.png')
