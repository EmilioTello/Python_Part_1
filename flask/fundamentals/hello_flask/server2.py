from flask import Flask, render_template, Response
# from flask import HttpResponse
# from flask import Flask # instantiating the app
app= Flask(__name__)

@app.route('/') # this is the same thing as localhost:5000/
def index():
    this_name = "Bob Ross"
    name_list = [this_name, "Fred Rogers", "Mr. T", "Bob Barker"]
    return render_template("index.html", name = this_name, all_names = name_list)

# @app.route('/mel') # this is the same thing as localhost:5000/mel
# def mel():
#     return "Mel's Page"


# @app.route('/hello/<string:name>') # this is the same thing as localhost:5000/carlos
# def say_hello(name):
#     return f"Hi, welcome to {name}'s page"


# @app.route('/<int:num_a>and<int:num_b>')
# def add(num_a, num_b):
#     return str(num_a+num_b)

if __name__=="__main__": # are we directly running this file?
    app.run(debug=True)



