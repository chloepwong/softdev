# Chloe Wong, Tiffany Yang
# Team Unknown
# SoftDev
# K13 -- combining past work
# 2024-9-30
# Time Spent

from flask import Flask, render_template
import random
import csv

app = Flask(__name__)

@app.route("/wdywtbwygp")
def randomjob():
    with open('data/occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    columns = list(rows[0].keys())
    jobs = {columns[0] : [], headers[1] : []}
    for row in rows[1:-1]:
        jobs[columns[0]].append(row[0])
        jobs[columns[1]].append(float(row[1]))
    rand_job = random.choices(jobs[columns[0]], weights=jobs[columns[1]], k=1)[0]
    return render_template('tablified.html', job_info = jobs)


if __name__ == "__main__":
    app.debug = True
    app.run()
