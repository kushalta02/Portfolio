# importing packages
from flask import Flask
from flask import render_template
import datetime
app = Flask(__name__)
@app.route("/")
def home_page():
    return render_template("home.html")
@app.route("/about")
def aboutpg():
    return render_template("about.html")
@app.route("/projects")
def project():
    return render_template("projects.html")
@app.route("/contact")
def contactpg():
    return render_template("contact.html")

if __name__ == "__main__":
	app.run(debug=True)