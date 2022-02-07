from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "super secret pizza"

@app.route('/')
def count():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template('index.html')

@app.route('/addtwo')
def add_two():
    session["count"] += 1
    return redirect('/')

@app.route('/addany', methods=['POST'])
def add_any():
    session['number'] = request.form['number']
    return redirect('/')


@app.route('/destroy')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)