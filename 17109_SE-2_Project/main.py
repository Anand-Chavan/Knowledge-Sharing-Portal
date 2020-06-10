from config import mysql,app
import flask
from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask import request, jsonify

pid = 0

@app.route('/api/v1/resources/books/all', methods=['GET'])
def getAll():
    cur = mysql.connection.cursor()
    cur.execute("select * from project_detail")
    myresult = cur.fetchall()
    return jsonify(myresult)

@app.route('/api/v1/resources/books/delete/<string:pid>', methods=['DELETE'])
def delete(pid):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM project_detail WHERE pid = %s",pid)
    mysql.connection.commit()
    return "Delete Successfully"


@app.route('/api/v1/resources/books/insert', methods=['POST'])
def add():
    data = request.get_json()
    cur = mysql.connection.cursor()
    mySql_insert_query = """INSERT INTO project_detail  (pid, pname, pauthor, pdescription) 
                                VALUES (%s, %s, %s, %s) """

    recordTuple = (data['pid'],data['pname'],data['pauthor'],data['pdescription'])
    cur.execute(mySql_insert_query, recordTuple)
    mysql.connection.commit()# cur.commit()
    return jsonify(data)

@app.route('/api/v1/resources/books/update/<int:pid>', methods=['PUT'])
def update(pid):
    data = request.get_json()
    cur = mysql.connection.cursor()
    mySql_insert_query = """UPDATE project_detail SET pid =%s ,pname =%s , pauthor = %s , pdescription =%s WHERE pid = %s """

    recordTuple = (data['pid'],data['pname'],data['pauthor'],data['pdescription'],pid)
    cur.execute(mySql_insert_query, recordTuple)
    mysql.connection.commit()# cur.commit()
    return jsonify(data)


@app.route('/', methods=['GET'])
def getAllProject():
    cur = mysql.connection.cursor()
    cur.execute("select * from users")
    myresult = cur.fetchall()
    return jsonify(myresult)

@app.route('/api/v1/resources/books/delete/<string:pid>', methods=['DELETE'])
def deleteSomeProject(pid):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM project_detail WHERE pid = %s",pid)
    mysql.connection.commit()
    return "Delete Successfully"


@app.route('/api/v1/resources/books/insert', methods=['POST'])
def addSomeProject():
    data = request.get_json()
    cur = mysql.connection.cursor()
    mySql_insert_query = """INSERT INTO project_detail  (pid, pname, pauthor, pdescription) 
                                VALUES (%s, %s, %s, %s) """

    recordTuple = (data['pid'],data['pname'],data['pauthor'],data['pdescription'])
    cur.execute(mySql_insert_query, recordTuple)
    mysql.connection.commit()# cur.commit()
    return jsonify(data)

@app.route('/api/v1/resources/books/update/<int:pid>', methods=['PUT'])
def updateSomeProject(pid):
    data = request.get_json()
    cur = mysql.connection.cursor()
    mySql_insert_query = """UPDATE project_detail SET pid =%s ,pname =%s , pauthor = %s , pdescription =%s WHERE pid = %s """

    recordTuple = (data['pid'],data['pname'],data['pauthor'],data['pdescription'],pid)
    cur.execute(mySql_insert_query, recordTuple)
    mysql.connection.commit()# cur.commit()
    return jsonify(data)


app.run()

