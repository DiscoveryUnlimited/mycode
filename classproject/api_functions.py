#!/usr/bin/env python3
""" Alta3 Research Project | JPagan
    Astrophysics Functions"""

# imports
import requests
from PIL import Image
import urllib.request


def planet_list():
    """List of planets"""

    # API URL
    SS_API = "https://api.le-systeme-solaire.net/rest/bodies/"

    # make API call and sort data
    bodiesrequest = requests.get(SS_API)
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
    SS_API = "https://api.le-systeme-solaire.net/rest/bodies/"

    # make API call and sort data
    bodiesrequest = requests.get(SS_API)
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
    """space picture of the day"""

    # API URL and key
    NASA_API = "https://api.nasa.gov/planetary/apod?"
    NASA_KEY = "api_key=" + "ZqrQl0M6SGoFZNND3HphsebfoAVJ8AfDjA7hVpgj"

    # make API call and sort data
    picrequest = requests.get(NASA_API + NASA_KEY)
    picdata = picrequest.json()

    # URL and title variables
    picURL = picdata["url"]
    picTitle = picdata["title"]

    # file name
    filename = "./classproject/assets/dailypic.jpg"

    # save URL to file
    urllib.request.urlretrieve(picURL, filename)

    # Opens a image in RGB mode
    im = Image.open(filename)

    # Size of the image in pixels (size of original image)
    width, height = im.size

    # Resize image
    new_width = 400
    new_height = new_width*(height/width)
    newsize = (new_width, int(new_height))
    im.thumbnail(newsize)

    # save image
    im.save(filename, "JPEG")

    return picTitle


def space_crew():
    """People in space"""

    # API URL
    peopleURL = "http://api.open-notify.org/astros.json"

    # make API call and sort data
    peoplerequest = requests.get(peopleURL)
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
