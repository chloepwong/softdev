# Chloe Wong, Jackie Zeng
# SoftDev
# September 2024

# This is the same code as that of v0, except it also prints "about to print __name__..." in the console
# It will show "No hablo queso!" in the site
# It will print "about to print __name__..." then __main__ in the console

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #this goes to the console
    return "No hablo queso!"

app.run()
