# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

# app.debug = True and app.run() are now in a conditional
# I expect this to have the same behavior as the previous code given the file is not imported

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
