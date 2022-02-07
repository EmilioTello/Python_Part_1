from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "dojo survey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print(f"Here is what is currently coming from the form: {request.form}")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    # session['this'] = request.form['this']
    # session['that'] = request.form['that']
    session['accept'] = request.form['accept']
    session['comments'] = request.form['comments']
    print(f"Here is what is currently in session: {session}")
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/reset')
def reset():
    session.clear()
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)