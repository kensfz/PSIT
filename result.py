#-*- coding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import ast
app = Flask(__name__)
@app.route("/")
def home(): #โมดูลรับค่าจากไฟล์ index.html โดยการส่งค่าในรูปแบบ POST
    return render_template('home.html')
@app.route('/save', methods=['POST'])
def save(): #โมดูลแสดงข้อมูล
    import mysql.connector
    x = dict(request.form.items())
    hub = ast.literal_eval("%s"%(x))
    name = ''
    contact = ''
    for i in hub:
        if i == 'name':
            name = hub['name']

        elif i == 'contact':
            contact = hub['contact']

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="mydatabase"
    )
    mycursor = mydb.cursor()
    x = dict(request.form.items())
    sql = "INSERT INTO customers (name, contact) VALUES (%s, %s)"
    val = (name, contact)
    mycursor.execute(sql, val)
    mydb.commit()
    iduse = mycursor.lastrowid
    ans_1(iduse)
    return render_template('answer.html')
@app.route('/ans', methods=['POST'])
def ans(): #โมดูลแสดงข้อมูล
    x = dict(request.form.items())
    hub = ast.literal_eval("%s"%(x))
    if hub['answer'] == "answer_1":
        return toans_1()
    if hub['answer'] == "answer_2":
        return answer_2()
    if hub['answer'] == "answer_3":
        return answer_3()

def toans_1():
    return render_template('answer_1.html')
@app.route('/ans_1', methods=['POST'])
def ans_1(iduse):
    print(iduse)

def answer_2():
    print(2222222)
def answer_3():
    print(333333)


app.run(debug=True)
