# Tiffany Yang, Chloe Wong
# Team X
# SoftDev
# K08
# 2024-09-20
# time spent: 0.5 hr

'''
DISCO:
When the code is run, a link leading to a page that staets "No hablo queso!" is provided.

QCC:
0. This is similar to object creation in a class in Java.
1. / refers to the root.
2. It prints to a local file.
3. It prints "No hablo queso!"
4. It appears on the website that is generated when the code is run. I can open the link that is provided.
5. This is similar to putting text into a website in HTML.
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?


