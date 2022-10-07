#!/usr/bin/env python3
""" Alta3 Research Project | JPagan
    Astrophysics Functions"""

# imports
from matplotlib.pyplot import title
import requests
import json
from PIL import Image
import urllib.request


def planet_list():
    # API URL
    SS_API = "https://api.le-systeme-solaire.net/rest/bodies/"

    # make a call to NASAAPI with our key
    bodiesrequest = requests.get(SS_API)

    # json
    bodydata = bodiesrequest.json()

    bodies = bodydata.get('bodies')

    names = []

    for body in bodies:
        if body.get('isPlanet') and body.get('englishName') != "Earth":
            names.append(body.get('englishName'))

    return names


def planet_info(planet):
    # API URL
    SS_API = "https://api.le-systeme-solaire.net/rest/bodies/"

    # make a call to NASAAPI with our key
    bodiesrequest = requests.get(SS_API)

    # json
    bodydata = bodiesrequest.json()

    bodies = bodydata.get('bodies')

    data = []

    for body in bodies:
        if body.get('englishName') != planet:
            data.append(body.get('gravity'))
            data.append((body.get('aphelion') + body.get('perihelion'))/2)
            data.append(body.get('avgTemp'))

    return data


def pic():
    # API URL
    NASA_API = "https://api.nasa.gov/planetary/apod?"
    NASA_KEY = "api_key=" + "ZqrQl0M6SGoFZNND3HphsebfoAVJ8AfDjA7hVpgj"

    # make a call to NASAAPI with our key
    picrequest = requests.get(NASA_API + NASA_KEY)

    # json
    picdata = picrequest.json()

    picURL = picdata["url"]
    picTitle = picdata["title"]

    # file name
    filename = "./classproject/assets/dailypic.jpg"

    # save URL to file
    urllib.request.urlretrieve(picURL, filename)

    # Resize image

    # Opens a image in RGB mode
    im = Image.open(filename)

    # Size of the image in pixels (size of original image)
    width, height = im.size

    # resize
    new_width = 400
    new_height = new_width*(height/width)
    newsize = (new_width, int(new_height))

    im.thumbnail(newsize)
    # Shows the image in image viewer
    im.save(filename, "JPEG")

    return picTitle


def space_crew():
    # API URL
    peopleURL = "http://api.open-notify.org/astros.json"

    # make a request with the request library
    peoplerequest = requests.get(peopleURL)

    # strip off json attachment from our response
    peopledata = peoplerequest.json()

    people = peopledata.get('people')
    num = peopledata.get('number')

    names = []
    craft = []
    for person in people:
        names.append(person.get('name'))
        craft.append(person.get('craft'))

    return names, craft

def planet_weight(weight1, gravity):
    weight2 = weight1*(gravity/9.8)
    return weight2