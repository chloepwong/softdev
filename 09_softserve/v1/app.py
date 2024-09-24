# Chloe Wong, Jackie Zeng
# SoftDev
# September 2024

# This code is the same as that of v0, except it excludes print(__name__)
# It will write "No hablo queso!" in the site but not print __main__ in the console

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()
