from flask_app.config.mysqlconnection import connectToMySQL

class Dog:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.breed = data['breed']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
