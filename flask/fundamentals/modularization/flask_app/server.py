from flask_app import app
from flask_app.controllers import dogs, doctors, owners

if __name__=="__main__":
    app.run(debug=True, port = 5000)