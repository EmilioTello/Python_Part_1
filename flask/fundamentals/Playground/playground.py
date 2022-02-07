from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html',num=3, color='lightskyblue')


@app.route('/play/<int:num>')
def any_number(num):
    return render_template('index.html',num=num, color='lightskyblue')

@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    return render_template('index.html',num=num, color=color)


if __name__=="__main__":
    app.run(debug=True)