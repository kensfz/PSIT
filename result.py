#-*- coding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import ast
app = Flask(__name__)
@app.route("/")
def index(): #โมดูลรับค่าจากไฟล์ index.html โดยการส่งค่าในรูปแบบ POST
    return render_template('index.html')
@app.route('/save', methods=['POST'])


def save(): #โมดูลแสดงข้อมูล
    import mysql.connector
    x = dict(request.form.items())
    hub = "%s"%(x)
    hub = ast.literal_eval(hub)
    txt = str()
    txt2 = str()
    swis = 0
    count = 0
    for i in hub:
        if i == 'name':
            print(hub['name'])
        elif i == 'contact':
            print(hub['contact'])


    #mydb = mysql.connector.connect(
    #  host="localhost",
    #  user="root",
    #  passwd="",
    #  database="mydatabase"
    #)
    #mycursor = mydb.cursor()
    #x = dict(request.form.items())
    #sql = "INSERT INTO customers (name, contact) VALUES (%s, %s)"
    #val = (name, "ssssssssssssssssssssssssssssssssssssssssss")
    #mycursor.execute(sql, val)
    #mydb.commit()

    return "555%s"%(x)




app.run(debug=True)
