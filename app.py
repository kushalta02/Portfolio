from flask import Flask ,render_template, url_for,redirect, session
import sqlite3
app=Flask(__name__)
app.secret_key = "kushalta_portfolio_secret"

conn = sqlite3.connect("portfolio.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS portfolio_stats (
    id INTEGER PRIMARY KEY,
    views INTEGER
)
""")

cur.execute("SELECT * FROM portfolio_stats")

if cur.fetchone() is None:
    cur.execute(
        "INSERT INTO portfolio_stats (id, views) VALUES (1, 100)"
    )

conn.commit()
conn.close()

print("Database created successfully!")


@app.route("/")
def index():

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()
    cursor.execute(
    "UPDATE portfolio_stats SET views = 247 WHERE id = 1"
)


    if not session.get("viewed"):

        cursor.execute(
            "UPDATE portfolio_stats SET views = views + 1 WHERE id = 1"
        )
        
        conn.commit()

        session["viewed"] = True

    cursor.execute(
        "SELECT views FROM portfolio_stats WHERE id = 1"
    )

    views = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        views=views
    )
@app.route("/About")
def abt():
    return render_template("About.html")
@app.route("/Skills")
def skills():
    return render_template("Skill.html")
@app.route("/Experience")
def experience():
    return render_template("Experience.html")
@app.route("/Projects")
def projects():
    return render_template("Projects.html")
@app.route("/Certificates")
def certificates():
    return render_template("Certificates.html")
@app.route("/Contact")
def contact():
    return render_template("Contact.html")
@app.route("/Resume")
def resume():
    return redirect(url_for('static', filename='resume/RESUME.pdf'))
if __name__=="__main__":
    app.run(debug=True)