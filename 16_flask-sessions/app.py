# Chloe Wong, Tiffany Yang, Claire Song
# Team X
# SoftDev
# K15 -- user sessions
# 2024-10-9
# Time Spent:

import os

from flask import Flask, render_template, request, session

app = Flask(__name__)    #create Flask object

app.secret_key = os.urandom(32)

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***")
    #print(request.args)
    session['username'] = request.args
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***")
    #print(request.args)
    if request.cookies.get('username') == request.args:
        return render_template( 'response.html', response=request.args['username'], method=request.method )
    else:
        return render_template( 'login.html' )

@app.route("/logout") # , methods=['GET', 'POST'])
def logout():
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***")
    #print(request.args)
    session.pop('username')
    return render_template( 'logout.html' )

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
