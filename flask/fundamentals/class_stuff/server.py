from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "super secret pizza"

language_dict= {
    'python': 'Python',
    'c_sharp': 'C#',
    'rust': 'Rust',
    'ruby': 'Ruby'
}

@app.route('/')
def index ():
    session.clear()
    print(session)
    return render_template("index.html", lang = language_dict)

# @app.route('/process', methods = ['POST'])
# def process ():
#     print(request.form['pet_name'])
#     return render_template("index.html")

@app.route('/process', methods = ['POST'])
def process ():
    print(f"Here is what is currently coming from the form: {request.form}")
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['pet_name'] = request.form['pet_name']
    print(f"Here is what is currently in session: {session}")
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("results.html")

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/purchase/render', methods = ['POST'])
def post_to_render():
    order_total

if __name__=="__main__":
    app.run(debug=True)