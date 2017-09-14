from flask import Flask, render_template, request, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friends')
# an example of running a query
print mysql.query_db("SELECT * FROM friends")


@app.route('/')
def index():
    friendslist = mysql.query_db('SELECT friends.name, friends.age, DATE_FORMAT(friends.created_at, "%b %D") as created_at, Year(friends.created_at) as created_year FROM friends')

    return render_template('index.html', friendslist = friendslist)



@app.route('/addfriend', methods=['post'])
def addfriend():
    name = request.form['name']
    age = request.form['age']
    query = 'INSERT INTO friends (name, age, created_at) VALUES (:name, :age, now())'
    data = {'name': name, 'age': age}

    mysql.query_db(query, data)
    print "ADDING FRIEND: ", name, age
    return redirect('/')





app.run(debug=True)
