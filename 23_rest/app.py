# Chloe Wong, Ziyad Hamed
# Team TBD
# SoftDev
# K23 - Rest APIs
# 2024-11-20
# Time Spent: .5 hr

from flask import Flask, render_template
import urllib.request
import json

with open("key_nasa.txt", "r") as file:
    key = file.read().strip()
    
app = Flask(__name__)

@app.route('/')
def index():
    data = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + key)
    info = json.loads(data.read())
    return render_template('main.html', image = info['hdurl'], explanation = info['explanation'])

if __name__ == '__main__':
    app.debug = True
    app.run()