import time

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/index", methods =['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form.get("fname")

        last_name = request.form.get("lname")

        return "Your name is " + first_name + " " + last_name
    else:
        return render_template('home.html')
    return render_template("index.html")



if __name__ == '__main__':
    app.run()

