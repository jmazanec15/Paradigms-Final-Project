# Paradimgs Final Project

# How should I use the API?
The idea of our api is to create a database of all discovered exo-planets. In order to do this one must first make an instance of the class and then load the data from a specified file using the function load_planets(). After this the user can get information about a single specified planet or about all the planets in the database at a time (using get_planet() and get_planets() respectively), delete the information about a single speciifed planet or all the planets at a time (using delete_planet() and delete_planets() respecitvely), set the information about a single specified planet (using set_planet()) and get information about the planet scaled in terms of earth (using scale_to_earth()).

# What features are a part of the API?
As mentioned we allow users to load information about the planets from a specified file into the database and then get and edit the data about those planets usually one at a time.