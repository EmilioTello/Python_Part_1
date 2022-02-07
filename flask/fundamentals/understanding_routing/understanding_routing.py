from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def hi_name(name):
    print(name)
    return f"Hi " + name +"!"

@app.route('/repeat/<int:number>/<string:word>')
def say_it_lots(number, word):
    print(number)
    print(word)
    return (number * word)

# @app.route('/hello/<string:banana>/<int:num>')
# def hello(banana,num):
#     return render_template("hello.html", banana= banana, num= num)

if __name__=="__main__":
    app.run(debug=True)