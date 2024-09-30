from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String(20), nullable=False)
    lastname =  db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    degree = db.Column(db.String(120), nullable=False)
    # Relationship with Participation to access participated competitions
    participations = db.relationship('Participation', backref='student', lazy=True, cascade="all, delete-orphan")


    def __init__(self, id, firstname, lastname, email, degree):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.degree = degree

    def __repr__(self):
        return (f"<Name: {self.firstname} {self.lastname} | "
                f"Email: {self.email} | Degree: {self.degree}>")

    def get_json(self):
        return{
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'degree': self.degree,
        }