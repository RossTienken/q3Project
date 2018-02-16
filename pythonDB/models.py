from index import db

class Drawings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    fileName = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255), unique=True)

    def __init__(self, name, fileName):
        self.name = name
        self.fileName = fileName
