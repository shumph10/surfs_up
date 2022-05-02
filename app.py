from flask import Flask
#create new flask instance called app
    #variables with the __ __ are valled magic methods in python
    #can be used to det if your code is being run from command line or 
    #imported into another piece of code
app = Flask(__name__)
#create flask route
    #need to ident a starting point aka a route
    #done with funct @app.route('/')
        #/ denotes we want to put our data at the root of our route
        #/ is the highest level of hierarchy in any computer system
@app.route('/')
#create a funct called hello world 
def hello_world():
    return 'Hello world'

#then have to run on the command w/ the FLASK_APP env variable 
    #done with (for windows)
#set FLASK_APP = file_name.py

    #set the flask app env var to the name of our flask file
        #env var are dynamic var on your computer - used to modify how your
        #computer operates
        #this env modifys the path that will run  our file so we can run it
#have to use:
#flask run
#to actually run it



