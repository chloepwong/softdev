# Chloe Wong, Tiffany Yang, Claire Song
# Team X
# SoftDev
# K19 - databases
# 2024-10-18
# Time Spent: 1 hr

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

studentcsv = csv.DictReader(open('students.csv', newline=''))
coursecsv = csv.DictReader(open('courses.csv', newline=''))

allcourses = []
uniquecourses = set()

for course in coursecsv:
    allcourses.append(course)
    uniquecourses.add(course['code'])
    
uniquecourses = list(uniquecourses)

allstudents = []

for student in studentcsv:
    studentinfo = {
        'name': student['name'],
        'id': student['id'],
        'age': student['age']
    }
    studentscourses = []
    for course in allcourses:
        if course['id'] == student['id']:
            studentinfo[course['code']] = course['mark']
            studentscourses.append(course['code'])
    for course in uniquecourses:
        if course not in studentscourses:
            studentinfo[course] = 'NULL'
    allstudents.append(studentinfo)

c.execute("DROP TABLE IF EXISTS school")
c.execute(f"CREATE TABLE school(name, id, age, {uniquecourses[0]}, {uniquecourses[1]}, {uniquecourses[2]}, {uniquecourses[3]}, {uniquecourses[4]})")

for student in allstudents:
    c.execute(f"INSERT INTO school VALUES ('{student['name']}', {student['id']}, {student['age']}, {student[uniquecourses[0]]}, {student[uniquecourses[1]]}, {student[uniquecourses[2]]}, {student[uniquecourses[3]]}, {student[uniquecourses[4]]})")
    
command = "SELECT * FROM school"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
