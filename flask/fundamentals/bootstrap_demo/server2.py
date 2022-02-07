from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "bootstrap demo"

@app.route('/')
def index():
    return render_template('index2.html')


if __name__=="__main__":
    app.run(debug=True)