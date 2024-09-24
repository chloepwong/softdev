# Chloe Wong, Jackie Zeng
# SoftDev
# September 2024

# This is the same code from K08.
# It leads to a site that states "No hablo queso!" and prints __main__ in the console.

from flask import Flask
app = Flask(__name__)          # Create instance of class Flask

@app.route("/")                # Assign function to route
def hello_world():
    print(__name__)            # Print __main__ in console
    return "No hablo queso!"   # Write "No hablo queso!" in site

app.run()                      # Run application
                
