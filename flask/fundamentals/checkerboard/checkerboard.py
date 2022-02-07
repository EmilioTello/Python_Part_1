from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def basic():
    return render_template('index.html', row=8, column=8, color_one='red', color_two='black')

@app.route('/<int:i>')
def rows(i):
    return render_template('index.html', row=i, column=8, color_one='red', color_two='black')

@app.route('/<int:i>/<int:x>')
def rows_and_columns(i,x):
    return render_template('index.html', row=i, column=x, color_one='red', color_two='black')

@app.route('/<int:i>/<int:x>/<string:color_one>/<string:color_two>')
def colors(i,x,color_one,color_two):
    return render_template('index.html', row=i, column=x, color_one=color_one, color_two=color_two)


if __name__=="__main__":   
    app.run(debug=True)

