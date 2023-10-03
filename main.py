import json, turtle, urllib.request, time, webbrowser
import geocoder


# part 1 ---------------------------------1----------------------------------------

# Define the URL for the API that provides information about the current astronauts
url = "http://api.open-notify.org/astros.json"  # api of the current astronauts

# Send a GET request to the API URL and retrieve the response
response = urllib.request.urlopen(url) # opening the api

# read the response from api
result = json.loads(response.read())

# open a text file by default, and we want to write on it
file = open("iss.txt", "w") 

# write the number of astronauts onboard to the file
file.write("There Are Currently" + str(result["number"]) + " Astronauts On The ISS: \n\n") # Convert the astronaut count (result["number"]) to a string so it can be properly printed.


# Retrieve names of people on board and write them to the file.
people = result["people"]
for p in people: 
    file.write(p["name"] + " - on board" + "\n") # for loop to get names of all people !


# print longitude and latitude of me !
g = geocoder.ip("me")
file.write("\n Your Current Latitude / Longitude Is: " + str(g.latlng)) # converting integer into a string
file.close() # closing the file
webbrowser.open("iss.txt") # opening the file     (type in terminal python main.py for results !!!!!!)

# part 1 ---------------------------------1----------------------------------------




# part 2 ---------------------------------2----------------------------------------

screen = turtle.Screen()
screen.setup(1280, 720) # width and height of our world map (image)
screen.setworldcoordinates(-180,-90,180,90) # creates x and y coordinates of world map

# load map image
screen.bgpic("Map-World.gif")
screen.register_shape("iss.gif")

# Creating a turtle object named 'iss.'
iss = turtle.Turtle()

# Setting the shape of the 'iss' turtle to the registered shape ("iss.gif").
iss.shape("iss.gif")

# Setting the heading (orientation) of the 'iss' turtle to 45 degrees.
iss.setheading(45)

# Lifting the pen (stopping drawing) for the 'iss' turtle.
iss.penup()





# creating a loop to connect to the live data 
while True: 
    #load the current status of iss  (live)
    url="http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    #extract the iss location
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]
    lat = float(lat)
    lon = float(lon)

    # longitude and latitude output to the terminal

    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # Updating ISS location on the map
    iss.goto(lon, lat)

    # Refreshing interval
    time.sleep(3)
    

# part 2 ---------------------------------2----------------------------------------