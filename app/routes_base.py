from flask import render_template


from app import app

@app.route('/')
@app.route('/index')
def index():

    # do something more here

    return render_template("home/dashboard.html")

