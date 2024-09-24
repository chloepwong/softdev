# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

# This code adds app.debug = True
# I expect it to have similar behavior to previous code but with some debugging mechanism
# The page automatically reloads with code updates and gives errors when applicable

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #this goes to the console
    return "No hablo queso!"

app.debug = True
app.run()
