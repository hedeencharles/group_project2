from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index')
def about():
    return render_template("index.html")

@app.route('/about)
def about():
    return render_template("about.html")
    
app.run(debug=True, port=5000)