from flask import Flask, render_template, request, redirect

from users import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template('read.html', users=User.get_all())


@app.route('/create_user_page')
def create_user_page():
    return render_template('create.html')


@app.route('/add_new_user', methods=['POST'])
def add_new_user():
    print(request.form)
    User.save(request.form)
    return redirect('/users')




if __name__ == "__main__":
    app.run(debug=True)