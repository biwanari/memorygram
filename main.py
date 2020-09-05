from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/testpage")
def testPage():
    return "<h1> welcome administrator this is a testing page</h1>"



if __name__ == "__main__":
    app.run(debug=True)
