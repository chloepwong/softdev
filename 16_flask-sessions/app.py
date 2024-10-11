# Chloe Wong, Tiffany Yang, Claire Song
# Team X
# SoftDev
# K15 -- user sessions
# 2024-10-9
# Time Spent:

import os

from flask import Flask, render_template, request, session, url_for

app = Flask(__name__)    #create Flask object

app.secret_key = os.urandom(32)

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    if 'username' in session:
        return render_template( 'response.html', response=session['username'], method=request.method)
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    session['username'] = request.args['username']
    return redirect(url_for('disp_loginpage'))

@app.route("/logout") # , methods=['GET', 'POST'])
def logout():
    session.pop('username')
    return render_template( 'logout.html' )

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
