from flask import Flask, render_template, request, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "SecretSecret"


mysql = MySQLConnector(app, 'friends')


@app.route('/')
def index():

    return render_template('index.html')



@app.route('/checkforemail', methods=['post'])
def checkforemail():
    email = request.form['email']
    data = {'email': email}

    email_query = 'SELECT email FROM friends WHERE email= :email'
    email_query_result = mysql.query_db(email_query, data)

    if email_query_result:
        print "Email Match Found"
        update_query = 'UPDATE friends SET updated_at=now() WHERE friends.email = :email'
        mysql.query_db(update_query, data)

        flash('The email address you entered (%s) is a VALID email address! Thank you!' % email)

        session['matched_users'] += mysql.query_db('SELECT name, email, DATE_FORMAT(updated_at, "%m/%e/%Y %h:%i%p") as updated FROM friends WHERE friends.email = :email', data)

        print session['matched_users']

        return redirect('/success')

    else:
        print "NO Email Match Found"
        flash('No match found for %s.' % email)
        return redirect('/')



@app.route('/success')
def success():

    return render_template('success.html')





app.run(debug=True)
