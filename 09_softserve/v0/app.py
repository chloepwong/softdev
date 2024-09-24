# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

# This is the same code from K08.
# It leads to a site that states "No hablo queso!" and prints __main__ in the terminal.

from flask import Flask
app = Flask(__name__)          # ...

@app.route("/")                # ...
def hello_world():
    print(__name__)            # ...
    return "No hablo queso!"   # ...

app.run()                      # ...
                
