# Paradimgs Final Project

# API usage information
The idea of our api is to create a database of all discovered exo-planets. In order to do this one must first make an instance of the class and then load the data from a specified file using the function load_planets(). After this the user can get information about a single specified planet or about all the planets in the database at a time (using get_planet() and get_planets() respectively), delete the information about a single speciifed planet or all the planets at a time (using delete_planet() and delete_planets() respecitvely), set the information about a single specified planet (using set_planet()) and get information about the planet scaled in terms of earth (using scale_to_earth()).

# API features
As mentioned we allow users to load information about the planets from a specified file into the database and then get and edit the data about those planets usually one at a time.

# Server port number
The port we used was 51020, which was Andrew's assigned port for the 
other project

# Server usage information
We made some changes since the pdf file to the way we are doing the 
webservice. The slight changes are that we added a reset url and added a 
scaled url to differentiate the scaled to earth version with the normal 
version of getting a planet. 

Otherwise we formatted the webservice similarly to the cherrypy project. 
We decided to make everything within one controller because there is a 
small enough scope of different features that we feel that they fit 
naturally together in one file. 

We used a different url for the reset to 
allow us to make it more intuitive for the user as opposed to using a 
normal post. We used a different url for the scaled because we have to 
differentiate the different get requests

The server maps pretty directly to the functions from the API so none of 
the handler functions are overly complex. 

# It should now describe the total steps for running your entire project code, including steps on how to start the server.
